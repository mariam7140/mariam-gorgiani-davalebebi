import random

list_random_numbers = []
expanded_list = []
count = 50

for i in range(count):
    random_number = random.randint(1, 30)
    list_random_numbers.append(random_number)
    expanded_list.extend([random_number] * random_number)


print("Generated list is ", list_random_numbers)
print("Expanded list is ", expanded_list)
print("Length of the expanded list is ", len(expanded_list))
