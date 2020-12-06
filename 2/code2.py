import os 
import sys
import re

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')
passes = 0

with open(filename, 'r') as f:
    passwords = [line.strip() for line in f]

for password in passwords:
    first_second, char_key, input_string = password.split()
    first_pos, second_pos = first_second.split('-')
    input_string = ' ' + input_string
    char_key = char_key.strip(':')
    char_check = 0
    if char_key == input_string[int(first_pos)]:
        char_check += 1
    if char_key == input_string[int(second_pos)]:
        char_check += 1
    if char_check == 1:
        passes += 1
print(passes)