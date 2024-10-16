word = input("enter the word: ")

for i in range (0, len(word)):
    if word[i] != "a" and word[i] != "e" and word[i] != "i" and word[i] != "o" and word[i] != "u": # ეს ხაზი არ ვიცი უფრო მარტივად როგორ დავწერო
        print(word[i], end="")