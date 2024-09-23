import random

number = int(input("Enter an integer from 0 to 30: "))

if 0 < number < 30:
    rand_nums = []
    
    for i in range(number):
        rand_num = random.randint(0, 1000)
        rand_nums.append(rand_num)
    
    print("Generated numbers: ", rand_nums)
    print("Generated max number: ", max(rand_nums))


else:
    print("Wrong number!")