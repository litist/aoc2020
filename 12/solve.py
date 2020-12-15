#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()


def rot(x, a):
    theta = np.radians(a)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c)))
    return np.matmul(R, x)

v = np.array([1, 0])
p = np.array([0, 0])



#%% part 2

v = np.array([10, 1])

for c in content:
    matchObj = re.match( r'^([NSEWLRF])(\d+)?', c.strip())
    if not matchObj:
        print("ERRROR: ", c.strip())
        break

    action = matchObj.group(1)
    value = int(matchObj.group(2))

    if action == 'N':
        v = v + np.array([0, value])
    elif action == 'S':
        v = v + np.array([0, -1*value])
    elif action == 'E':
        v = v + np.array([value, 0])
    elif action == 'W':
        v = v + np.array([-1*value, 0])
    elif action == 'F':
        p = p + v*value
    elif action == 'L':
        v = rot(v, value)
    elif action == 'R':
        v = rot(v, -1*value)
    else:
        print("ERRROR")
        break

print("Solution 2: ", (np.abs(p[0]) + np.abs(p[1])))




#%% part 1
v = np.array([1, 0])
p = np.array([0, 0])

for c in content:
    matchObj = re.match( r'^([NSEWLRF])(\d+)?', c.strip())
    if not matchObj:
        print("ERRROR: ", c.strip())
        break

    action = matchObj.group(1)
    value = int(matchObj.group(2))

    if action == 'N':
        p = p + np.array([0, value])
    elif action == 'S':
        p = p + np.array([0, -1*value])
    elif action == 'E':
        p = p + np.array([value, 0])
    elif action == 'W':
        p = p + np.array([-1*value, 0])
    elif action == 'F':
        p = p + v*value
    elif action == 'L':
        v = rot(v, value)
    elif action == 'R':
        v = rot(v, -1*value)
    else:
        print("ERRROR")
        break

print("Solution 1: ", np.abs(p[0]) + np.abs(p[1]))


# %%
