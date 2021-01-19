#!/bin/python3

# %%
import re
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm

filename = 'input'
#filename = 'input_test'

with open(filename) as f:
    content = f.readlines()

N = 130
ref_x = int(N/2)
ref_y = int(N/2)
tiles = np.zeros((N, N), dtype=bool)

# %%
for op in content:
    op = op.strip()
    print(op)

    pos = 0
    i = 0

    cur_px = ref_x
    cur_py = ref_y
    while(pos < len(op)):
        i = i + 1
        n = op[pos:pos+2]

        if op[pos] == 'n':

            if op[pos+1] == 'e':
                cur_px = cur_px + (cur_py % 2)
                cur_py = cur_py - 1
                pos = pos + 2
                continue
            if op[pos+1] == 'w':
                cur_py = cur_py - 1
                cur_px = cur_px - (cur_py % 2)
                pos = pos + 2
                continue

        if op[pos] == 's':

            if op[pos+1] == 'e':
                cur_px = cur_px + (cur_py % 2)
                cur_py = cur_py + 1
                pos = pos + 2
                continue
            if op[pos+1] == 'w':
                cur_py = cur_py + 1
                cur_px = cur_px - (cur_py % 2)
                pos = pos + 2
                continue

        if op[pos] == 'e':
            cur_px = cur_px + 1
            pos = pos + 1
            continue

        if op[pos] == 'w':
            cur_px = cur_px - 1
            pos = pos + 1
            continue

        print("ERROR", op, pos, n, i )

    tiles[cur_py, cur_px] = not tiles[cur_py, cur_px]
    print(f"Flip tile on {cur_px},{cur_py} to {tiles[cur_py, cur_px]}")

print("Solution 1", np.count_nonzero(tiles == True))

#%% PART II

art = tiles.copy()
art = art.astype(int)

art2 = art.copy()

for day in range(100):
    art = art2.copy()

    second_ring_true = np.count_nonzero(art[1,:] == True) + np.count_nonzero(art[-2,:] == True) + np.count_nonzero(art[:, 1] == True) + np.count_nonzero(art[:, -2] == True)
    if second_ring_true > 0:
        print("ERROR: INCRESE TILES SPACE: ", second_ring_true)
        break
    for y in range(1,N-1):
        for x in range(1,N-1):

            # get number of black tiles
            n = art[y, x-1] + art[y, x+1]
            n = n + art[y-1, x-1+(y%2)] + art[y-1, x+(y%2)]
            n = n + art[y+1, x-1+(y%2)] + art[y+1, x+(y%2)]
            #print(y,x,n)

            if art[y, x] == 1 and (n == 0 or n > 2):
                art2[y,x] = 0

            if art[y, x] == 0 and (n == 2):
                art2[y,x] = 1

    print(f"Day {day}: {np.count_nonzero(art2 == True)}")
print("Solution 2", np.count_nonzero(art2 == True))

# %% PLOT
hexa = np.zeros((2*art.shape[0], 2*art.shape[1]))

for y in range(N):
    for x in range(N):
        hexa[2*y, 2*x + ((y)%2)] = art2[y,x]

fig = plt.figure()
plt.imshow(hexa, cmap=cm.Greys_r)
plt.savefig('hex_grid.png', dpi=300)
