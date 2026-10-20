"""Build local dictionaries; no runtime network translation service."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent.parent/'web/locales'
for lang in ('de','en'):
    data=json.loads((root/(lang+'.json')).read_text())
    (root/(lang+'.js')).write_text('window.HUE2LOX_MESSAGES=window.HUE2LOX_MESSAGES||{};\nwindow.HUE2LOX_MESSAGES.'+lang+'='+json.dumps(data,ensure_ascii=False)+';\n')
