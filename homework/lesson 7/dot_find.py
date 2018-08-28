#!/usr/bin/env python
"""
Your task is to write a query that will return all cars with width dimension
greater than 2.5. Please modify only the 'dot_query' function, as only that
will be taken into account.
"""


def dot_query():
    query = {"dimensions.width": {"$gt": 2.5}}
    return query


def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


if __name__ == "__main__":
    db = get_db()
    query = dot_query()
    cars = db.cars.find(query)

    print "Printing first 3 results\n"
    import pprint
    for car in cars[:3]:
        pprint.pprint(car)
