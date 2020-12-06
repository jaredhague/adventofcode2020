
questions = ['t', 'b', 'e', 'i', 'z', 'd', 'p', 'h', 'y', 's', 'f', 'x', 'w', 'r', 'l', 'a', 'o', 'k', 'u', 'q', 'y', 'w', 'z', 'a', 'q', 's', 'p', 'r', 'u', 'k', 'd', 't', 'b', 'h', 'e', 'o', 'x', 'i', 'l', 'r', 'v', 'k', 'i', 'e', 'o', 'd', 'h', 't', 'q', 's', 'u', 'p', 'y', 'w', 'x', 'c', 'a', 'z', 'l', 'h', 's', 'd', 'i', 'w', 'z', 'e', 'q', 'o', 'r', 'y', 'u', 'l', 'p', 'k', 't', 'a', 'x', 'a', 'x', 'o', 'q', 'u', 'l', 'r', 'i', 'g', 't', 'n', 'w']

answers_dict = {}

for answer in questions:
    if answer in questions:
        if answer in answers_dict:
            answer_num = answers_dict[answer] + 1
            answers_dict[answer] = answer_num
            print(answers_dict)
        else:
            answers_dict[answer] = 1
            print(answers_dict)

print(questions.count('t'),questions.count('b'),questions.count('e'),questions.count('i') )