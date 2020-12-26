#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()

rules = ['']*len(content)
for i in range(0, len(content)):
    if content[i].strip() == '':
        break

    #print(content[i])

    (id, rule) = content[i].strip().split(':')
    #print(id, rule, len(rule))

    r = rule.strip().split('|')

    #print("r", r)

    if r[0] == '"a"' or r[0] == '"b"':
        rules[int(id)] = ('leaf', r[0][1])
    else:
        if len(r) == 1:
            rules[int(id)] = ('line', [int(j) for j in r[0].strip().split(' ')])
        elif len(r) == 2:
            rules[int(id)] = ('or', [int(j) for j in r[0].strip().split(' ')], [int(i) for i in r[1].strip().split(' ')])
        else:
            print("ERROR")


# todo: resize the list
messages = []
for i in range(i+1, len(content)):
    #print(content[i])
    messages.append(content[i].strip())

# %%
def check(rule_id, m_pos , m):
    #m = messages[0]
    r = rules[rule_id]
    pos = m_pos

    if m_pos >= len(m):
        return (False, m_pos)



    if r[0] == 'leaf':
        if m[pos] == r[1]:
            return (True, pos + 1)
        else:
            return (False, pos + 1)
    elif r[0] == 'line':
        for r_id in r[1]:
            (res, pos_next) = check(r_id, pos, m)
            if not res:
                return (False, pos_next)
            else:
                pos = pos_next
        else:
            return (True, pos)
    elif r[0] == 'or':
        # check first line
        pos_ = pos
        valid = True
        for r_id in r[1]:
            (res, pos_next) = check(r_id, pos, m)
            if not res:
                valid = False
                break
            else:
                pos = pos_next

        if valid:
            return (True, pos)

        # check second line
        pos = pos_
        valid = True
        for r_id in r[2]:
            (res, pos_next) = check(r_id, pos, m)
            if not res:
                valid = False
                break
            else:
                pos = pos_next

        if valid:
            return (True, pos)
        else:
            return (False, pos)


valid_m = 0
for m in messages:
    (res, l) = check(0, 0, m)
    if res and l == len(m):
#        print(f"messages {m} is okay")
        valid_m = valid_m + 1

print("Solution 1: ", valid_m)


# %% part 2

# patch the rules
# 8: 42 | 42 8
#rules[8] = ('or', [42], [42, 8])
#11: 42 31 | 42 11 31
#rules[11] = ('or', [42, 31], [42, 11, 31])

# The patched rules are only used within rule #0 and applying
# them yield to following regexp style for rule 0: 42+ 42{n} 31{n}


def check_p2(rule_id, pos, m):

    # find max multiple matches for internal rule which is 42
    (res, pos_next) = check(42, pos, m)
    #print(f"1st r42: {res} and {pos}->{pos_next}")
    if not res:
        return (False, 0)
    last_res = res
    last_pos = pos_next
    pos = pos_next
    n_r42 = 0
    while(res):
        last_pos = pos
        n_r42 = n_r42 + 1
        (res, pos) = check(42, pos, m)
        #print(f"1st r42: {res} and {last_pos}->{pos}")
    
    res = True
    pos = last_pos
    n_r31 = -1
    while(res):
        last_pos = pos
        n_r31 = n_r31 + 1
        (res, pos) = check(31, pos, m)
        #print(f"1st r31: {res} and {last_pos}->{pos}")

    #print(f"r42: {n_r42} r31: {n_r31} and {last_pos}=={len(m)}")

    if n_r42 > n_r31 > 0 and last_pos == len(m):
        return (True, last_pos)
    else:
        return (False, 0)



valid_m = 0
#for m in [messages[0]]:
for m in messages:
    (res, l) = check_p2(0, 0, m)
    if res and l == len(m):
        #print(f"messages {m} is okay")
        valid_m = valid_m + 1

print("Solution 2: ", valid_m)
