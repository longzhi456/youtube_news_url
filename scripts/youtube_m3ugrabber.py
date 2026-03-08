#! /usr/bin/python3

import requests

def get_live_url(channel_id: str) -> str | None:
    url = f"https://www.youtube.com/channel/{channel_id}/live"
        
    try:
        r = requests.get(url, allow_redirects=True, timeout=10)

        if "watch?v=" in r.url:
            return r.url

        return None

    except Exception as e:
        print("error:", e)
        return None

    if __name__ == "__main__":
    channel_id = "UC5nwNW4KdC0SzrhF9BXEYOQ"

    live_url = get_live_url(channel_id)

    if live_url:
        print("LIVE URL:", live_url)
    else:
        print("No live stream")  

with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith('#EXTINF:'):
            print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
        else:
            print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_n2a.m3u')
