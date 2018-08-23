"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

If you look at the full city data, you will notice that there are couple of
values that seem to provide the same information in different formats: "point"
seems to be the combination of "wgs84_pos#lat" and "wgs84_pos#long". However,
we do not know if that is the case and should check if they are equivalent.

Finish the function check_loc(). It will recieve 3 strings: first, the combined
value of "point" followed by the separate "wgs84_pos#" values. You have to
extract the lat and long values from the "point" argument and compare them to
the "wgs84_pos# values, returning True or False.

Note that you do not have to fix the values, only determine if they are
consistent. To fix them in this case you would need more information. Feel free
to discuss possible strategies for fixing this on the discussion forum.

The rest of the code is just an example on how this function can be used.
Changes to "process_file" function will not be taken into account for grading.
"""
import csv
import pprint

CITIES = 'cities.csv'


def check_loc(point, lat, longi):
    if point.startswith('{'):
        s1 = point.replace('{', "").replace('}', "").split('|')
        lat1 = s1[0].split(" ")[0]
        long1 = s1[0].split(" ")[1]
        lat2 = s1[1].split(" ")[0]
        long2 = s1[1].split(" ")[1]
        if lat.startswith('{'):
            s2 = lat.replace('{', "").replace('}', "").split('|')
            lat_1 = s2[0]
            lat_2 = s2[1]
        else:
            lat_1 = lat_2 = lat
        if longi.startswith('{'):
            s3 = longi.replace('{', "").replace('}', "").split('|')
            long_1 = s3[0]
            long_2 = s3[1]
        else:
            long_1 = long_2 = longi
        return lat1 == lat_1 and lat2 == lat_2 and long1 == long_1 and long2 == long_2
    else:
        p = point.split(" ")
        return p[0] == lat and p[1] == longi


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        for i in range(3):
            l = reader.next()

        for line in reader:
            # calling your function to check the location
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
                print "{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"],
                                               line["wgs84_pos#long"])
            data.append(line)

    return data


def test():
    assert check_loc("33.08 75.28", "33.08", "75.28") == True
    assert check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183") == False
    assert check_loc("{23.0 80.12|23.48 80.12}", "{23.0|23.48}", "80.12") == True
    assert check_loc("{29.448055555555555 77.31027777777778|29.45 77.32}", "{29.4481|29.45}", "{77.3103|77.32}") == False
    assert check_loc("{23.78 72.63|23.785 72.64}", "{23.78|23.785}", "{72.63|72.64}") == True
    print "success..."


if __name__ == "__main__":
    test()