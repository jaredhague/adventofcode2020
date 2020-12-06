import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

with open(filename, 'r') as f:
        treeline = [line.strip() for line in f]

pos = 3
index = 0
counter = 0
trees = 0
for line in treeline:
    if index > (len(line) - 1):
        index = index - (len(line) - 1)
    print(line[index], index)
    if line[index == '#']:
        trees +=1
    index = index + pos 
    counter += 1
print(trees)