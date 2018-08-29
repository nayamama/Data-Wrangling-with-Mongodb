#!/usr/bin/env python
"""
Use an aggregation query to answer the following question.

What we are asking here is that you first calculate the average city population
for each region in a country and then calculate the average of all the regional
averages for a country.

  As a hint, _id fields in group stages need not be single values. They can
also be compound keys (documents composed of multiple fields). You will use the
same aggregation operator in more than one stage in writing this aggregation
query. I encourage you to write it one stage at a time and test after writing
each stage.
"""


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$unwind": "$isPartOf"},
                {"$group": {
                    "_id": {"region": "$isPartOf", "country": "$country"},
                    "avg_region": {"$avg": "$population"}
                }},
                {"$project": {
                    "country": "$_id.country",
                    "region": "$_id.region",
                    "avg_region": 1
                }},
                {"$group": {
                    "_id": "$country",
                    "avgRegionalPopulation": {"$avg": "$avg_region"}
                }}]
    return pipeline


def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint

    if len(result) < 150:
        pprint.pprint(result)
    else:
        pprint.pprint(result[:100])
    key_pop = 0
    for country in result:
        if country["_id"] == 'Lithuania':
            assert country["_id"] == 'Lithuania'
            assert abs(country["avgRegionalPopulation"] - 14750.784447977203) < 1e-10
            key_pop = country["avgRegionalPopulation"]
    assert {'_id': 'Lithuania', 'avgRegionalPopulation': key_pop} in result
