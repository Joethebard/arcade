import sys

class CoinLedger:
    def __init__(self):
        self.balance = 100

    def check_balance(self):
        print(f"--Your balance is ${self.balance}.")
        player_choice = input("Press A to return to the Arcade:").lower()
        if player_choice == "a":
            return True
        else:
            print("Please enter A.")
            return False
    

if __name__ == "__main__":
    ledger = CoinLedger()
    ledger.check_balance()
