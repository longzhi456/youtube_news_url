#! /usr/bin/python3

import requests

with open('../youtube_channel_info.txt') as f:
    print('https://111.m3u')
    for line in f:
        line = line.strip()
        #print(f'\nhttps://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na1.m3u')
        if line.startswith('#EXTINF:-1'):
            print(f'\n' + line)
        else
            print(f'\nhttps://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na1.m3u')
