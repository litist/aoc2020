#!/bin/python3

# %%
import re
import numpy as np

# %% PART I
input = '389125467' #testinput
input = '326519478'

N = len(input) + 0
cups_ = [0]*(N+1) # +1 index offset


for i in range(len(input)-1):
    print(i)
    cups_[int(input[i])] = int(input[i + 1])

last = int(input[-1])
for ii in range(len(input) + 1, N + 1):
    # print(f"ii: {ii} {last} -> {ii} and last becomes: {ii}")
    cups_[last] = (ii)
    last = ii

# last item
cups_[last] = int(input[0])

cup_max = max(cups_)

# %%
def step(cups, current_cup):
    #current_id = cups.index(current_cup)

    picked_cups = []
    picked_cups.append( cups[current_cup] )
    for i in range(2):
        #print("remove item on idx", (cups.index(current_cup) + 1) % len(cups))
        picked_cups.append( cups[picked_cups[-1]] )


    dest_cup = current
    # get dest cup
    while dest_cup in picked_cups or dest_cup == current:
        dest_cup = dest_cup - 1
        if dest_cup <= 0:
            dest_cup = cup_max

    cups[current_cup] = cups[picked_cups[-1]]

    cups[picked_cups[-1]] = cups[dest_cup]
    cups[dest_cup] = picked_cups[0]


    return cups[current_cup]

cups = cups_.copy()
current = int(input[0])

for l in range(100):
    current = step(cups, current)

# %%
c = 1
s = ""
while(cups[c] != 1):
    s = s + f"{cups[c]}"
    c = cups[c]

print("Solution 1: ", s)

# %% Part II

N = 1000000
cups_ = [0]*(N+1) # +1 index offset

for i in range(len(input)-1):
    print(i)
    cups_[int(input[i])] = int(input[i + 1])

last = int(input[-1])
for ii in range(len(input) + 1, N + 1):
    # print(f"ii: {ii} {last} -> {ii} and last becomes: {ii}")
    cups_[last] = (ii)
    last = ii

# last item
cups_[last] = int(input[0])

cup_max = max(cups_)

cups = cups_.copy()
current = int(input[0])

for l in range(10000000):
    current = step(cups, current)


print("Solution 2: ", cups[1] * cups[cups[1]])
