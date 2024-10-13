n = int(input("Enter an integer from 0 to 1000: "))

if n <= 0 or n >= 1000:
    print("incorrecტ number")
else:
    # მიმდევრობის დაწყევა
    while n != 1:
        print(n, end=" -> ")
        # თუ რიცხვი ლუწია, გავყოთ 2-ზე
        if n % 2 == 0:
            n = n // 2
        # თუ რიცხვი კენტია, გავამრავლოთ 3-ზე და მივუმატოთ 1
        else:
            n = n * 3 + 1

    print(1)