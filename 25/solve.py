#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'
#filename = 'input_test'

with open(filename) as f:
    content = f.readlines()


pub_card = int(content[0].strip())
pub_door = int(content[1].strip())


# %% brute force 

subject = 7
value = 1
loop_count_card = 0
while value != pub_card:
    value = value * subject
    value = value % 20201227
    loop_count_card = loop_count_card + 1
print(value, loop_count_card)



value = 1
loop_count_door = 0
# %%
subject = 7
#value = 1
while value != pub_door:
    value = value * subject
    value = value % 20201227
    loop_count_door = loop_count_door + 1
print(value, loop_count_door)



# %%
subject = pub_card
value = 1
for loop in range(loop_count_door):
    value = value * subject
    value = value % 20201227
enc_key_door = value

print("door enc ", enc_key_door)

subject = pub_door
value = 1
for loop in range(loop_count_card):
    value = value * subject
    value = value % 20201227
enc_key_card = value

print("card enc ", enc_key_card)
