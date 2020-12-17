#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()


mem = {}

for c in content:
    [a, b] = c.split(' = ')

    if a.strip() == 'mask':

        mask = b.strip()
        and_mask = np.power(2, 36, dtype=np.int64) - 1
        or_mask = 0
        for i in range(0, len(mask)):
            if mask[-1*i-1] == '1':
                or_mask = or_mask + np.power(2, i, dtype=np.int64)
            elif mask[-1*i-1] == '0':
                and_mask = and_mask - np.power(2, i, dtype=np.int64)
                #print(i)
        
        # print(f"b:\t{mask}\n&\t{and_mask:b}\n|\t{or_mask:b}\n\n")

    else:
        address = int(a.split(']')[0][4:])
        value = np.int64(b)
        #print(a,b, address, value)

        if value > np.power(2,32, dtype=np.int64):
            print(f"v\t{value}\nv\t{value:036b}\n\t{((value & and_mask) | or_mask):b}")

        mem[address] = ((value & and_mask) | or_mask)


#print(mem)
#f"{np.power(2, 6, dtype=np.int64) - 1:b}"

s = 0
for k in mem.keys():
    s = s + mem[k]

print("Solution 1:", s)

# %% part 2

mem = {}

for c in content:
    [a, b] = c.split(' = ')

    if a.strip() == 'mask':

        mask = b.strip()
        and_mask = np.int64(0)
        or_mask = np.int64(0)
        x_pos = []
        for i in range(0, len(mask)):
            if mask[-1*i-1] == '1':
                or_mask = or_mask + np.power(2, i, dtype=np.int64)
            elif mask[-1*i-1] == '0':
                and_mask = and_mask + np.power(2, i, dtype=np.int64)
                #print(i)
            elif mask[-1*i-1] == 'X':
                x_pos.append(i)
        
        #print(f"b:\t{mask}\n&\t{and_mask:b}\n|\t{or_mask:b}\n\n")
        #print(x_pos)

    else:
        address = np.int64(a.split(']')[0][4:])
        value = np.int64(b)
        #print(a,b, address, value)

        al = np.array(list(np.binary_repr(((address & and_mask) | or_mask), width=36)), dtype=np.int64)

        for adr in range(0, np.power(2,len(x_pos))):
            x_bin = np.array(list(np.binary_repr(adr, width=len(x_pos))), dtype=np.int64)

            for i in range(len(x_pos)):
                al[x_pos[i]*-1 - 1] = x_bin[i*-1 - 1]
            
            adr_x = al.dot(1 << np.arange(al.size, dtype=np.int64)[::-1])
            #print(x_bin , al, adr_x)

            mem[adr_x] = value
            

        #print(f"v\t{value}\nv\t{value:036b}\n\t{((value & and_mask) | or_mask):b}")



        #mem[address] = ((value & and_mask) | or_mask)
s = 0
for k in mem.keys():
    s = s + mem[k]

print("Solution 2:", s)

# %%
