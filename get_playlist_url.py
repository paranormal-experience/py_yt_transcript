import os
try:
  from pytube import Playlist
  from art import *
except ModuleNotFoundError:
  os.system('pip install pytube')
  os.system('pip install art')

# function to get urls from list of playlists
def get_playlist(playlists):
  urls = []
  #iterate to get wtach links from playlists
  for playlist in playlists:
    playlist_urls = Playlist(playlist)

    for url in playlist_urls:
      urls.append()
      urls.append(url)

  return urls

 # load playlist json
# https://www.youtube.com/playlist?list=PLLbIkA4HJddeU5aDKd7cvLeJ_0I2UJULJ
import json

with open('playlists.json', 'r') as fl:
  data = json.load(fl)

# playlist array

pl_array = []

for url in data['playlist']:
  pl_array.append(url['url'])

# print(pl_array)

# playlist = ['https://www.youtube.com/playlist?list=PLLbIkA4HJddeU5aDKd7cvLeJ_0I2UJULJ','https://www.youtube.com/playlist?list=PLLbIkA4HJddd8NTDYoXs3_aSctFXGup3u']
pl_urls = get_playlist(pl_array)

with open('pl_urls.txt', 'w') as f:
  for url in pl_urls:
    f.write(url+'\n')

print("Endereços salvo com sucesso em " + os.getcwd())    