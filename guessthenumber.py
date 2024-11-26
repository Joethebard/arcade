import random
import sys
import arcadehub
import coinledger

def init(): #simplest way i can think of to call the title to each game
    print("Guess the Number")
    print("****************")
    guess_number()

player_score = 0
computer_score = 0
balance = 100

def guess_number():# i guess i dont need to tab the function
    global balance
    print(f"Your balance is ${balance}.")
    bet = input("How much do you want to bet? ")
    bet = int(bet)
    print(f"You bet ${bet}.")
    computer_guess = random.randint(1, 10)
    user_guess = int(input("Please enter a number between 1 and 10: "))
    if user_guess == computer_guess:
        print("--You win!--")
        global player_score
        player_score += 1
        balance += bet + 10
    else:
        print("--You lose!--")
        global computer_score
        computer_score += 1
        balance -= bet
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print(f"Your balance is ${balance}.")

    def play_again():
        choice = input("Do you want to play again? (y/n) \nPress A to return to the Arcade: ").lower()
        if choice == "y":
            return guess_number()
        elif choice == "n":
            print("--Thanks for playing!--")
            sys.exit()
        elif choice == "a":
            return arcadehub.main()
        else:
            print("--Invalid choice. Please enter something valid.--")
            return play_again()
    play_again()

if __name__ == "__main__":
    guess_number()
