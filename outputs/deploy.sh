#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 build.py
python3 qa_check.py
rsync -rlptz --delete site/ "info@ok-marked.com@p-asttdj@ssh.altgemeinde.project.host:/home/p-asttdj/html/webnew2026/"
echo "Deploy fertig."
