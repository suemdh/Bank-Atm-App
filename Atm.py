class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    
    def check_balance(self):
        print("Your balance is 30000")
    
    def cash_withdrawal(self, amount):
        new_amount = 100-amount
        print("You withdrawed" + str(amount) +  " Your new amount is " + str(new_amount))

def main():
    name = input("Hello, what is your name")
    print("Hello, " + name)
    cardNumber = input("Enter your card number")
    pin = input("Enter your pin")
    new_User = Atm(cardNumber, pin)

    print("Choose your activity")
    print("1. Checking Balance")
    print("2. Cash Withdrawal")
    activity = int(input("Enter your activity choice: "))

    if (activity == 1):
        new_User.check_balance()
    
    elif (activity == 2):
        amount = int(input("Enter how much money you want to withdraw: "))
        new_User.cash_withdrawal(amount)
    else:
        print("Please Enter a valid number(1 and 2 only)")

if __name__ == "__main__":
     main()
