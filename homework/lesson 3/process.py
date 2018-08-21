"""
Let's assume that you combined the code from the previous 2 exercises with code
from the lesson on how to build requests, and downloaded all the data locally.
The files are in a directory "data", named after the carrier and airport:
'placeholder-placeholder.html'.format(carrier, airport), for example "FL-ATL.html".

The table with flight info has a table class="dataTDRight". Your task is to
use 'process_file()' to extract the flight data from that table as a list of
dictionaries, each dictionary containing relevant data from the file and table
row. This is an example of the data structure you should return:

data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}
]

Note - year, month, and the flight data should be integers.
You should skip the rows that contain the TOTAL data for a year.

There are couple of helper functions to deal with the data files.
Please do not change them for grading purposes.
All your changes should be in the 'process_file()' function.

The 'data/FL-ATL.html' file in the tab above is only a part of the full data,
covering data through 2003. The test() code will be run on the full table, but
the given file should provide an example of what you will get.
"""

from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    return:

    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]


    Note - year, month, and the flight data should be integers.
    You should skip the rows that contain the TOTAL data for a year.
    """
    data = []

    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list
    # will be a reference to the same info dictionary.
    # with open("{}\{}".format(datadir, f), "r") as html:
    with open("data\FL-ATL.html", "r") as html:
        soup = BeautifulSoup(html)
        rows = soup.find(id="DataGrid1").find_all("tr")

        for row in rows[1:]:
            info = dict()
            info["courier"], info["airport"] = f[:6].split("-")
            cells = row.find_all("td")
            if cells[1].get_text() != "\nTOTAL":
                info["year"] = int(cells[0].get_text())
                info["month"] = int(cells[1].get_text())
                tmp = dict()
                tmp["domestic"] = int(cells[2].get_text().replace(',', ''))
                tmp["international"] = int(cells[3].get_text().replace(',', ''))
                info["flights"] = tmp
                data.append(info)
    return data


def test():
    print "Running a simple test..."
    files = process_all(datadir)
    data = []
    # Test will loop over three data files.
    for f in files:
        data += process_file(f)
    print data[-1]
    #assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    assert data[-1]["airport"] == "ATL"
    #assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}

    print "... success!"


if __name__ == "__main__":
    test()