#!/bin/python3

# %%
import re


filename = 'input'

with open(filename) as f:
    content = f.readlines()

area = []

for l in content:
    area.append(([x for x in l.strip()]))

# %%

def runSlope(area, inc_x, inc_y):
    pos_x = 0
    pos_y = 0

    tree_hits = 0

    while(pos_y < len(area)):
        if area[pos_y][pos_x] == '#':
            tree_hits = tree_hits + 1

        # print( f"{pos_x}, {pos_y} -> {area[pos_y][pos_x]} : {tree_hits}")

        pos_x = (pos_x + inc_x) % len(area[0])
        pos_y = pos_y + inc_y

    return tree_hits

# %%
print("Sol 1: ", runSlope(area, 3, 1))

# %%
print("Sol 2: ", runSlope(area, 1, 1)*runSlope(area, 3, 1)*runSlope(area, 5, 1)*runSlope(area, 7, 1)*runSlope(area, 1, 2))

