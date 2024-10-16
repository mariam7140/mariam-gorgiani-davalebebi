string = input("Enter the string: ")

for i in range (0, len(string)):
    if i % 2 == 0 and string[i] != "e":
        print(string[i], end="")