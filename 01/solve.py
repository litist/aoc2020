#!/bin/python3

filename = '01/input'

with open(filename) as f:
    content = f.readlines()

expense = list(map(lambda x: int(x.strip()), content))

for i in range(0, len(expense)):
    for j in range(i, len(expense)):
        if expense[i] + expense[j] == 2020:
            print(f"Part 1: {expense[i]} + {expense[j]} = 2020  *-> {expense[i]*expense[j]}")
        for k in range(j, len(expense)):
            if expense[i] + expense[j] + expense[k] == 2020:
                print(f"Part 2: {expense[i]} + {expense[j]} + {expense[k]} = 2020 *-> {expense[i]*expense[j]*expense[k]}")

# Remove first # to make it a interactive cell
##%%
