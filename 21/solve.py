#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'
#filename = 'input_test'

with open(filename) as f:
    content = f.readlines()

#content.append('\n')

tiles = []
_food = []
for c in content:

    (ingrediants, allergens) = c.split('(contains')

    print(c, ingrediants, allergens)

    ing_l = []
    for ing in ingrediants.strip().split(' '):
        print("ingred: ", ing)
        ing_l.append(ing.strip())

    allerg_l = []
    for allerg in allergens.strip()[:-1].split(','):
        print("Allergen: ", allerg)
        allerg_l.append(allerg.strip())

    _food.append((set(ing_l), set(allerg_l)))

print(_food)

# %%
food = np.copy(_food)

allFood = set()
for f in _food:
    allFood = allFood.union(f[0])

done = False
while not done:
    done = True

    for i in range(len(food)):
        (il, al) = food[i]
        
        if len(al) == 1:
            print(f"Removing all inng: {il} whihc may contain {al}")
            for j in range(len(food)):
                if i == j:
                    continue
                
                (iil, aal) = food[j]

                if len(al & aal) == 1:
                    #print("UPDATE: ", il, " to ", il & iil)
                    
                    #goodFood = goodFood.union(il - iil)
                    print(f"Reduce list {j} from {len(il)} to {len(il & iil)}")
                    food[i] = (il & iil, al)
                    #food[j] = (il & iil, aal)
                    (il, al) = food[i]
                    done = False


                #print(iil, " MINUS ", il, " = ", iil - il)

                # food[j] = (iil - il, aal - al)

            print(f"Reduced to {il}")
        
            # remove all
            # food[i] = (set(), set())

            #print("stetp:\n" , food)
    print("Food step1:\n" , food)        

    for i in range(len(food)):
        (il, al) = food[i]
        
        if len(il) == 1 and len(al) == 1:
            for j in range(len(food)):
                if i == j:
                    continue
                
                (iil, aal) = food[j]

                food[j] = (iil - il, aal - al)


    for i in range(len(food)):
        (il, al) = food[i]

        if len(al) == 0:
            food[i] = (set(), set())


    print("FOOD:\n" , food)

badFood = set()
for f in food:
    badFood = badFood.union(f[0])

    
goodFood = allFood - badFood
print("GOOD FOOD: ", goodFood)



# %%
sol1 = 0
for f in _food:
    sol1 = sol1 + len(f[0] & goodFood)
    # print(sol1, f[0], goodFood)
print("Solution 1: ", sol1)

# %% part 2

l = [ (x[0].pop(), x[1].pop()) for x in food if len(x[0]) > 0]
l.sort(key=lambda x: x[1])

print("Solution 2: ", ','.join([k[0] for k in l]))
# %%
