import random

numbers = []

for i in range(100):
    random_numbers = random.randint(1, 1000000000)
    numbers.append(random_numbers)

longest_number = max(numbers, key=lambda x: len(str(x)))
shortest_number = min(numbers, key=lambda x: len(str(x)))
sorted_min_max = sorted(numbers)
sorted_max_min = sorted(numbers, reverse=True)

print("Generated Numbers: ", numbers)
print("The Longest Number: ", longest_number)
print("The Shortest Number: ", shortest_number)
print("Numbers sorted from minimum to maximum: ", sorted_min_max)
print("Numners sorted from maximum to minimum: ", sorted_max_min)