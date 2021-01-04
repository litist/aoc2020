#!/bin/python3

# %%
import re
import numpy as np

filename = 'input'
#filename = 'input_test'

with open(filename) as f:
    content = f.readlines()

content.append('\n')

tiles = []

i = 0
while i < len(content):

    #print("Tile: ", i,  content[i])
    matchObj = re.match( r'^Tile ([\d]+):', content[i].strip())
    if matchObj:
        tile_id = int(matchObj.group(1))
    else:
        print("ERRROR: ", content[i].strip())

    i = i + 1

    arr = np.zeros((len(content[i].strip()), len(content[i].strip())))
    j = 0
    while(content[i].strip() != ''):
        
        line = list(content[i].strip())
        for a in range(len(line)):
            arr[j, a] = ord(line[a])

        i = i + 1
        j = j + 1


    #print(arr)

    tiles.append((tile_id, arr))

    i = i + 1

#print(tiles)


# %% part 1 
def p1():
    edges_product = 1
    matches_dist = [0, 0, 0, 0, 0]

    for ref_id in range(len(tiles)):


        (ct_nr, ct_arr) =  tiles[ref_id]

        s_matches = []
        for s in range(4):
            ct_arr = np.rot90(ct_arr)
            side = ct_arr[0,:]

            matches = 0
            for i in range(0, len(tiles)):
                (tile_nr, tile_arr) = tiles[i]

                if ct_nr == tile_nr:
                    continue



                #print(tile_arr)
                #print(tile_arr[0,:])
                #print(tile_arr[-1,:])
                #print(tile_arr[:, 0])
                #print(tile_arr[:,-1])

                if (side == tile_arr[0,:]).all():
                    #print("match")
                    matches = matches + 1
                
                if (side == tile_arr[0,::-1]).all():
                    #print("match")
                    matches = matches + 1

                if (side == tile_arr[-1,:]).all():
                    #print("match")
                    matches = matches + 1
                
                if (side == tile_arr[-1,::-1]).all():
                    #print("match")
                    matches = matches + 1

                if (side == tile_arr[:,0]).all():
                    #print("match")
                    matches = matches + 1
                
                if (side == tile_arr[::-1,0]).all():
                    #print("match")
                    matches = matches + 1

                if (side == tile_arr[:, -1]).all():
                    #print("match")
                    matches = matches + 1
                
                if (side == tile_arr[::-1, -1]).all():
                    #print("match")
                    matches = matches + 1

            #print(f"We found {matches} on side {s} of tile {ct_nr}")
            s_matches.append(matches)
        #print(s_matches)
        matches_dist[sum(s_matches)] = matches_dist[sum(s_matches)] + 1

        if sum(s_matches) == 2:
            edges_product = edges_product * ct_nr

    print("Fount mataches distirbution: ", matches_dist)

    print("Solution 1: ", edges_product)

p1()


# %% Part 2

# find the first edge, upper left

for ref_id in range(len(tiles)):


    (ct_nr, ct_arr) =  tiles[ref_id]

    s_matches = []
    for s in range(4):
        ct_arr = np.rot90(ct_arr)
        side = ct_arr[0,:]

        matches = 0
        for i in range(0, len(tiles)):
            (tile_nr, tile_arr) = tiles[i]

            if ct_nr == tile_nr:
                continue


            for r in range(4):
                if (side == np.rot90(tile_arr, r)[0, :]).all():
                    matches = matches + 1
                    print("match on ", tile_nr, np.rot90(tile_arr, r)[0, :])
            for r in range(4):
                if (side == np.rot90(tile_arr, r)[0, ::-1]).all():
                    matches = matches + 1
                    print("match on ", tile_nr, np.rot90(tile_arr, r)[0, ::-1])

        print(f"We found {matches} on side {s} of tile {ct_nr}")
        s_matches.append(matches)
    print(s_matches)
    #matches_dist[sum(s_matches)] = matches_dist[sum(s_matches)] + 1

    if sum(s_matches) == 2:
        break
