"""Build the HTML slides of a Marp talk.

Requires Marp CLI on PATH (https://github.com/marp-team/marp-cli/releases), or the MARP environment variable set to the executable.

    python tools/build_marp_slides.py 281026_RosSinRodeos/ros-sin-rodeos.md

The output for a folder DDMMAA_TalkName is TalkName.html in that folder. The script also inserts a base URL so htmlpreview can load images from the repo.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

markdown = Path(sys.argv[1]).resolve()
folder = markdown.parent
output = folder / (folder.name.split("_", 1)[-1] + ".html")
marp = os.environ.get("MARP") or shutil.which("marp")
if not marp:
    sys.exit("marp was not found on PATH. Set MARP to the executable.")

subprocess.run([marp, str(markdown), "--output", str(output)], check=True)

base = f"https://raw.githubusercontent.com/danimtb/talks/master/{folder.name}/"
script = (
    '<script>if(location.protocol!=="file:"){var b=document.createElement("base");'
    f'b.href="{base}";document.head.appendChild(b);}}</script>'
)
html = output.read_text(encoding="utf-8")
output.write_text(html.replace("<head>", "<head>" + script, 1), encoding="utf-8")
