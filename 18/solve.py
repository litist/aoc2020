#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()

# 1 + (2 * 3) + (4 * (5 + 6))

def bracket(data, i_pos):
    res = 0
    op = '?'
    
    # skip spaces
#    while(data[i_pos] == ' '):
#        i_pos = i_pos + 1
    
    # get first digit
#    res = int(data[i_pos])
#    i_pos = i_pos + 1

    while data[i_pos] != ')':

        if data[i_pos] == ' ':
            i_pos = i_pos + 1
            continue


        #print(f"i_pos {i_pos} res {res} op {op}")

        if data[i_pos] == ' ':
            i_pos = i_pos + 1
        elif data[i_pos] == '+':
            #print('plus')
            op = '+'
            i_pos = i_pos + 1
            #x = x + calc(data, i_pos + 1)
        elif data[i_pos] == '*':
            #print('mult')
            op = '*'
            i_pos = i_pos + 1
            #x = x * calc(data, i_pos + 1)
        elif data[i_pos] == '(':
            #print("going deeper")
            [val, next_pos] = bracket(data, i_pos + 1)
            #print("rerurned", val, next_pos)
            #print(f"after return DO operation {op} on {val} and {res}")
            if op == '+':
                res = res + val
            elif op == '*':
                res = res * val
            elif op == '?':
                res = val
            else:
                print("Unknown operation: ", op)#data[i_pos])
            i_pos = next_pos
        elif data[i_pos] == ')':
            #print("Closing bracket ")
            return (res, i_pos + 1)
        else:
            # make operation
            #print(f"DO operation {op} on {data[i_pos]} and {res}")
            if op == '+':
                res = res + int(data[i_pos])
            elif op == '*':
                res = res * int(data[i_pos])
            elif op == '?':
                res = int(data[i_pos])
            else:
                print("Unknown operation: ", op)#data[i_pos])
            i_pos = i_pos + 1

    #print(f"Loop end ({res}, {i_pos+1})")

    return (res, i_pos + 1)


s = 0
for l in content:
    # print(l)

    [a,b]= bracket( l.strip() + ')', 0)
    #print(l, a, b)
    s = s + a
    
print("Solution 1", s)






# %% part 2
def bracket(data, i_pos):
    res = 0
    op = '?'

    # store a first operand of a multiplication
    hold_val = -1

    while data[i_pos] != ')':

        #print(f"i_pos {i_pos}->{data[i_pos]} res {res} op {op} hold_val {hold_val}")

        if data[i_pos] == ' ':
            i_pos = i_pos + 1
        elif data[i_pos] == '+':
            #print('plus')
            op = '+'
            i_pos = i_pos + 1
            #x = x + calc(data, i_pos + 1)
        elif data[i_pos] == '*':
            #print('mult')
            op = '*'
            i_pos = i_pos + 1

            #x = x * calc(data, i_pos + 1)
        elif data[i_pos] == '(':
            #print("going deeper")
            [val, next_pos] = bracket(data, i_pos + 1)
            #print("rerurned", val, next_pos)
            #print(f"after return DO operation {op} on {val} and {res}")
            if op == '+':
                res = res + val
            elif op == '*':
                if hold_val == -1:
                    hold_val = res
                    res = val
                else:
                    hold_val = res * hold_val
                    res = val
            elif op == '?':
                res = val
            else:
                print("Unknown operation: ", op)#data[i_pos])
            i_pos = next_pos
        else:
            # make operation
            #print(f"DO operation {op} on {data[i_pos]} and {res}")
            if op == '+':
                #print(f"DO operation {op} on {data[i_pos]} and {res} | hold_val: {hold_val}")
                res = res + int(data[i_pos])
            elif op == '*':
                if hold_val == -1:
                    hold_val = res
                    res = int(data[i_pos])
                else:
                    hold_val = res * hold_val
                    res = int(data[i_pos])
            elif op == '?':
                res = int(data[i_pos])
            else:
                print("Unknown operation: ", op)#data[i_pos])
            i_pos = i_pos + 1

    #print(f"Loop end ({res}, {i_pos+1})")
    if hold_val != -1:
        res = res * hold_val
    

    return (res, i_pos + 1)


s = 0
for l in content:
    # print(l)

    [a,b]= bracket( l.strip() + ')', 0)
    #print(l, a, b)
    s = s + a
    
print("Solution 2: ", s)
# %%
