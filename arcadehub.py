import rps
import guessthenumber
import sys
import coinledger

print("Welcome to the Arcade!")
print("**********************")

def main():
    ledger = coinledger.CoinLedger()
    print("What would you like to play?")
    print("1. Rock, Paper, Scissors")
    print("2. Guess the Number")
    print("3. Exit")
    print("4. Check Balance")
    choice = input("Enter your choice: 1, 2, 3 or 4: ")
    if choice == "1":
        rps.init()
    elif choice == "2":
        guessthenumber.init()
    elif choice == "3":
        print("Thanks for playing!")
        sys.exit()
    elif choice == "4":
        ledger.check_balance()
    else:
        print("Invalid choice. Please enter a valid option.")
        main()
main()

if __name__ == "__main__":
    ledger = coinledger.CoinLedger()
    ledger.check_balance()