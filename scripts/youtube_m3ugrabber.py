#! /usr/bin/python3

import requests
import os
import sys
import re
import yt_dlp
import json
from bs4 import BeautifulSoup

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url, timeout=15):
    # 发起请求获取页面内容
    response = requests.get(url)
    html_content = response.text
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 使用正则表达式搜索所有的 m3u8 地址
    m3u8_url = re.findall(r'https?://[^\s]+\.m3u8', html_content)
    
    if m3u8_url:
        print(m3u8_url[0])
        return 
    else:
        print("https://xxxx.m3u8")
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
