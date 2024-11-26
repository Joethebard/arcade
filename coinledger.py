import arcadehub
import os
import json

class CoinLedger():
    def __init__(self):
        self.save_file = "balance.json"
        self.balance = self.load_balance()  

    def load_balance(self):
        try:
            if os.path.exists(self.save_file):
                with open(self.save_file, "r") as file:
                    data = json.load(file)
                    return data.get("balance", 100)
            return 100
        except FileNotFoundError:
            return 100
        
    def save_balance(self):
        with open(self.save_file, "w") as file:
            json.dump({"balance": self.balance}, file)

    def check_balance(self):
        print(f"--Your balance is ${self.balance}.")
        player_choice = input("Press A to continue:").lower()
        if player_choice == "a":
            return #arcadehub.main()
        else:
            print("Please enter A.")
            self.check_balance()
    
