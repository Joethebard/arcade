import arcadehub

class CoinLedger():
    def __init__(self):
        self.balance = 100

    def check_balance(self):
        print(f"--Your balance is ${self.balance}.")
        player_choice = input("Press A to continue:").lower()
        if player_choice == "a":
            return arcadehub.welcome()
        else:
            print("Please enter A.")
            self.check_balance()
    
