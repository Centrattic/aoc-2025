banks = open("input3.txt").read().splitlines()

def find_max(arr):
    
    max_jol = 0
    max_jol_id = -1

    for j in range(len(arr)):
        if int(arr[j]) > max_jol:
            max_jol = int(arr[j])
            max_jol_id = j

    return max_jol, max_jol_id

total_joltage = 0

# banks = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

for i in range(len(banks)):
    bank = banks[i] # str
    
    # find earliest instance of max value in bank (excluding last value)
    max_jol, max_jol_id = find_max(bank[:-1])
    
    # find max value in bank[max_jol_id +1:]
    sec_max_jol, _ = find_max(bank[max_jol_id+1:])

    max_joltage = str(max_jol)+str(sec_max_jol)

    # print(max_joltage)
    
    total_joltage += int(max_joltage)

print(total_joltage)

total_joltage_2 = 0

for i in range(len(banks)):

    bank = banks[i]

    max_joltage = ""
    max_jol_id = -1
    cum_id = 0
    
    for j in range(12): # 0 - 11
        e = 12 - j - 1
        cum_id += max_jol_id + 1
        # print(bank[cum_id:-e])
        
        if e != 0:
            max_jol, max_jol_id = find_max(bank[cum_id:-e])
        if e == 0:
            max_jol, max_jol_id = find_max(bank[cum_id:])
            
        max_joltage += str(max_jol)

    print(max_joltage)
    total_joltage_2 += int(max_joltage)

print(total_joltage_2)

    
