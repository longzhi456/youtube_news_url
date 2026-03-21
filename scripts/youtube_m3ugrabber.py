#! /usr/bin/python3

import subprocess

def grab(ch_id):
    if not ch_id:
        print('https://xxxx.m3u')
        return

    url = f"https://www.youtube.com/channel/{ch_id}/live"
    result = subprocess.run(
        ["yt-dlp", "--flat-playlist", "-J", url],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("❌ 获取失败")
        print(result.stderr)
        exit()

    data = json.loads(result.stdout)
    entries = data.get("entries", [])
    f not entries:
        print("❌ 没有直播")
        exit()

    video_id = entries[0]["id"]
    watch_url = f"https://www.youtube.com/watch?v={video_id}"
            
    print(watch_url)

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
