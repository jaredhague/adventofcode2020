import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
playfield = os.path.join(here, 'playfield.txt')


line = '.#..........#...#...#..#.......'

counter = 0
while counter < 11:
    line = line + line
    print(line)
    counter+=1