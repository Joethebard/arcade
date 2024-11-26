import rps
import guessthenumber
import coinledger
import sys
import os

def welcome():
    print("Welcome to the Arcade!")
    print("**********************")
    main()

def main():
    ledger = coinledger.CoinLedger()
    while True:
        print("What would you like to play?")
        print("1. Rock, Paper, Scissors")
        print("2. Guess the Number")
        print("3. Exit")
        print("4. Check Balance")
        choice = input("Enter your choice: 1, 2, 3 or 4: ")
        if choice == "1":
            rps.init(ledger)
        elif choice == "2":
            guessthenumber.init(ledger)
        elif choice == "3":
            print("Thanks for playing!")
            if os.path.exists(ledger.save_file):
                os.remove(ledger.save_file)
            sys.exit()
        elif choice == "4":
            ledger.check_balance()
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

if __name__ == "__main__":
    welcome()
