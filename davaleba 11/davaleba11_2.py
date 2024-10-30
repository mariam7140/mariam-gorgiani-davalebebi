def gcd(number_a, number_b):
    
    if number_a > 1000 or number_b > 1000:
        return("Incorrect input, please try again")
    elif number_a < 0 or number_b < 0:
        return("Incorrect input, please try again")
    
    minimum = min(number_a, number_b)
    while minimum > 0:
        if number_a % minimum == 0 and number_b % minimum == 0:
            return minimum
        else:
            minimum -= 1

number_a = int(input("Please enter the first number: "))
number_b = int(input("Please enter the second number: "))

result = gcd(number_a, number_b)
print(result)