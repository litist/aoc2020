#!/bin/python3

# %%
import re

filename = 'input'

with open(filename) as f:
    content = f.readlines()


rom = []

for i in content:
    [op, arg] = i.split(' ')

    rom.append(('foo', op, int(arg)))


print(rom)



# %% run the program
def run(_rom):
    pc = 0
    acc = 0
    n_ex = [0] * len(_rom)
    while n_ex[pc] < 1:

        n_ex[pc] = n_ex[pc] + 1
        
        if _rom[pc][1] == 'nop':
            pc = pc + 1
        elif _rom[pc][1] == 'acc':
            acc = acc + _rom[pc][2]
            pc = pc + 1

        elif _rom[pc][1] == 'jmp':
            pc = pc + _rom[pc][2]

        if pc >= len(_rom):
            return (True, acc)

    return (False, acc)


print('Solution 1: ', run(rom))


# %% second part
ex_pos_swapped = 0
while ex_pos_swapped < len(rom):

    new_rom = rom[:]

    if new_rom[ex_pos_swapped][1] == 'nop':
        new_rom[ex_pos_swapped] = (new_rom[ex_pos_swapped][0], 'jmp', new_rom[ex_pos_swapped][2])
    elif new_rom[ex_pos_swapped][1] == 'jmp':
        new_rom[ex_pos_swapped] = (new_rom[ex_pos_swapped][0], 'nop', new_rom[ex_pos_swapped][2])
    else:
        ex_pos_swapped = ex_pos_swapped + 1
        continue

    ex_pos_swapped = ex_pos_swapped + 1

    (term, acc) = run(new_rom)

    print(f"{ex_pos_swapped - 1} -> {new_rom[ex_pos_swapped - 1]} -> {term, acc} | {new_rom[1]}")

    if term:
        print("Solution 2:", acc)
        break
