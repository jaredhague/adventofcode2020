import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

with open(filename, 'r') as f:
    treeline = [line.strip() for line in f]

slope1 = 0
pos1 = 0
pos1_increase = 1
slope2 = 0
pos2 = 0 
pos2_increase = 3
slope3 = 0
pos3 = 0 
pos3_increase = 5
slope4 = 0
pos4 = 0 
pos4_increase = 7
slope5 = 0   
pos5 = 0 
pos5_increase = 1
counter = 1
trees = 0
tree = '#'

for i in treeline:
    
    if i[pos1] == tree:
        slope1 += 1
    pos1+=pos1_increase

    if i[pos2] == tree:
        slope2 += 1
    pos2+=pos2_increase

    if i[pos3] == tree:
        slope3 += 1
    pos3+=pos3_increase

    if i[pos4] == tree:
        slope4 += 1
    pos4+=pos4_increase

    counter += 1
    if counter == 2:
        if i[pos5] == tree:
            slope5 += 1
        counter = 0
        pos5+=pos5_increase
    
total = slope1 * slope2 * slope3 * slope4 * slope5
print('Answer Part 1:' + str(slope2))
print('Answer Part 2:' + str(total))
