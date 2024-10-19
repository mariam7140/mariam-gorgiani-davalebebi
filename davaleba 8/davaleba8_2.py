# მიიღებს 2 სტრიქონს

string_one = input("Please input the first string: ").strip().lower()
string_two = input("Please input the second string: ").strip().lower()

# შეამოწმოს არის თუ არა შესაძლებელი პირველის სიმბოლოებით მეორე სტრიქონის მიღება

if len(string_one) != len(string_two):
    print("NO")
else:
    for i in string_one:
        if string_one.count(i) != string_two.count(i):
            print("NO")
            break
    else:
        print("YES")