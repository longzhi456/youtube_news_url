#! /usr/bin/python3

import requests
import os
import sys
import re
import yt_dlp

windows = False
if 'win' in sys.platform:
    windows = True

def grab(youtube_url, timeout=15):
    with open("../youtube.json", 'r') as js:
        cookies = json.load(js)
        
    ydl_opts = {
        'quiet': True,  # 禁止冗长输出
        'format': 'best',  # 选择最佳质量的流
        'extractor_args': {'youtube': {'live': True}},  # 提取直播流
        'cookiefile': "../youtube.json"  # 提供 cookies 文件
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:       
        info_dict = ydl.extract_info(youtube_url, download=False)
        m3u8_url = info_dict['url']  # 获取 .m3u8 流地址
        if m3u8_url:
            print(m3u8_url)
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
