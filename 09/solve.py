#!/bin/python3

# %%
import re

filename = 'input'

with open(filename) as f:
    content = f.readlines()

data = []

for c in content:
    data.append(int(c.strip()))


# %%
N_preamble = 25


def isValid(l, i):

    for ai in range(0, len(l)):
        for bi in range(0, len(l)):
            if ai == bi:
                continue
            
            if l[ai] + l[bi] == i:
                return True
    
    return False


pos = N_preamble
# check if data is valid
sol1 = -1
while pos < len(data):

    if isValid(data[pos-N_preamble:pos], data[pos]) == False:
        print("Encoding failed on ", pos, data[pos])
        sol1 = data[pos]
        break

    pos = pos + 1

print("Solution 1: ", sol1)

# %% second part
s_pos = 0
e_pos = 1
s = data[s_pos] + data[e_pos]

while s != sol1:

    if s < sol1:
        e_pos = e_pos + 1
        s = s + data[e_pos]
    elif s > sol1:
        s = s - data[s_pos]
        s_pos = s_pos + 1
    else:
        print("ERROR")

print("sum found with ", s_pos, e_pos, sum(data[s_pos:e_pos+1]), min(data[s_pos:e_pos+1]), max(data[s_pos:e_pos+1]))
sol2 = min(data[s_pos:e_pos+1]) + max(data[s_pos:e_pos+1])
print("Solution 2: ", sol2)
