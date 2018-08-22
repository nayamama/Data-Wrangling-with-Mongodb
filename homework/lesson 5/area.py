"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import csv
import json
import pprint

CITIES = 'cities.csv'


def is_significant(nums):
    if '.' in nums[0] and '.' in nums[1]:
        first = nums[0].split('.')[1]
        second = nums[1].split('.')[1]
        if len(first) >= len(second):
            return nums[0]
        else:
            return nums[1]
    elif '.' not in nums[0] and '.' in nums[1]:
        return nums[1]
    elif '.' in nums[0] and '.' not in nums[1]:
        return nums[0]


def fix_area(area):

    if area == "NULL":
        return None
    elif area.startswith('{'):
        # print area
        nums = area.replace('{', "").replace('}', "").split('|')
        return float(is_significant(nums))
    else:
        return float(area)


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        # skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5, 8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] is None
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0


if __name__ == "__main__":
    test()  # <- the test does not provide correct number, mu code passed the online check
