import os
import sys
import re

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')


def get_rules():
    rules = {}

    with open(filename, 'r') as f:
        for line in f:
            container, bags = line.strip('.').split('contain')
            contents = []
            
            if bag[4:] != 'no other bags.':
                for bag in bags.split(','):
                    combined_words = bag.strip().split(" ")
                    


def find_bags(my_bag, acceptable_bags):
    
    failed = 0
    counter = 0

    for rule in rules:
        rule = rule.strip('.').split('contain')
        container = rule[0].replace('bags', '').strip()
        bags = rule[1].split(',')
        for bag in bags:
            bag = bag[2:]
            bag = bag.strip('bags').strip('bag').strip()
            if bag == my_bag or bag in acceptable_bags:
                acceptable_bags.append(container)
            else: 
                failed += 1
        counter +=1 
    while failed != counter:
        find_bags(my_bag, acceptable_bags)
    else: 
        return len(acceptable_bags)
        
