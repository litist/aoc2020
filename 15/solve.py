#!/bin/python3

# %%
import re
import numpy as np

content = [11,18,0,20,1,7,16]

turn = 1
history = {}

# init this 0
history[0] = (0,0)

last = 0
for i in content:
    history[i] = (1,turn)
    turn = turn + 1
    last = i

print(history)

for t in range(turn, 30000000+1):
    hl = history[last]
    if hl[0] == 1:
        s = history[0]
        history[0] = (s[0] + 1, t, s[1])
        last = 0
    else:
        last = hl[1] - hl[2]
        if last in history.keys():
            hd = history[last]
            history[last] = (hd[0] + 1, t, hd[1])
        else:
            history[last] = (1, t)

    #print(f"t: {t} -> {last} | {history}")
    #print(last)
    if t % 1000000 == 0:
        print(t)

    if t == 3001:
        print("Solution 1: ", last)


#print(history)

print("Solution 2: ", last)
