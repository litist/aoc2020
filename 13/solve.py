#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()

arrival = int(content[0].strip())


bus_id = []
for b in content[1].strip().split(','):
    if b == 'x':
        continue
    bus_id.append(int(b))
    print(b)


# %%
min_wait_id = bus_id[0]
for b in bus_id:
    min_wait = min_wait_id - (arrival % min_wait_id)
    if min_wait >= (b - (arrival % b)):
        min_wait_id = b

print("Solution 1:", (min_wait_id - (arrival % min_wait_id))*min_wait_id)

# %%
for t in range(0,4000):
    if (t + 0) % 17 != 0:
        continue

    #print(f"t:{t} fits to 17")
    if (t + 2) % 13 == 0:
        print(f"t:{t} fits to 17 and t+1 its to 13")



# %% part 2
bus_list = content[1].strip().split(',')
#bus_list = '1789,37,47,1889'.strip().split(',')


s_id = 1 # id of first valid bus
start = 0
for b in range(0, len(bus_list)):
    if bus_list[b] == 'x':
        continue
    
    r = np.lcm(s_id, int(bus_list[b]), dtype=np.int64)
    #print(f"lcm({s_id}, {int(bus_list[b])}) -> {r}")

    # check in bus_list[s_id] steps
    for t in range(start, r, s_id):
        # print("check t", t)

        #print(f"t:{t} fits to 17")
        if (t + b) % int(bus_list[b]) == 0:
            print(f"lcm({s_id}, {int(bus_list[b])}) -> {r} | t:{t} fits to {s_id} and t+{b} its to {bus_list[b]}")
            start = t
            s_id = r
            break
else:
    print("Solution 2:", t)
