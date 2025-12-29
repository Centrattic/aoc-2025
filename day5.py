ingreds = open("input5.txt").read().split("\n\n")

fresh_ranges = ingreds[0].split("\n")
ids = ingreds[1].split("\n")

# fresh_ranges = ["3-5","10-14","16-20","12-18"]
# ids = ["1","5","8","11","17","32"]

def get_count(fresh_ranges, ids):
    fresh_ids = []

    count = 0

    for i in ids:

        id = int(i)
    
        for rng in fresh_ranges: # cant make a list of range values, too large

            bounds = rng.split("-")
        
            a = int(bounds[0])

            b = int(bounds[1])

            if id > a and id <= b and id not in fresh_ids:
                # print(a,b,i)
                fresh_ids.append(id)
                count += 1

    return count

count = get_count(fresh_ranges, ids)
print(count)

# Part 2

tups = []

for rng in fresh_ranges:

    bounds = rng.split("-")
        
    a = int(bounds[0])   
    b = int(bounds[1])

    tups.append((a,b))
    
sort_rngs = sorted(tups)


# merge ranges instead of this cursed thing

i = 0
# while much easier than for when you have to control the counter!!
while i < len(sort_rngs) -1:
    
    curr_start = sort_rngs[i][0]
    curr_end = sort_rngs[i][1]
    
    next_start = sort_rngs[i+1][0]
    next_end = sort_rngs[i+1][1]

    if next_start >= curr_start and next_start <= curr_end + 1:
        print(curr_start, curr_end, next_start, next_end)
        new_rng = (curr_start, max(curr_end, next_end))
        print(new_rng)
        sort_rngs[i] = new_rng
        del sort_rngs[i+1]
    else:
        i += 1
print(sort_rngs)
        
tot = 0

for rng in sort_rngs:
    a, b = rng
    tot += b - a + 1

print(tot)
        
