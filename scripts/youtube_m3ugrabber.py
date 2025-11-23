#! /usr/bin/python3

import requests
import os
import sys
import re
import yt_dlp
import json
from bs4 import BeautifulSoup
import subprocess

windows = False
if 'win' in sys.platform:
    windows = True

def grab(youtube_url, timeout=15):
    try:
        # 运行 yt-dlp 命令
        result = subprocess.run(
            ['yt-dlp', '-f', 'best', '--get-url', youtube_url], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        # 获取并返回结果
        m3u8_url = result.stdout.strip()  # 去除输出中的多余空白字符
        if m3u8_url:
            print(m3u8_url)
            return
        else:
            print("https://xxxx.m3u8")
            return None
    except Exception as e:
        print("https://xxxx.m3u8")
        return None
         
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
