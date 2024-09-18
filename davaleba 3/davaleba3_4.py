# random მოდული

import random

# ყველა შესაძლო ნომერი
# ყველა შესაძლო ფერი

numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
colors = ["Clubs", "Diamond", "Hearts", "Spades"]

# ფუნქციის განსაზღვრა --> რენდომ კარტის ამოღება

def draw_random_card():
    num = random.choice(numbers) 
    col = random.choice(colors)
    return num, col

# რენდომ კარტის დაბეჭდვა

your_card = draw_random_card()
print("Your random card is ", your_card)
