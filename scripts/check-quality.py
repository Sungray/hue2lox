"""Offline syntax, generated translation and documentation checks (no devices)."""
import ast
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
for path in sorted(ROOT.glob('*.py')) + sorted((ROOT / 'tests').rglob('*.py')) + sorted((ROOT / 'scripts').glob('*.py')) + sorted((ROOT / 'tools').glob('*.py')):
    ast.parse(path.read_text(), filename=str(path))
for path in sorted((ROOT / 'web').rglob('*.js')):
    subprocess.run(['node', '--check', str(path)], check=True, stdout=subprocess.DEVNULL)
for path in sorted(ROOT.glob('*.sh')) + sorted((ROOT / 'scripts').glob('*.sh')):
    interpreter = 'bash' if 'bash' in path.read_text().splitlines()[0] else 'sh'
    subprocess.run([interpreter, '-n', str(path)], check=True)
de = json.loads((ROOT / 'web/locales/de.json').read_text())
en = json.loads((ROOT / 'web/locales/en.json').read_text())
assert de.keys() == en.keys(), 'Translation keys differ'
for name in ('README.md', 'README.en.md', 'MANUAL.md', 'MANUAL.en.md', 'CONTRIBUTING.md', 'SECURITY.md', 'docs/ACCEPTANCE.md'):
    path = ROOT / name
    for target in re.findall(r'\]\(([^\s)]+)', path.read_text()):
        if ':' in target or target.startswith('#'):
            continue
        assert (path.parent / target.split('#')[0]).exists(), f'{name}: missing {target}'
for name in ('README.md', 'README.en.md'):
    assert 'src="web/hue2lox-logo.png"' in (ROOT / name).read_text()
assert (ROOT / 'web/hue2lox-logo.png').is_file()
print('PASS: Python, JavaScript and shell syntax, translation keys, documentation links and README logo.')
