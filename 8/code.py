import os
import sys

def get_data():
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'input.txt')
    with open(filename, 'r') as f:
        lines = [line.strip().split() for line in f]
    global data
    data = {}
    counter = 0

    for line in lines:
        counter += 1
        lst = []
        lst.append(line[0])
        lst.append(line[1])
        lst.append(0)
        data[counter]= lst

def accumulator():
    get_data()
    start = 1
    end = 2
    accum = 0
    while start < end:
        try:
            ins = data[start][0]
            value = data[start][1]
            visited = data[start][2]
            if visited < 1:
                data[start][2] += 1
                if ins == 'nop':
                    start += 1
                    end += 1
                if ins == 'acc':
                    accum = accum + int(value)
                    start += 1
                    end += 1
                if ins == 'jmp':
                    start = start + int(value)
                    end = end + int(value)
            else:
                print('Part 1:', accum)
                break
        except:
            print('Part 2:', accum)

def accumulator2():
   

    data_reverse = []
    for key in data:
        data_reverse.append(key)
    data_reverse.reverse()
    
    for i in data_reverse:
        get_data()
        print('org', data[i][0])
        if data[i][0] == 'nop':
            data[i][0] = 'jmp'
            print(data[i][0])
            start = 1
            end = 2
            accum = 0
            while start < end:
                try:
                    ins = data[start][0]
                    value = data[start][1]
                    visited = data[start][2]
                    if visited < 1:
                        data[start][2] += 1
                        if ins == 'nop':
                            start += 1
                            end += 1
                        if ins == 'acc':
                            accum = accum + int(value)
                            start += 1
                            end += 1
                        if ins == 'jmp':
                            start = start + int(value)
                            end = end + int(value)
                    else:
                       
                        break
                except:
                    print('Part 2:', accum)
        if data[i][0] == 'jmp':
            data[i][0] = 'nop'
            print('updated',data[i][0])
            start = 1
            end = 2
            accum = 0
            while start < end:
                try:
                    ins = data[start][0]
                    value = data[start][1]
                    visited = data[start][2]
                    if visited < 1:
                        data[start][2] += 1
                        if ins == 'nop':
                            start += 1
                            end += 1
                        if ins == 'acc':
                            accum = accum + int(value)
                            start += 1
                            end += 1
                        if ins == 'jmp':
                            start = start + int(value)
                            end = end + int(value)
                    else:
                       
                        break
                except:
                    print('Part 2:', accum)
        

accumulator()
accumulator2()


