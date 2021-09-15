import os

webm = input('webm file name: ')
mp3 = input('mp3 name: ')

os.system(f'ffmpeg -i "{webm}.webm" -vn -ab 128k -ar 44100 -y "{mp3}.mp3";')