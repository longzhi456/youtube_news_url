#! /usr/bin/python3

import requests

with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            print('https://xxx.m3u')
            return
        if line.startswith('#EXTINF:-1'):
            print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
        else
            print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na1.m3u')
