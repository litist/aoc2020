#!/bin/python3

# %%
import re


filename = 'input'

with open(filename) as f:
    content = f.readlines()

# %%
maxSeatId = 0
seats = []
for p in content:
    row = int(p[0:7].replace('F', '0').replace('B', '1'), 2)
    seat = int(p[7:10].replace('L', '0').replace('R', '1'), 2)

    seatId = row*8 + seat
    maxSeatId = max(maxSeatId, seatId)
    print(p, row, seat, seatId)

    seats.append(seatId)

print("Solution: ", maxSeatId)

mySeat = maxSeatId
while mySeat > 0:

    if mySeat in seats:
        mySeat = mySeat - 1
    else:
        print("mySeat is not in list", mySeat)
        break

print("Solution 2: ", mySeat)
