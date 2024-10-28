def number_factorial():
    number = int(input("Please enter the number: "))
    factorial = 1

    for i in range(1, number+1):
        factorial *= i
    
    print("Factorial of", number, "is ", factorial)

number_factorial()

# p.s როგორც ვნახე math-ში factorial() ფუნქცია არსებობს, მაგრამ რადგან ფუნქციის განსაზრვრაზე ვართ ჩემით განვსაზღვრე <333 შემდეგში გამოვიყენებ ხოლმე ამ ფუნქციასაც