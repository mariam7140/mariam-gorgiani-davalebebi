user_input = input("Enter a string: ")

char_count = {} # სიმბოლო სტრინგში

for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"{char} - {count}")