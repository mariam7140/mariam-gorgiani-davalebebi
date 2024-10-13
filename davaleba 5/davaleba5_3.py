number = int(input("Enter a number from 0 to 19: "))

first = 0
second = 1

if 0 < number <= 19:
    if number == first:
        print(number)
    elif number == second:
        print(first, second)
    else:
        print(first, second, end=" ")
        
        while second + first <= number:
            next = first + second
            second_var = second
            second = next
            first = second_var
            print(second, end=" ")
            
else:
    print("wrong number, try again.")