print("First edge is on ", ref_id)

print("ct_arr ", ct_arr)

while not np.all(s_matches == [1, 1, 0, 0]):
    ct_arr = np.rot90(ct_arr)
    s_matches = np.roll(s_matches, -1)

print(ct_arr)

aligned = []

aligned.append(ct_arr)

tiles.pop(ref_id)
# find matching tiles to the right

# %%
N = int(np.sqrt(len(tiles)+1))
for fill in range(N-1):
    side = aligned[-1][:,-1]
    found = False
    for tile_i in range(len(tiles)):
        (tile_nr, tile_arr) = tiles[tile_i]

        for r in range(4):
            tile_arr = np.rot90(tile_arr)

            if (side == tile_arr[:, 0]).all():
                found = True
                #print("left side is okay: ", tile_arr)
                break

            tile_arr = tile_arr[::-1,:]
            
            if (side == tile_arr[:, 0]).all():
                found = True
                #print("left side flipped is okay: ", tile_arr)
                break

            tile_arr = tile_arr[::-1,:]
        
        if found:
            #print("solve with ttile: ", tile_nr, tile_arr)
            aligned.append(tile_arr)

            tiles.pop(tile_i)
            break
    else:
        print("ERROR: failed to find matching elemento ro right side")

aligned_mat = []
aligned_mat.append(aligned)
aligned = []

# %%
# find elements in next row
for cols in range(N-1):
    for fill in range(N):
        side = aligned_mat[-1][fill][-1,:]
        found = False
        for tile_i in range(len(tiles)):
            (tile_nr, tile_arr) = tiles[tile_i]
            #print("look ", tile_nr, tile_arr)
            for r in range(4):
                tile_arr = np.rot90(tile_arr)

                if (side == tile_arr[0, :]).all():
                    found = True
                    #print("top side is okay: ", tile_arr)
                    break

                tile_arr = tile_arr[:, ::-1]
                
                if (side == tile_arr[0, :]).all():
                    found = True
                    #print("top side flipped is okay: ", tile_arr)
                    break

                tile_arr = tile_arr[:, ::-1]

            if found:
                #print("solve with ttile: ", tile_nr, tile_arr)
                aligned.append(tile_arr)

                tiles.pop(tile_i)
                break
        else:
            print("ERROR: failed to find element to bottom")

    aligned_mat.append(aligned)
    aligned = []




# %%
monster=[
[ord(x) for x in "                  # "],
[ord(x) for x in "#    ##    ##    ###"],
[ord(x) for x in " #  #  #  #  #  #   "]]

# remove borders
matno_border = []
for c in range(len(aligned_mat)):
    tmp = []
    for r in range(len(aligned_mat[0])):
        tmp.append(aligned_mat[c][r][1:-1, 1:-1])
    matno_border.append(tmp)

# stick tiles together
f_mat = []
for col in range(len(matno_border)):
    f_mat.append(np.concatenate(matno_border[col], axis=1))
full_mat = np.concatenate(f_mat, axis=0)

# print
for c in full_mat:
    #print(c)
    l = ''
    for r in c:
        l = l + chr(int(r))
    print(l)

N_monsters = 0
for r in range(4):
    full_mat = np.rot90(full_mat)

    for mirror in range(2):
        full_mat = full_mat[:,::-1]

        for y in range(0, len(full_mat) - len(monster)):
            for x in range(0, len(full_mat[0]) - len(monster[0])):
                res = np.logical_or((full_mat[y:y+len(monster),x:x+len(monster[0])] == monster) , np.not_equal(monster , ord('#'))).all() == True
                if res:
                    print(f"We have a monster (x:{x} y;{y} r:{r} m:{mirror}):", full_mat[y:y+len(monster),x:x+len(monster[0])])
                    N_monsters = N_monsters + 1

print("Solution 2: ", np.sum(full_mat == ord('#')) - N_monsters*np.sum(np.array(monster) == ord('#')))
