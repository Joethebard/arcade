import random
import time
import sys

def init(): #simplest way i can think of to call the title to each game(i think)
    print("Rock, Paper, Scissors")
    print("*********************")
    playrps()

class RPS:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

player_score = 0
computer_score = 0

def playrps():# i guess i dont need to tab the function
    user_choice = input("Enter your choice... \n1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return playrps()
    
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
    elif "--You lose!--" in result:
        global computer_score
        computer_score += 1

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    decide_winner(user_choice, computer_choice)

    
    def play_again():
        player_choice = input("Do you want to play again? (y/n): ").lower()
        if player_choice == "y":
            return playrps()
        elif player_choice == "n":
            print("--Thanks for playing!--")
            sys.exit()
        else:
            print("--Invalid choice. Please enter y or n.--")
            return play_again()
    play_again()

if __name__ == "__main__":
    playrps()

