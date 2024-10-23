# მიიღოს ნატურალური რიცხვი n, n>1
# დათვალოს x
# x = 4 * (1 - 1/3 + 1/5 - 1/9 - ... (+/-)1 / (2n - 1))
# 

number = int(input("Please enter a natural number (n>1): "))

if number <= 1:
    print("Wrong number, please try again")
else:
    x = 0
    for i in range(number):
       mnishvneli = 2 * i + 1
       
       if i % 2 == 0:
          x += 1 / mnishvneli
       else:
           x -= 1 / mnishvneli
    
    x = x * 4
    print("x = ", x)

