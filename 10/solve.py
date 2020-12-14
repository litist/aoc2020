#!/bin/python3

# %%
import re

filename = 'input'

with open(filename) as f:
    content = f.readlines()

jolts= []

for c in content:
    jolts.append(int(c.strip()))


# %%
last = 0
diffs = [0,0,0, 1] # 3jolt differece to adapter
for j in sorted(jolts):
    d = j - last
    last = j
    diffs[d] = diffs[d] + 1


print("Solution 1:", diffs[1] * diffs[3])
# %% get max number of consecutive 1s
max_streak = 0
cur_streak = 1
last = 0
for j in sorted(jolts):
    d = j - last
    last = j
    if d == 1:
        cur_streak = cur_streak + 1
    else:
        max_streak = max(max_streak, cur_streak)
        cur_streak = 0


# %% build number of possiible apater for 1s stream

# 3 1s in a row make up for 2 possibilities
# 4 1s in a row make up for 4 possibilities

pos_list = [1] * (max_streak+2)
pos_list[3] = 2
pos_list[4] = 4
p = [1,1,1,1]
for pos in range(5, len(pos_list)):
    v = [0] * 4
    v[0] = p[1]
    v[1] = p[2]+ p[3]
    v[2] = p[0]+ p[1]
    v[3] = p[2]+ p[3]
    p = v
    pos_list[pos] = sum(p)
print(pos_list)

# %% get max number of consecutive 1s
cur_streak = 1
last = 0
n_pos = 1
# add the last adapter manually
jolts.append(max(jolts)+3)
for j in sorted(jolts):
    d = j - last
    last = j
    #print(" -> ", j,f"cur_streak: {cur_streak} d: {d}")
    if d == 1:
        cur_streak = cur_streak + 1
    else:
        n_pos = n_pos * pos_list[cur_streak]
        cur_streak = 1

print("Solution 2:", n_pos)

# %%
