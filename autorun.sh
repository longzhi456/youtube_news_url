#!/bin/bash

echo $(dirname $0)

if ! python3 -c "import requests" &>/dev/null; then
    python3 -m pip install requests
fi

set -e  # 脚本中任何错误都会导致立即停止

cd $(dirname $0)/scripts/

python3 youtube_m3ugrabber.py > ../result.m3u

echo m3u grabbed
