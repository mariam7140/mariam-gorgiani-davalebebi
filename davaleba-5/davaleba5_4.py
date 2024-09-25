
number = int(input("What's a number between 0 and 50: "))

if 0 < number < 50:
    spaces = number - 1
    print(" " * spaces, "*")
    
    for i in range(1, number):
        spaces = number - i
        print(" " * spaces, end="") 

        for j in range(i):
            print("/", end="")
    
        print("|", end="")
        
        for j in range(i):
            print("\\", end="")
        
        print()

else:
    print("Wrong number, try again.")

trunk = number - 1
print(" " * trunk, "|")
