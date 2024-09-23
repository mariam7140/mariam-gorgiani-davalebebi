number = int(input("Please enter a number from 0 to 1000: "))

if 0 < number < 1000:
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print("these are divisors: ", divisors)
else:
    print("Wrong number!")