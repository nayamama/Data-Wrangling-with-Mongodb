"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!
"""
import xml.etree.cElementTree as ET
import pprint


def get_user(element):
    if element.get("uid"):
        return element.get("uid")


def process_map(filename):
    """ return a set of unique user IDs ("uid") """
    users = set()
    for _, element in ET.iterparse(filename):
        if get_user(element):
            users.add(get_user(element))

    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6


if __name__ == "__main__":
    test()