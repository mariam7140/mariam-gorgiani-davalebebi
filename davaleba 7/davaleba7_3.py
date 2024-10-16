word = input("Enter the word: ")
word_length = len(word)

if word_length % 2 == 0:
    middle_character = word[(word_length // 2) - 1] + word[(word_length // 2)]
else:
    middle_character = word[(word_length // 2)]

count = 0

while count < 5:
    print(word[1], middle_character, word[-1])
    count += 1