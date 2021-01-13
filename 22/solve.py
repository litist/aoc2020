#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'
#filename = 'input_test'

with open(filename) as f:
    content = f.readlines()

content.append('\n')

i = 0
if content[i].strip() != "Player 1:":
    print("ERROR")

i = i + 1

p0 = []
while content[i].strip() != '':
    p0.append(int(content[i].strip()))
    i = i + 1

i = i + 1

if content[i].strip() != "Player 2:":
    print("ERROR")

i = i + 1

p1 = []
while content[i].strip() != '':
    p1.append(int(content[i].strip()))
    i = i + 1


# %%
def game(p0, p1):

    print(p0)
    print(p1)

    while(len(p0)>0 and len(p1)>0):
        if p0[0] > p1[0]:
            p0.append(p0.pop(0))
            p0.append(p1.pop(0))
        elif p0[0] < p1[0]:
            p1.append(p1.pop(0))
            p1.append(p0.pop(0))
        else:
            print("ERROR")

    print(p0)
    print(p1)

    return (p0, p1)

(r0, r1) = game(p0.copy(), p1.copy())


score = 0
for i in range(len(r0)):
    score = score + r0[i]*(len(r0) - i )

for i in range(len(r1)):
    score = score + r1[i]*(len(r1) - i )

print("Solution 1: ", score)

# %%
def gameRec(p0, p1):

    history_p0 = []
    history_p1 = []


    while(len(p0)>0 and len(p1)>0):
        #print("Player 1 deck: ", p0)
        #print("Player 2 deck: ", p1)

        # check for already seen decks
        if p0 in history_p0 or p1 in history_p1:
            #print("found current deck of player0 in history,", history_p0)
            return ([1], [])

        history_p0.append(p0[:])
        history_p1.append(p1[:])

        if p0[0] < len(p0) and p1[0] < len(p1):
            #print("Starting recursion")
            # do recursion
            (r0, r1) = gameRec(p0[1:1+p0[0]], p1[1:1+p1[0]])

            if len(r1) == 0 and len(r0) > 0:
                #r0 won
                p0.append(p0.pop(0))
                p0.append(p1.pop(0))
            elif len(r0) == 0 and len(r1) > 0:
                # r1 won
                p1.append(p1.pop(0))
                p1.append(p0.pop(0))
            else:
                print("ERROR in recursion")
        
        else:


            if p0[0] > p1[0]:
                p0.append(p0.pop(0))
                p0.append(p1.pop(0))
            elif p0[0] < p1[0]:
                p1.append(p1.pop(0))
                p1.append(p0.pop(0))
            else:
                print("ERROR")

    return (p0, p1)


(r0, r1) = gameRec(p0.copy(), p1.copy())
print("After the game:")
print("Player 1 deck: ", r0)
print("Player 2 deck: ", r1)
score = 0
for i in range(len(r0)):
    score = score + r0[i]*(len(r0) - i )

for i in range(len(r1)):
    score = score + r1[i]*(len(r1) - i )

print("Solution 2: ", score)

# %%
