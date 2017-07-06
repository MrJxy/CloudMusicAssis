from sys import argv
from spider import *
from db_connection import *

if __name__ == '__main__':
    script, user_id = argv[0], argv[1]
    favor = user_access(int(user_id))
    song_num = len(favor)
    recommend_table = dict()
    count = 0
    for song in favor:
        print("processing song " + str(count) + "/" + str(song_num) + "...")
        count += 1
        for unique_obj in db_find('CloudMusicAssis', 'InvertedIndex', {'song_id':song}):
            user_who_likes_list = unique_obj['user_id']
            for user in user_who_likes_list:
                if user in recommend_table:
                    recommend_table[user] += 1
                else:
                    recommend_table[user] = 1
    print("length of recommend_tbl: " + str(len(recommend_table)))
    print("sorting table...")
    recommend_list = list(recommend_table.items())
    top_count, top_index = 0, -1
    for i in range(5):
        for j in range(len(recommend_list)):
            if recommend_list[j][1] > top_count:
                top_count, top_index = recommend_list[j][1], j
        print(recommend_list[top_index])
        recommend_list[top_index] = (recommend_list[top_index][0], 0)
        top_count, top_index = 0, -1


