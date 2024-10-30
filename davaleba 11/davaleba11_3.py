def lcm(number_a, number_b):
    
    if number_a > 1000 or number_b > 1000:
        return("Incorrect input, please try again")
    elif number_a < 0 or number_b < 0:
        return("Incorrect input, please try again")
    
    maximum = max(number_a, number_b)
    while True:
        if maximum % number_a == 0 and maximum % number_b == 0:
            return maximum
        maximum += 1

number_a = int(input("Please enter the first number: "))
number_b = int(input("Please enter the second number: "))

result = lcm(number_a, number_b)
print(result)