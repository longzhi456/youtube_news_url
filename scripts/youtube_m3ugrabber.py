#! /usr/bin/python3

import subprocess

def grab(ch_id):
    if not ch_id:
        print('https://xxxx.m3u')
        return

    result = subprocess.run(
        [
            "yt-dlp",
            "-g",
            "--match-filter", "is_live",
            f"https://www.youtube.com/channel/{ch_id}/videos"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        url = result.stdout.strip()
        if url:
            print(url)
            return
            
    print('https://yyyy.m3u')

    except Exception as e:
        print("ERROR:", e)
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
