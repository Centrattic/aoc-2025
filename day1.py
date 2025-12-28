
def apply_rotation(pos, rot):
    d = rot[0]
    n = int(rot[1:])

    zero_crossings = 0
    
    if d == "L":
        new_pos = (pos - n) % 100
        if pos - n < 0: # not eq
            
            zero_crossings += abs(pos-n)//100

            if pos != 0:
                zero_crossings += 1
            if new_pos == 0:
                zero_crossings -= 1
                
    if d == "R":
        new_pos = (pos + n) % 100

        if pos + n > 100: # not eq
            print(pos,n)
            zero_crossings += (pos+n)//100

            if new_pos == 0:
                zero_crossings -= 1
            
    return new_pos, zero_crossings

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

start_pos = 50
password = 0

curr_pos = start_pos

# lines = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

for i in range(len(lines)):
    rot = lines[i]
    # print(rot)
    curr_pos, _ = apply_rotation(curr_pos, rot)
    # print(curr_pos)
    if curr_pos == 0:
        password += 1

print(password)

curr_pos = start_pos
password_2 = 0

for i in range(len(lines)):
    rot = lines[i]
    curr_pos, zero_crossings = apply_rotation(curr_pos, rot)
    print(curr_pos)
    print("cross",zero_crossings)
    if curr_pos == 0:
        password_2 += 1
        
    password_2 += zero_crossings

print(password_2)
    
