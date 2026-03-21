#! /usr/bin/python3

import requests

def grab(ch_id):
    if not ch_id:
         print('https://xxxx.m3u')
    else:
        print('https://yyyy.m3u')

with open('../youtube_channel_info.txt') as f:
    print('#EXTM3U x-tvg-url="https://live.fanmingming.cn/e.xml" catchup="append" catchup-source="?playseek=${(b)yyyyMMddHHmmss}-${(e)yyyyMMddHHmmss}"')
    for line in f:
        line = line.strip()
        if line.startswith('#EXTINF:-1'):
            print(line)
        else:
            line = line.split('|')
            ch_id = line[1].strip()
            print(ch_id)
