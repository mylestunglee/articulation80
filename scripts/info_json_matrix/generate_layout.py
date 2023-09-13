import sys
import re

entry = '{{"matrix": [{2}, {3}], "x": {0}, "y": {1}}},'
filename = sys.argv[1]
with open(filename) as file:
    layout_csv = file.read()

row_csv, col_csv = filter(None, re.split(',+\n', layout_csv))

for y, (row_line, col_line) in enumerate(zip(row_csv.splitlines(), col_csv.splitlines())):
    for x, (row, col) in enumerate(zip(row_line.split(','), col_line.split(','))):
        if row and col:
            print(entry.format(x, y, row, col))
