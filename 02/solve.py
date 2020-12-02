#!/bin/python3
import re


filename = 'input'

with open(filename) as f:
    content = f.readlines()


valid = 0
valid_p2 = 0

for c in content:
    # (policy, password) = c.split(':')
    # (p_range, p_letter) = policy.split()
    # (p_range_min, p_range_max) = p_range.split('-')
    # password = password.strip()
    # p_range_min = int(p_range_min)
    # p_range_max = int(p_range_max)


    matchObj = re.match( r'(\d+)-(\d+) (\w): (\w+)', c, re.I)
    if matchObj:
        p_range_min = int(matchObj.group(1))
        p_range_max = int(matchObj.group(2))
        p_letter = matchObj.group(3)
        password = matchObj.group(4)
    else:
        print("Failed to match regexp on: ", c)
        exit(-1)

    lc = password.count(p_letter)

    if p_range_min <= lc <= p_range_max:
        valid = valid + 1

    f1 = password[p_range_min - 1] == p_letter
    f2 = password[p_range_max - 1] == p_letter

    if f1 ^ f2:
        valid_p2 = valid_p2 + 1


print("Sol 1: ", valid)
print("Sol 2: ", valid_p2)
# Remove first # to make it a interactive cell
##%%

# %%
