# მიიღოს ნატურალური რიცხვი
number = int(input("Please enter a number from 0 to 50: "))

# 0 < ნატ.რიცხ < 50
if 0 < number < 50:
    i = 1
    while i <= number: # ციკლი, რომელიც 0-დან number-მდე მიიღებს რიცხვებს
        divisors = []  # გამყოფების სია 
        count = 0
        j = 1
        while j <= i: # ციკლი, რომელიც მიიღებს 0-დან number-მდე კონკრეტული რიცხვის გამყოფებს
            if i % j == 0:
                divisors.append(j) # ამ ციკლში მიღებული გამყოფების მოთავსება სიაში
                count += 1
            if count == 3:
                break
            j += 1
        # დაბეჭდოს რიცხვი და მისი გამყოფი
        print(i, "-", divisors)
        i += 1
else:
    print("Please enter a valid number between 0 and 50.")