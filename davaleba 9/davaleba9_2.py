# მიიღებს ნატურალურ რიცხვს n, (n>1)
# დააგენერირებს n ცალ წყვილ შემთხვევით რიცხვს a, b (0<a<1; 0<b<1)
# შემოიღეთ მთვლელი counter
# თუ დაგენერირებული რიცხვი აკმაყოფილებს პირობას math.sqrt(a ** 2 + b ** 2) <= 1, counter იზრდება 1-ით
# დაბეჭდოს 4 * counter / n

import random
import math

number = int(input("Please enter a natural number (n>1): "))

# ეს რიცხვები უნდა იყოს n ცალი

if number <= 1:
    print("Wrong number, please try again")
else:
    counter = 0 

    for i in range(number):
        a_rand = random.random()
        b_rand = random.random()
        print(a_rand, b_rand)
        
        if math.sqrt(a_rand ** 2 + b_rand ** 2) <= 1:
            counter += 1
    
    print(4 * counter / number)
