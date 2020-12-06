import os
import sys


here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')
answers = open(filename, 'r').read().split("\n\n")

total1 = 0
group_total = 0
for line in answers:
    positives = 0
    questions = []
    answers_dict = {}
    group_num = line.count("\n") + 1
    group_yes = 0
    line = line.replace("\n", "")
    for answer in line:
        if answer in answers_dict:
            answer_num = answers_dict[answer] + 1
            answers_dict[answer] = answer_num
        else:
            answers_dict[answer] = 1
        questions.append(answer)
    for key, value in answers_dict.items():
        if value == group_num:
            group_yes += 1
    questions = set(questions)
    total1 += len(questions)
    group_total += group_yes
print('Part 1: ' + str(total1))
print('Part 2: ' + str(group_total))