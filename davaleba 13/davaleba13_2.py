import random

list1 = []
for i in range(10):
    random_numbers = random.randint(1, 100)
    list1.append(random_numbers)

list2 = []
for i in range(10):
    random_numbers = random.randint(1, 100)
    list2.append(random_numbers)

list3 = []
for i in range(10):
    random_numbers = random.randint(1, 100)
    list3.append(random_numbers)

sums = []
for i in range(10):
    sum_of_indexes = list1[i] + list2[i] + list3[i]
    sums.append(sum_of_indexes)


print("List 1: ", list1)
print("LIst 2: ", list2)
print("list 3: ", list3)
print("Sum of numbers with the same indexes: ", sums)