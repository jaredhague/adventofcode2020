import os
import sys

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'list.txt')

with open(filename, 'r') as f:
    numbers = [line.strip() for line in f]

for i in numbers:
    for x in numbers:
        for y in numbers:
            if int(i) + int(x) + int(y) == 2020:
                answer = int(i) * int(x) * int(y)
                print(answer)