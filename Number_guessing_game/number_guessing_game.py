import random


min_attempts = 10
scores = {}
game = 1

def main():
    init_game()

def init_game():
    global game
    range_min = 0
    range_max = 0
    
    while range_min >= range_max:
        print(f"Enter the range for Game {game}")
        try:
            range_min = int(input("Minimum: "))
            range_max = int(input("Maximum: "))
            print()
            if range_min >= range_max:
                print("Maxmimum range cannot be smaller or equal to Minimum range.")
        except ValueError:
            print()
            print("Please enter a valid number.")
            print()
    start_game(range_min, range_max)

def start_game(range_min, range_max):
    global min_attempts
    global game
    
    number = random.randint(range_min, range_max)
    attempts = 0
    max_guesses = 10

    while max_guesses > 0:
        try:
            print(f"You have {max_guesses} guesses left.")
            user_num = int(input(f"Guess the number (between {range_min} and {range_max}): "))
            print()
            
            # Handling correct Range
            if user_num < range_min or user_num > range_max:
                print("Your number is not in the specified range!")
                print()
                continue
            
            attempts += 1
            max_guesses -= 1
            
            if user_num == number:
                if attempts < min_attempts:
                    min_attempts = attempts
                    print(f"***** You broke the record with {attempts} attempts! *****")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                scores[f"Game {game}"] = f"{attempts} attempts"
                show_highscores()
                new_game()
            elif user_num > number:
                print("Too high! Try again.\n")
            elif user_num < number:
                print("Too low! Try again.\n")
        except ValueError:
            print()
            print("Please enter a valid number.\n")

    print("You are out of guesses! Game Over.")
    scores[f"Game {game}"] = f"{attempts} attempts"
    show_highscores()
    new_game()

def show_highscores():
    print("___________________________")
    print("Scoreboard:")
    for game, score in scores.items():
        print(f"{game}: {score}")
    print()
    print(f"Bestscore: {min_attempts} attempts")
    print("___________________________")

def new_game():
    global game
    while True:
        try:
            play_again = input("Play again? (y/n): ").lower()
            if play_again == "y":
                game += 1
                print()
                init_game()
            elif play_again == "n":
                exit()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid character!")

main()