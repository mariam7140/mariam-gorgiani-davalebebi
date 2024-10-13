import random

# პროგრამა ჩაიფიქრებს რიცხვს 0-100
generated_number = random.randint(0, 100)

# მომხმარებელს აქვს 10 მცდელობა
chances = 10

while chances > 0:
    # მომხმარებელს შეყავს თავისი ვარაუდი
    user_guess = int(input("Guess the number between 0 and 100: "))

    if user_guess == generated_number:
        print("You are the winner!")
        break # თუ მომხმარებელმა გამოიცნო ჩაფიქრებული რიცხვი, ციკლი წყდება
    elif user_guess > generated_number:
        print("high")
    else:
        print("low")
        
    chances -= 1


