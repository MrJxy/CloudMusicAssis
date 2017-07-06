from db_connection import *

def inverted_index(db_name, src_collection, tgt_collection):
    index_table = dict()
    print('reading db...')
    for u in db_find(db_name, src_collection):
        for song in u['song_id']:
            if song not in index_table:
                index_table[song] = list()
            index_table[song].append(u['user_id'])
    print('writing db...')
    for (k, v) in index_table.items():
        db_insert(db_name, tgt_collection, {
            'song_id': k,
            'user_id': v
        })


if __name__ == '__main__':
    inverted_index('CloudMusicAssis', 'Favourite', 'InvertedIndex')