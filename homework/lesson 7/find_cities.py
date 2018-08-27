#!/usr/bin/env python
"""
Your task is to write a query that will return all cities
that are founded in 21st century.
Please modify only 'range_query' function, as only that will be taken into account.
The date format is -- 'foundingDate': datetime.datetime(2000, 7, 1, 0, 0)

"""

from datetime import datetime
from pymongo import MongoClient
import pprint


def range_query():
    min_date = datetime(2000, 12, 31, 0, 0)  # <- last day of 2000
    query = {"foundingDate": {"$gt": min_date}}
    return query


def get_db():
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


if __name__ == "__main__":
    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print "Found cities:", cities.count()
    pprint.pprint(cities[0])

