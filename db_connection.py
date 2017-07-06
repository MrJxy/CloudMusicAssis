from pymongo import MongoClient
from pymongo import errors

CLIENT = MongoClient('localhost', 27017)

def db_insert(db_name, collection_name, item):
    if item == {}: return
    db = CLIENT[db_name]
    collection = db[collection_name]
    try:
        collection.insert(item)
    except errors.DuplicateKeyError:
        pass

def db_find(db_name, collection_name, to_find = None, skip = -1, limit = -1):
    db = CLIENT[db_name]
    collection = db[collection_name]
    if to_find == None:
        if (skip == -1 and limit == -1):
            return collection.find()
        elif (skip == -1 and limit >= 0):
            return collection.find().limit(limit)
        elif (skip >= 0 and limit == -1):
            return collection.find().skip(skip)
        else:
            return collection.find().skip(skip).limit(limit)
    else:
        if (skip == -1 and limit == -1):
            return collection.find(to_find)
        elif (skip == -1 and limit >= 0):
            return collection.find(to_find).limit(limit)
        elif (skip >= 0 and limit == -1):
            return collection.find(to_find).skip(skip)
        else:
            return collection.find(to_find).skip(skip).limit(limit)

if __name__ == '__main__':
    db_insert('CloudMusicAssis', 'Favourite', {'user_id':60000009, 'song_id':[100,300]})
    db_insert('CloudMusicAssis', 'Favourite', {'user_id':60000009, 'song_id': [100, 400]})