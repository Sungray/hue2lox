"""Prepare an isolated fresh installation; never start Docker or contact a bridge."""
import argparse
import ipaddress
import os
from pathlib import Path
import secrets
import shutil
import subprocess
import tempfile
import sys

SOURCE=Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SOURCE / 'src'))
from install_state import initialize

CODE=('.dockerignore','LICENSE','NOTICE','THIRD-PARTY-NOTICES.md','INSTALL.md','RELEASE.md')


def installation_name():
    adjectives = 'jolly happy clever sunny brave gentle merry lucky cosmic nifty calm bright speedy friendly playful curious dancing flying glowing magic smiling tiny mighty quiet silver golden bold cozy lively fancy swift purple'.split()
    animals = 'jumper octopus otter dolphin penguin puffin turtle panda fox badger beaver koala gecko owl raven robin seal whale squid crab lobster manta falcon finch tiger lion lynx rabbit squirrel wombat yak zebra'.split()
    return 'hue2lox-' + secrets.choice(adjectives) + secrets.choice(animals)


def prepare(destination,host,port=8443):
    address=ipaddress.IPv4Address(host)
    if address.is_unspecified or address.is_multicast or not (address.is_private or address.is_loopback):
        raise ValueError('Use a local unicast IPv4 address')
    if type(port) is not int or not 1024<=port<=65535:raise ValueError('Port must be 1024–65535')
    dest=Path(destination).absolute()
    if dest.exists() or dest.is_symlink():raise ValueError('Destination already exists; nothing changed')
    if not dest.parent.is_dir():raise ValueError('Destination parent must exist')
    if not shutil.which('openssl'):raise ValueError('OpenSSL is required')
    work=Path(tempfile.mkdtemp(prefix='.hue2lox-setup-',dir=dest.parent))
    try:
        for file in CODE:shutil.copyfile(SOURCE/file,work/file);(work/file).chmod(0o644)
        for directory in ('src','docker','config','web','catalog','trust','install','docs'):
            shutil.copytree(SOURCE/directory,work/directory)
            for path in (work/directory).rglob('*'):path.chmod(0o755 if path.is_dir() else 0o644)
            (work/directory).chmod(0o755)
        shutil.copyfile(SOURCE/'docker/compose.install.yaml',work/'compose.yaml')
        owner = (10001, 10001) if os.geteuid() == 0 else (None, None)
        initialize(work/'data', work/'certs', work/'secrets', str(address), *owner)
        name = installation_name()
        (work/'.env').write_text(f'COMPOSE_PROJECT_NAME={name}\nHUE2LOX_CONTAINER_NAME={name}-1\nHUE2LOX_BIND_IP={address}\nHUE2LOX_PORT={port}\nHUE_PUBLIC_URL=https://{address}:{port}\nHUE_WRITES_ENABLED=0\nHUE_COLOR_ENABLED=0\nHUE_WHITE_ENABLED=0\n');(work/'.env').chmod(0o600)
        shutil.copyfile(work/'certs/server.crt',work/'health-test.crt')
        # Refuse concurrent creation too, rather than replacing another installation.
        if dest.exists() or dest.is_symlink():raise ValueError('Destination appeared during setup')
        # Allow the SSH user to enter the install directory and read public assets.
        # Private subdirectories and .env retain their restrictive permissions.
        work.chmod(0o755)
        work.rename(dest)
    finally:
        if work.exists():shutil.rmtree(work)
    return dest

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination',required=True);parser.add_argument('--host',required=True)
    parser.add_argument('--port',type=int,default=8443);args=parser.parse_args()
    try:dest=prepare(args.destination,args.host,args.port)
    except (ValueError,OSError,subprocess.SubprocessError) as error:parser.exit(1,'Setup failed: '+str(error)+'\n')
    print('Fresh installation prepared at '+str(dest))
    print('No container started; no Hue requests sent. Control is disabled by default.')
