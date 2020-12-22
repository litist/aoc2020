#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()

N_steps = 6+1
#grid=np.zeros((1+2*N_steps, len(content)+2*N_steps, len(content[0])+2*N_steps), dtype=np.bool)
grid_=np.zeros((1+2*N_steps, 1+2*N_steps, len(content)+2*N_steps, len(content[0].strip())+2*N_steps), dtype=np.int8)


w = N_steps
z = N_steps
y = N_steps
for l in content:
    x = N_steps
    for c in l.strip():
        # mark as active 
        if c == '#':
            grid_[w,z,y,x] = 1
        x = x + 1

    y = y + 1
# %%
def step(grid):
    G = np.copy(grid)
    (W, Z, Y, X) = grid.shape
    w = N_steps
    for z in range(1, Z - 1):
        for y in range(1, Y - 1):
            for x in range(1, X - 1):
                N_active = np.sum(G[w, z-1:z+2, y-1:y+2, x-1:x+2])
 
                if G[w,z,y,x] == 1 and ( 3 <= N_active <= 4):
                    grid[w,z,y,x] = 1
                else:
                    grid[w,z,y,x] = 0

                if G[w,z,y,x] == 0 and N_active == 3:
                    grid[w,z,y,x] = 1
      

grid = np.copy(grid_)
for s in range(6):
    step(grid)

#    for z in range(len(grid)):
#        if np.sum(grid[z,:,:]) == 0:
#            continue
#        print("Z: ", z)
#        print(grid[z,:,:])

print("Solution 1: ", np.sum(grid))

# %%
def step2(grid):
    G = np.copy(grid)
    (W, Z, Y, X) = grid.shape
    w = N_steps
    for w in range(1, W - 1):
        for z in range(1, Z - 1):
            for y in range(1, Y - 1):
                for x in range(1, X - 1):
                    N_active = np.sum(G[w-1:w+2, z-1:z+2, y-1:y+2, x-1:x+2])

                    if G[w,z,y,x] == 1 and ( 3 <= N_active <= 4):
                        grid[w,z,y,x] = 1
                    else:
                        grid[w,z,y,x] = 0

                    if G[w,z,y,x] == 0 and N_active == 3:
                        grid[w,z,y,x] = 1
      

grid = np.copy(grid_)
for s in range(6):
    print("Step ", s)
    step2(grid)

#    (W, Z, Y, X) = grid.shape
#    for w in range(W):
#        for z in range(Z):
#            if np.sum(grid[w,z,:,:]) == 0:
#                continue
#            print("Z: ", z, " W: ", w)
#            print(grid[w,z,:,:])

print("Solution 2: ", np.sum(grid))
