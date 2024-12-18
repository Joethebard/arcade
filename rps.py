import random
import time
import sys
import arcadehub

def init(ledger): #simplest way i can think of to call the title to each game(i think)
    print("Rock, Paper, Scissors")
    print("*********************")
    play_rps(ledger)

class RPS:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

player_score = 0
computer_score = 0

def play_rps(ledger):# i guess i dont need to tab the function
    print(f"Your balance is ${ledger.balance}.")
    try:
        bet = int(input("How much do you want to bet? "))
    except ValueError:
        print("--That's not a number...--")
        return play_rps(ledger)
    if bet > ledger.balance:
        print("--You're too broke to make that bet...--")
        return play_rps(ledger)
    elif bet <= 0:
        print("--You can't bet nothing...--")
        return play_rps(ledger)
    

    user_choice = input("Enter your choice... \n1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return play_rps(ledger)
    
    user_choice = int(user_choice)
    computer_choice = random.choice([RPS.ROCK, RPS.PAPER, RPS.SCISSORS])


    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    def decide_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "--It's a tie!--"
        elif (user_choice == RPS.ROCK and computer_choice == RPS.SCISSORS) or (user_choice == RPS.PAPER and computer_choice == RPS.ROCK) or (user_choice == RPS.SCISSORS and computer_choice == RPS.PAPER):
            return "--You win!--"
        else:
            return "--You lose!--"
        
    result = decide_winner(user_choice, computer_choice)
    print(result)

    if "--You win!--" in result:
        global player_score
        player_score += 1
        ledger.balance += bet * 2
    elif "--You lose!--" in result:
        global computer_score
        computer_score += 1
        ledger.balance -= bet
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print(f"Your balance is ${ledger.balance}.")
    decide_winner(user_choice, computer_choice)

    
    def play_again(ledger):
        player_choice = input("Do you want to play again? (y/n) \nPress A to return to the Arcade: ").lower()
        if player_choice == "y":
            return play_rps(ledger)
        elif player_choice == "n":
            print("--Thanks for playing!--")
            sys.exit()
        elif player_choice == "a":
            return #arcadehub.main()
        else:
            print("--Invalid choice. Please enter something valid.--")
            return play_again(ledger)
    play_again(ledger)

if __name__ == "__main__":
    play_rps()
    arcadehub.main()

