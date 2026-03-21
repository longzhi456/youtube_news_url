#! /usr/bin/python3

import requests

def grab(ch_id):
    if not ch_id:
        print('https://xxxx.m3u')
        return

    url = f"https://www.youtube.com/channel/{ch_id}/live"
    try:
        r = requests.get(url, allow_redirects=True, timeout=10)
        if "watch?v=" in r.url:
            print(r.url)
            return

        print('https://xxxx.m3u')

    except Exception as e:
        print('https://xxxx.m3u')

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
