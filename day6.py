probs = open("input6.txt").read().splitlines()

probs = ["123   328 51  64","45   64 387 23", "6 98 215 314", "* + * +"]

for i in range(len(probs)):
    edit = probs[i].split(" ")
    probs[i] = [k for k in edit if k != ""]
   
# print(probs)

num_probs = len(probs[0])

tot = 0

for i in range(num_probs):
    nums = []
    for j in range(len(probs)):
        nums.append(probs[j][i])
        
    op = nums[-1]
        
    if op == "*":
        val =1
    if op == "+":
        val = 0
            
    for k in range(len(nums)-1):
        if op == "*":
            val *= int(nums[k])
        if op == "+":
            val += int(nums[k])

    # print(val)
    tot += val

# print(tot)

# Part 2

probs = open("input6.txt").read().splitlines()

# probs = ["123 328  51 64 "," 45 64  387 23 ", "  6 98  215 314", "*   +   *   +  "]

# all cols are same length!

print(len(probs[0]), len(probs[1]), len(probs[2]), len(probs[3]))

cols = []
len_col = len(probs[0])
for i in range(len_col):
    val = ""
    for k in range(len(probs)):
        val += probs[k][i]
        
    cols.append(val)

cols.append(" ")
print(cols)

tot = 0

for i in range(len(cols)):
    col = cols[i]
    pos_op = col[-1]
    if pos_op == "*":
        op = "*"
        val = int(col[:-1].strip())
    elif pos_op == "+":
        op = "+"
        val = int(col[:-1].strip())
    elif col.strip() == '':
        tot += val
        print("val", val)
    else:
        print("hmm", int(col.strip()))
        if op == "*":
            val *= int(col.strip())
        if op == "+":
            val += int(col.strip())

print(tot)
