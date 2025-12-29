rolls = open("input4.txt").read().splitlines()

# rolls = ["..@@.@@@@.", "@@@.@.@.@@","@@@@@.@.@@","@.@@@@..@.","@@.@@@@.@@",".@@@@@@@.@",".@.@.@.@@@","@.@@@.@@@@",".@@@@@@@@.","@.@.@@@.@."]

def check_rolls(rolls, update_rolls = False):

    num_rows = len(rolls)

    rolls_per_row = len(rolls[0])

    count = 0

    for i in range(num_rows):

        for j in range(rolls_per_row):

            if rolls[i][j] == "@":
                locs_full = 0
                
                to_check = [(i,j-1), (i,j+1), (i-1, j), (i-1, j+1), (i-1, j-1),
                            (i+1, j), (i+1, j-1), (i+1, j+1)]

                for tup in to_check:
                    
                    a,b = tup
                    
                    if a < 0 or a >= num_rows:
                        continue
                    if b < 0 or b >= rolls_per_row:
                        continue
                    
                    if rolls[a][b] == "@": # array, then string indexing
                        locs_full += 1

                if locs_full < 4:
                    count += 1
                    if update_rolls:
                        rolls[i] = rolls[i][:j] + "." + rolls[i][j+1:]
                    # print(i,j)
    if update_rolls:
        return count, rolls
    
    return count

count = check_rolls(rolls)

print(count)

# Part 2

count, rolls = check_rolls(rolls, update_rolls=True)

removable = count

while count > 0:
    count, rolls = check_rolls(rolls, update_rolls=True)
    removable += count

print(removable)
