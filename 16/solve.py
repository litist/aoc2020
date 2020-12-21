#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'

with open(filename) as f:
    content = f.readlines()

content.append('\n')

line = 0

ticketFields = []

while(content[line].strip() != ''):
    matchObj = re.match( r'^([a-zA-Z ]+): ([\d]+)-([\d]+) or ([\d]+)-([\d]+)?', content[line].strip())
    if matchObj:
        # print(matchObj.group(1), matchObj.group(2), matchObj.group(3), matchObj.group(4), matchObj.group(5) )
        ticketFields.append( (matchObj.group(1), (int(matchObj.group(2)), int(matchObj.group(3))),
         (int(matchObj.group(4)), int(matchObj.group(5)))))
        # if matchObj.group(2) not in bags:
        #     bags[matchObj.group(2)] = []    
        # bags[matchObj.group(2)].append(bag.strip())
    else:
        print("ERRROR: ", content[line].strip())
    line = line + 1

# print(ticketFields)

# get you ticket
yourTicket = content[line + 2]

line = line + 5

tickets = []
while(content[line].strip() != ''):
    #print("2: ", content[line])
    tickets.append( [ int(x) for x in content[line].strip().split(',') ] )
    line = line + 1
# %%


ticketScanningErrorRate = 0
validTickets = []
validTickets.append( [ int(x) for x in yourTicket.strip().split(',') ] )
for t in tickets:
    # each for a match on each field for the ticket
    isValied = True
    for f in t:
        for i in range(0, len(ticketFields)):
            [_, (a_1, b_1), (a_2, b_2)] = ticketFields[i]

            if ((a_1 <= f <= b_1) or (a_2 <= f <= b_2)):
                # print(f"fail on ticket {t} for field {f}")
                break
        else:
            # print(f"Not field found on ticket {t} for field {f}")
            ticketScanningErrorRate = ticketScanningErrorRate + f
            isValied = False

    if isValied:
        validTickets.append(t)

print("Solution 1: ", ticketScanningErrorRate)


# %%

resmat = np.zeros((len(validTickets[0]), len(validTickets[0])))

# build table, which rule matches to which field on all tickets
for tf in range(0, len(validTickets[0])):
    testField = np.array( [ x[tf] for x in validTickets ])
    #print("check field", tf)
    for i in range(0, len(ticketFields)):
        [_, (a_1, b_1), (a_2, b_2)] = ticketFields[i]

        if np.all(np.logical_or(np.logical_and(a_1 <= testField, testField <= b_1), np.logical_and(a_2 <= testField, testField <= b_2))):
            #print("We have a match")
            resmat[tf, i] = 1

#print(resmat)


sol2 = 1

for i in range(0, len(resmat)):
    nt_id = np.nonzero(np.sum(resmat, axis = 0) == 1)

    if len(nt_id[0]) == 1:
        r_id = nt_id[0][0]
        f_id = np.nonzero(resmat[:,r_id])[0][0]
        #print(f"Rule {r_id} only goes to field: {f_id}")
        resmat[f_id,:] = 0
        #print(resmat)

        # mulitply all depart fields from our ticket
        if r_id < 6:
            sol2 = sol2 * validTickets[0][f_id]

print("Solution 2: ", sol2)
# %%
