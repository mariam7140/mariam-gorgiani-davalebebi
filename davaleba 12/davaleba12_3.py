import random

list_random_numbers = []
shortlist = []
count = 50

for i in range(count):
    random_number = random.randint(1, 30)
    list_random_numbers.append(random_number)
    if random_number not in shortlist:
        shortlist.append(random_number)


print("Generated list is ", list_random_numbers)
print("shorted list is ", shortlist)
print("Length of the shorted list is ", len(shortlist))