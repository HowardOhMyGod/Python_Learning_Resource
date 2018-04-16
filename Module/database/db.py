from pymongo import MongoClient
import os


class MongoDB:
    def __init__(self):
        pass

    def connect(self, db_name):
        client = MongoClient(os.environ['local_db'])
        db = client[db_name]

        return db

mongoDB = MongoDB()
