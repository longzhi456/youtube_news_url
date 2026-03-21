#! /usr/bin/python3

import subprocess

def grab(ch_id):
    if not ch_id:
        print('https://xxxx.m3u')
        return

    url = f"https://www.youtube.com/channel/{ch_id}/live"

    result = subprocess.run(
        ["yt-dlp", "-g", "-f", "best", url],
        capture_output=True,
        text=True
    )

    m3u8_url = result.stdout.strip()
    if not m3u8_url:
        print('https://yyyy.m3u')
        return
            
    print(m3u8_url)

with open('../youtube_channel_info.txt') as f:
    print('#EXTM3U x-tvg-url="https://live.fanmingming.cn/e.xml" catchup="append" catchup-source="?playseek=${(b)yyyyMMddHHmmss}-${(e)yyyyMMddHHmmss}"')
    for line in f:
        line = line.strip()
        if line.startswith('#EXTINF:-1'):
            print(line)
        else:
            line = line.split('|')
            ch_id = line[1].strip()
            grab(ch_id)
