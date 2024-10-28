import random

dice_roll = 0

while True:
    answer = input("Roll the dice? (y/n): ").lower()
    if answer == "y":
        dice_amount = int(input("How many dices do you want to roll? "))
        for i in range(dice_amount):
            random_num1 = random.randint(1, 6)
            random_num2 = random.randint(1, 6)
            print(f"{random_num1, random_num2}")
            dice_roll += 1
    elif answer == "n":
        print(f"Dices rolled in total: {dice_roll}")
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")