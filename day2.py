closed_ranges = open("input2.txt").read().split(",")

print(closed_ranges)

invalid_sum = 0

for i in range(len(closed_ranges)):
    bounds = closed_ranges[i].split("-")
    bounds = [int(i) for i in bounds]

    # print(bounds)
    
    for j in range(bounds[0], bounds[1]+1):
        val = str(j)
        if len(val) % 2 == 0:
            dup_len = int(len(val)/2)
            if val[:dup_len] == val[dup_len:]:
                invalid_sum += j

print(invalid_sum)


# closed_ranges = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]

invalid_sum_2 = 0

for i in range(len(closed_ranges)):
    bounds = closed_ranges[i].split("-")
    bounds = [int(i) for i in bounds]
    
    for j in range(bounds[0], bounds[1]+1):

        val = str(j)

        for k in range(2,len(val)+1):
            
            if len(val) % k == 0:
                
                dup_len = int(len(val)/k)
                
                if val[:dup_len]*k == val:
                    # print(j)
                    invalid_sum_2 += j
                    break

print(invalid_sum_2)
    
