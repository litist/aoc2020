#!/bin/python3

# %%
import re

filename = 'input'

with open(filename) as f:
    content = f.readlines()


# %%

# dict in which bag a bag is
bags = {}

for l in content:
    [bag, value] = l.strip().split('bags contain')

    ibags = value.strip().split(',')

    for ib in ibags:
        matchObj = re.match( r'^(\d+) ([a-z]+ [a-z]+) bags?', ib.strip(), re.I)
        if matchObj:
            #print(matchObj.group(1), matchObj.group(2) )
            if matchObj.group(2) not in bags:
                bags[matchObj.group(2)] = []    
            bags[matchObj.group(2)].append(bag.strip())
        else:
            if ib.strip() != 'no other bags.':
                print("ERRROR: ", ib.strip())


# %%

# find shiny gold
has_gold = 0

gold_list = bags['shiny gold']
bags_seen = []

while len(gold_list) > 0:
    if gold_list[0] in bags_seen:
        gold_list.pop(0)
        continue

    has_gold = has_gold + 1
    if gold_list[0] in bags:
        for i in bags[gold_list[0]]:
            gold_list.append(i)
    bags_seen.append(gold_list.pop(0))

print("Solution 1: ", has_gold)



# %%
# dict in which bag a bag is
bags = {}

for l in content:
    [bag, value] = l.strip().split('bags contain')

    ibags = value.strip().split(',')

    for ib in ibags:
        matchObj = re.match( r'^(\d+) ([a-z]+ [a-z]+) bags?', ib.strip(), re.I)
        if matchObj:
            if bag.strip() not in bags:
                bags[bag.strip()] = []

            bags[bag.strip()].append((matchObj.group(2).strip(), int(matchObj.group(1))))

        else:
            if ib.strip() != 'no other bags.':
                print("ERRROR: ", ib.strip())


# %%
def get_bags(bags, which):
    N = 1

    if which not in bags:
        #print(f"get_bags ankers for {which}")
        return N
    
    for b in bags[which]:
        N = N + b[1] * get_bags(bags, b[0])
    
    #print(f"get_bags returns {N} for {which}")
    return N

#print(bags)

# reduce by one, as we do not want the golden to count
print("Solution 2: ", get_bags(bags, 'shiny gold') - 1)

# %%
