import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

with open(filename, 'r') as f:
        treeline = [line.strip() for line in f]

def count_trees(pos, down):
    row_count = 1
    trees = 0
    for i in treeline:
        if pos > (len(i) - 1):
            pos = pos - (len(i) - 1)
        if down % row_count == 0:
            print(i[pos])
            if i[pos] == '#':
                trees +=1
        pos = pos + pos
        row_count +=1
    return trees

print(count_trees(3, 1))