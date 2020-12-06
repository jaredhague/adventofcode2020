import os
import sys
import re
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

value = 'amd'

if value in valid_ecl:
    print('ok')
else:
    print('not ok')