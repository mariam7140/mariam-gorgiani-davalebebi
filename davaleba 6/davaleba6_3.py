n = int(input("Enter an integer from 0 to 10000: "))

if n <= 0 or n >= 10000:
    print("incorrect number")
else:
    reversed_number = 0
    sum_of_digits = 0

    while n > 0:
        digit = n % 10 # ბოლო ციფრი რაც არის იმის მიღება
        reversed_number = reversed_number * 10 + digit # ბოლო ციფრიდან მოყვება და თითოეულ ციკლში "მიუწერს" (მაგ; 0 * 10 + 3 = 3, ამის მერე 3*10+2=32 და ა.შ. სანამ 3297 არ მიიღება)
        sum_of_digits += digit #  წინა ციკლში მიღებულ ჯამს ამატებს ციფრს
        n = n // 10 # თითოეულ ციკლში ბოლო ციფრის გარდა რაც დარჩა
    
    print("Reversed number:", reversed_number)
    print("Sum of digits:", sum_of_digits)  

