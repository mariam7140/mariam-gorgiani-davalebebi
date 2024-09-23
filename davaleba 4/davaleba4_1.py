import random

player_number = int(input("Enter player number: "))

for i in range(player_number):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1,6)
    print(dice_1, dice_2)