import os
import sys
import re

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

capturelines = open(filename, 'r').read().split("\n\n")
valid_key_criteria = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

min_byr = 1920
max_byr = 2002
min_iyr = 2010
max_iyr = 2020
min_eyr = 2020
max_eyr = 2030
min_hgt_cm = 150
max_hgt_cm = 193
min_hgt_in = 59
max_hgt_in = 76
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
pid_digits = 9
hcl_digits = 6

#validate against criteria
p1valid = 0
p2valid = 0
for line in capturelines:
    line = line.replace("\n", " ")
    key_criteria = 0
    value_criteria = 0
    for item in line.split():
        key,value = item.split(":")
        if key in valid_key_criteria:
            key_criteria += 1
        
        if key == 'byr' and int(value) >= min_byr and int(value) <= max_byr:
            value_criteria +=1
        if key == 'iyr' and int(value) >= min_iyr and int(value) <= max_iyr:
            value_criteria +=1
        if key == 'eyr' and int(value) >= min_eyr and int(value) <= max_eyr:
            value_criteria +=1
        if key == 'hgt' and re.search('(cm)', value):
            value_cm = int(value.split('cm')[0])
            if value_cm >= min_hgt_cm and value_cm <= max_hgt_cm:
                value_criteria +=1
        if key == 'hgt' and re.search('(in)', value):
            value_in = int(value.split('in')[0])
            if value_in >= min_hgt_in and value_in <= max_hgt_in:
                value_criteria += 1
        if key == 'ecl' and value in valid_ecl:
            value_criteria += 1
        if key == 'pid' and value.isnumeric() and len(value) == pid_digits:
            value_criteria += 1
        if key == 'hcl' and re.search('^#[a-f,0-9]{6}$', value):
            value_criteria += 1
            
    if key_criteria == 7:
        p1valid +=1
    if key_criteria == 7 and value_criteria == 7:
        p2valid +=1

print('Part 1: ' + str(p1valid))
print('Part 2: ' + str(p2valid))

