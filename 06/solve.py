#!/bin/python3

# %%
import re

filename = 'input'

with open(filename) as f:
    content = f.readlines()

content.append('\n')


#%%
sol1 = 0
g = {}

for l in content:

    if l == '\n':
        # add group count to all count
        print(g, len(g))
        sol1 = sol1 + len(g)
        g = {}

    else:
        print(l)
        for c in l.strip():
            g[c] = 1

print("Solution 1: ", sol1)

# %%
sol2 = 0

g = [True] * 26

for l in content:

    if l == '\n':
        # add group count to all count

        for c in range(0, len(g)):
            if g[c] == True:
                sol2 = sol2 + 1
            # reset 
            g[c] = True

    else:
        print(l)
        for c in range(0, len(g)):
            if chr(ord('a') + c) in l:
                g[c] = g[c] and True
            else:
                g[c] = False

print("Solution 2: ", sol2)

# %%
