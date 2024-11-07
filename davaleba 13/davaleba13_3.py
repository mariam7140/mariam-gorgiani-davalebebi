user_input = input("Enter the words (please separate them by spaces): ")

words = user_input.split()

words_filtered = []
for word in words:
    if len(word) <= 3:
        words_filtered.append(word)

words_uppercase = []
for word in words_filtered:
    words_uppercase.append(word.upper())

print("Filtered words in uppercase: ", words_uppercase) 