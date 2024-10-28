def number_type():
    number = int(input("Please enter a number: "))
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    if len(divisors) == 2:
        print("This is a prime number")
    elif len(divisors) == 1:
        print("Number 1 is neither prime nor composite.")
    else:
        print("This is a composite number")

number_type()