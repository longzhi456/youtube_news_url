#! /usr/bin/python3

import requests
import os
import sys
import re

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url, fallback_url="https://xxxx.m3u", timeout=15):
    try:
        response = requests.get(url, timeout=timeout).text
    except requests.RequestException:
        # 请求失败直接返回备用链接
        return fallback_url
        
    # 正则匹配 .m3u8 链接
    match = re.search(r'https://[^\'"\s]+\.m3u8', response)
    if match:
        print(match.group(0))
        return 
    else:
        return

with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    #os.system('rm temp.txt')
    os.system('rm watch*')
