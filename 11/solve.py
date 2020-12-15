#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()

seats = np.zeros((len(content)+2, len(content[0].strip())+2), dtype=int)

for y in range(0, len(content)):
    c = content[y].strip()
    for x in range(0, len(c)):
        seats[y+1, x+1] = ord(c[x])

seats_p2 = np.copy(seats)

print(seats_p2)


#%% part 2
def step_p2(s):
    (ny, nx) = s.shape

    seats_lin = np.copy(s)
    seats_lin = seats_lin.reshape(-1)

    n_changes = 0

    for p in range(0, len(seats_lin)):

        if not (seats_lin[p] == ord('L') or seats_lin[p] == ord('#')):
            continue

        seat_occ = 0
        # check items to the left
        #left = seats_lin[p:p-(p%nx)-1:-1]
        for e in seats_lin[p:p-(p%nx):-1][1:]:
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        for e in seats_lin[p:p-(p%nx)+nx:1][1:]:
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        # top
        for e in seats_lin[p::-nx][1:]:
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        #bottom
        for e in seats_lin[p::nx][1:]:
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        # topright = seats_lin[p::-(nx-1)]
        for e in seats_lin[p::-(nx-1)][1:]:
            if e == 0:
                break
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        # topleft = seats_lin[p::-(nx+1)]
        for e in seats_lin[p::-(nx+1)][1:]:
            if e == 0:
                break
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        # bottomright = seats_lin[p::(nx+1)]
        for e in seats_lin[p::(nx+1)][1:]:
            if e == 0:
                break
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        # bottomleft = seats_lin[p::(nx-1)]
        for e in seats_lin[p::(nx-1)][1:]:
            if e == 0:
                break
            if e == ord('#'):
                seat_occ = seat_occ + 1
                break
            if e == ord('L'):
                break

        if seats_lin[p] == ord('L') and seat_occ == 0:
            s[p // nx, p % nx] = ord('#')
            n_changes = n_changes + 1

        if seats_lin[p] == ord('#') and seat_occ >= 5:
            s[p // nx, p % nx] = ord('L')
            n_changes = n_changes + 1

        # print(f"p: {p} {seats_lin[p]} -> {s[p // nx, p % nx]}", "seat_occ: ", seat_occ, "seat_free: ", seat_free)

    return n_changes


print(seats_p2)
n = 1
iterations = 0
while(n>0):
    n = step_p2(seats_p2)
    iterations = iterations + 1
    # print(seats_p2)

print("Solution 2: ", np.count_nonzero(seats_p2 == ord('#')))
print(f"This took {iterations} iterations.")



# %%
# make a step
def step(s):

    _seats = np.copy(s)
    (ny, nx) = _seats.shape

    n_changes = 0
    for y in range(1, ny-1):
        for x in range(1, nx-1):

            if _seats[y,x] == ord('L'):
                if np.count_nonzero(_seats[y-1:y+2, x-1:x+2] == ord('#')) == 0:
                    s[y,x] = ord('#')
                    n_changes = n_changes + 1
                
            if _seats[y,x] == ord('#'):
                if np.count_nonzero(_seats[y-1:y+2, x-1:x+2] == ord('#')) >= 5:
                    s[y,x] = ord('L')
                    n_changes = n_changes + 1

    print("n_changes: ", n_changes)

    return n_changes

n = 1
while(n>0):
    n = step(seats)
    print(seats)

print("Solution 1: ", np.count_nonzero(seats == ord('#')))
