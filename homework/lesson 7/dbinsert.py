"""
Complete the insert_data function to insert the data into MongoDB.
"""

import json


def insert_data(data, db):
    collection = db.arachnid
    collection.insert_many(data)


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://qi-docker01.sqroot.local:27017")
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()
