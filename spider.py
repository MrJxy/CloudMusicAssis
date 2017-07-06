import requests
import json
import time

from sys import argv
from db_connection import *

def user_access(user_id):
    user_id = str(user_id).zfill(8)
    user_url = "http://music.163.com/api/user/playlist/?offset=0&limit=1&uid=" + str(user_id)
    response = requests.get(user_url)
    user_json = json.loads(response.text)
    if len(user_json['playlist']) == 0 or user_json['playlist'][0]['creator'] == None:
        return None
    playlist_id = user_json['playlist'][0]['id']
    playlist_url = "http://music.163.com/api/playlist/detail?updateTime=-1&id=" + str(playlist_id)
    response = requests.get(playlist_url)
    playlist_json = json.loads(response.text)
    tracks = []
    for song in playlist_json['result']['tracks']:
        tracks.append(song['id'])
    return tracks



if __name__ == '__main__':
    script, start_num, end_num = argv[0], int(argv[1]), int(argv[2])
    i = 0
    while True:
        try:
            for i in range(start_num, end_num + 1):
                favor = user_access(i)
                if favor == None:
                    print("id: ", i, " not exists.")
                else:
                    print("id: ", i, ": ", len(favor))
                    if len(favor) > 20 and len(favor) < 1000:
                        db_insert('CloudMusicAssis', 'Favourite', {
                            'user_id': i,
                            'song_id': favor
                        })
            if i == end_num: break
        except TimeoutError:
            start_num = i
            continue



'''
spider2: 10677783
spider3: 20219938
spider4: 30292557
spider5: 40254952
spider6: 50209211
spider7: 60040678
spider8: 70037987
spider9: 80038247
spider10: 90027948
spider11: 100012508
'''