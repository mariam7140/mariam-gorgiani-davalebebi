import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

even = 0
odd = 0

for number in random_numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

number_quantity = {
    "even": even,
    "odd": odd
}

print("Random Numbers:", random_numbers)
print("Lexicon with counts:", number_quantity)