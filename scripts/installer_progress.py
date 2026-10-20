"""Compact terminal progress for installer commands; never record command arguments."""
import collections
import os
import re
import selectors
import subprocess
import sys
import tempfile
import time

# Suppress entire potentially sensitive lines before writing to disk or showing them.
SENSITIVE = re.compile(r'password|passwort|token|secret|authorization|api.?key|private.?key|BEGIN .*PRIVATE', re.I)
ANSI = re.compile(r'\x1b(?:\[[0-?]*[ -/]*[@-~]|\][^\x07]*(?:\x07|$))')


def clean(line):
    line = ANSI.sub('', line)
    line = ''.join(c for c in line if c in '\n\t' or ord(c) >= 32)
    if SENSITIVE.search(line):
        return '[sensitive output omitted]'
    line = re.sub(r'(https?://)[^/\s]+@', r'\1[redacted]@', line)
    return re.sub(r'\b[0-9a-fA-F]{32,}\b', '[redacted]', line)


def run(command, label):
    en = os.environ.get('HUE2LOX_INSTALL_LANG') == 'en'
    fd, filename = tempfile.mkstemp(prefix='hue2lox-install-', suffix='.log')
    os.fchmod(fd, 0o600)
    tail = collections.deque(maxlen=18)
    frames = (r'    _/ / || \ \_', r'   \_\ \||/ /_/', r'    / / /||\ \ \ ', r'   _\ \ || / /_')
    animated = sys.stdout.isatty() and os.environ.get('TERM') != 'dumb'
    drawn = False
    prompt_mode = False
    private_block = False
    buffer = b''
    last_data = time.monotonic()
    process = None
    print(label + ' …', flush=True)
    def clear_animation():
        nonlocal drawn
        if drawn:
            print('\033[4A\033[J', end='', flush=True)
            drawn = False

    with os.fdopen(fd, 'w', encoding='utf-8') as log:
        def record(raw, partial=False):
            nonlocal prompt_mode, private_block
            decoded = raw.decode('utf-8', errors='replace')
            if 'BEGIN ' in decoded and 'PRIVATE' in decoded:
                private_block = True
            line = '[sensitive output omitted]' if private_block else clean(decoded)
            if 'END ' in decoded and 'PRIVATE' in decoded:
                private_block = False
            log.write(line + '\n'); log.flush()
            tail.append(line)
            # Package tools may ask about existing configuration files.
            if partial or re.search(r'\?|\[.*(?:default|standard).*\]|configuration file|konfigurationsdatei', line, re.I):
                if not prompt_mode:
                    clear_animation()
                    print('\n'.join(tail), flush=True)
                    prompt_mode = True
                else:
                    print(line, flush=True)
            elif prompt_mode:
                print(line, flush=True)

        try:
            # Inherit terminal input so package-manager questions remain answerable.
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            selector = selectors.DefaultSelector()
            selector.register(process.stdout, selectors.EVENT_READ)
            index = 0
            while selector.get_map():
                events = selector.select(0.15)
                for key, _ in events:
                    chunk = os.read(key.fileobj.fileno(), 65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        continue
                    last_data = time.monotonic()
                    buffer += chunk
                    while b'\n' in buffer:
                        line, buffer = buffer.split(b'\n', 1)
                        record(line)
                # An unterminated prompt must also be visible before input is requested.
                if buffer and time.monotonic() - last_data > 0.5:
                    record(buffer, partial=True)
                    buffer = b''
                if animated and not prompt_mode:
                    clear_animation()
                    print('       .----.\n      ( o  o )\n' + frames[index % len(frames)] + '\n  ' + label + ' …', flush=True)
                    drawn = True
                    index += 1
            if buffer: record(buffer)
            code = process.wait()
            selector.close()
            process.stdout.close()
        except KeyboardInterrupt:
            if process is not None:
                process.terminate()
                try: process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill(); process.wait()
            code = 130
        except OSError as error:
            record(str(error).encode())
            code = 1
        finally:
            clear_animation()
    if code:
        print(('Failed: ' if en else 'Fehlgeschlagen: ') + label)
        if not prompt_mode: print('\n'.join(tail))
    else:
        print('✓ ' + label)
    print(('Log: ' if en else 'Protokoll: ') + filename, flush=True)
    return code


if __name__ == '__main__':
    sys.exit(run(sys.argv[2:], sys.argv[1]))
