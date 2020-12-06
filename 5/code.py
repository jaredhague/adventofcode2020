import os
import sys
import re
import math

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')
with open(filename, 'r') as f:
    lines = [line.strip() for line in f]
seat_ids = []
for line in lines:
    rows = [*range(0, 128, 1)]
    columns = [*range(0, 8, 1)]
    re_input = re.search('(.{7})(.{3})', line)
    row_string = re_input.group(1)
    column_string = re_input.group(2)
    for i in row_string:
        if i == 'F':
            max_len = len(rows) // 2
            rows = rows[:max_len]
        else:
            min_len= len(rows) // 2
            rows = rows[min_len:]

    for i in column_string:
        if i == 'L':
            max_len = len(columns) // 2
            columns = columns[:max_len]
        else:
            min_len= len(columns) // 2
            columns = columns[min_len:]

    seat_id = (int(rows[0]) * 8) + int(columns[0])
    seat_ids.append(seat_id)

print('Part 1: ' + str(max(seat_ids)))
seat_ids.sort()
num_of_seats = len(seat_ids) - 1
i = 0
while i < num_of_seats:
    o = i - 1
    result = seat_ids[i] - seat_ids[o]
    if result > 1:
        print('Part 2: ' + str(seat_ids[i] - 1))
    i+=1