import random
import sys

def init(): #simplest way i can think of to call the title to each game
    print("Guess the Number")
    print("****************")
    guess_number()

player_score = 0
computer_score = 0

def guess_number():# i guess i dont need to tab the function
    computer_guess = random.randint(1, 10)
    user_guess = int(input("Please enter a number between 1 and 10: "))
    if user_guess == computer_guess:
        print("--You win!--")
        global player_score
        player_score += 1
    else:
        print("--You lose!--")
        global computer_score
        computer_score += 1

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

    def play_again():
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == "y":
            return guess_number()
        elif choice == "n":
            print("--Thanks for playing!--")
            sys.exit()
        else:
            print("--Invalid choice. Please enter y or n.--")
            return play_again()
    play_again()

if __name__ == "__main__":
    guess_number()
