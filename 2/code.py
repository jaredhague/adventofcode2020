import os 
import sys
import re

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')
passes = 0

with open(filename, 'r') as f:
    passwords = [line.strip() for line in f]

for i in passwords:
    m = re.search('(\d+)-(\d+)[ ]([a-z]):[ ](.*)', i)

    lower_limit = int(m.group(1))
    upper_limit = int(m.group(2))
    policy_key = m.group(3)
    password = m.group(4)
    policy_count = password.count(policy_key)
    

    if policy_count >= lower_limit and policy_count <= upper_limit:
        passes +=1
        
    print(passes)