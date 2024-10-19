string = input("Please write a string: ")
letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
# კითხვა - მინდოდა, რომ აქ isalpha() მეთოდი გამომეყენებინა, მაგრამ ვერ გავაკეთე. როგორ შეიძლება ამ მეთოდით განსაზღვრა ანბანში არის სიმბოლო თუ არა?

# უგულებელყოს a-z / A-Z სიმბოლოების გარდა ყველა

for i in string:
    if i not in letters:
        string = string.replace(i, "")

string = string.lower()
# დაადგინოს პალინდრომი არის თუ არა

if string[0:] == string[::-1]:
    print("Is palindrome")
else:
    print("Is not palindrome")
