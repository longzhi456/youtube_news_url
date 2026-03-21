#! /usr/bin/python3

import subprocess

def grab(ch_id):
    if not ch_id:
        print('https://xxxx.m3u')
        return

    url = f"https://www.youtube.com/channel/{ch_id}/live"
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text

    match = re.search(r'"videoId":"(.*?)"', html)
    if not match:
        print('https://yyyy.m3u')
        exit()

    video_id = match.group(1)
    watch_url = f"https://www.youtube.com/watch?v={video_id}"
            
    print(match)

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
