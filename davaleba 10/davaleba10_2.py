def biggest_number():
    # სტრინგის შეყვანა და მისი დასპლიტვა რიცხვებად (რიცხვები  გამოყოფილია სფეისებით)
    user_input = input("Please enter integers: ").split()
    # input-ში რაც ჩავწერეთ - რიცხვითი ტიპის არგუმენტად გარდაქმნა და მათი ლისტში მოთავსება
    numbers = []
    for number in user_input:
        numbers.append(int(number))    

    # მაქსიმალური რიცხვის პოვნა
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

print(biggest_number())