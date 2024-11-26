import random
import sys
import arcadehub

def init(ledger): #simplest way i can think of to call the title to each game
    print("Guess the Number")
    print("****************")
    guess_number(ledger)

player_score = 0
computer_score = 0

def guess_number(ledger):# i guess i dont need to tab the function
    print(f"Your balance is ${ledger.balance}.")
    try:
        bet = int(input("How much do you want to bet? "))
    except ValueError:
        print("--That's not a number...--")
        return guess_number(ledger) 
    if bet > ledger.balance:
        print("--You're too broke to make that bet...--")
        return guess_number(ledger)
    elif bet <= 0:
        print("--You can't bet nothing...--")
        return guess_number(ledger)
    else:
        print(f"You bet ${bet}.")

        computer_guess = random.randint(1, 10)
        user_guess = int(input("Please enter a number between 1 and 10: "))
        if user_guess == computer_guess:
            print("--You win!--")
            global player_score
            player_score += 1
            ledger.balance += bet * 10
        else:
            print("--You lose!--")
            global computer_score
            computer_score += 1
            ledger.balance -= bet
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print(f"Your balance is ${ledger.balance}.")

    def play_again(ledger):
        choice = input("Do you want to play again? (y/n) \nPress A to return to the Arcade: ").lower()
        if choice == "y":
            return guess_number(ledger)
        elif choice == "n":
            print("--Thanks for playing!--")
            sys.exit()
        elif choice == "a":
            return #arcadehub.main()
        else:
            print("--Invalid choice. Please enter something valid.--")
            return play_again(ledger)
    play_again(ledger)

if __name__ == "__main__":
    guess_number()
