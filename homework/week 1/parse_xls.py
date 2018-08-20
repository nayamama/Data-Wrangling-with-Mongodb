import xlrd

from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    # get the data
    # sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    # other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)

    values = []
    for r in range(1, sheet.nrows):
        values.append((sheet.cell_value(r, 0), sheet.cell_value(r, 1)))

    max_pair = max(values, key=lambda x: x[1])
    min_pair = min(values, key=lambda x: x[1])
    mu = 1.0 * sum(sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows)) / (sheet.nrows - 1)

    data = {
        'maxtime': xlrd.xldate_as_tuple(max_pair[0], 0),
        'maxvalue': max_pair[1],
        'mintime': xlrd.xldate_as_tuple(min_pair[0], 0),
        'minvalue': min_pair[1],
        'avgcoast': mu
    }
    return data


if __name__ == '__main__':
    print parse_file(datafile)
