#! /usr/bin/python3

import subprocess

def grab(ch_id):
    if not ch_id:
        print('https://xxxx.m3u')
        return

    try:
        video_id = subprocess.check_output(
            [
                "yt-dlp",
                "--get-id",
                f"https://www.youtube.com/channel/{ch_id}/live"
            ],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        if video_id:
            print(f"https://www.youtube.com/watch?v={video_id}")
        else:
            print('https://yyyy.m3u')

    except Exception as e:
        print('https://eeee.m3u')

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
