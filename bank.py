class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self._accountNumber = accountNumber
        self._accountHolder = accountHolder
        self._balance = initialBalance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount:.2f} to account {self._accountNumber}. New balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew ${amount:.2f} from account {self._accountNumber}. New balance: ${self._balance:.2f}")
            else:
                print("Insufficient balance for the withdrawl.")
        else:
            print("Withdrawal amount must be positive.")

    def getBalance(self):
        return self._balance
        
    def displayAccountInfo(self):
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Holder: {self._accountHolder}")
        print(f"Current Balance: ${self._balance:.2f}")


#demonstrate the use of Bank account class
def main():
    #bank account objects
    account1 = BankAccount("123456789", "Erica", 10000.00)
    account2 = BankAccount("1000553974", "Ari", 1200.00)

    #Account info and current balance
    account1.displayAccountInfo()
    account2.displayAccountInfo()

    #Deposits
    account1.deposit(500.00)
    account2.deposit(100.00)

    account1.withdraw(1000.00)
    account2.withdraw(1500.00) #insufficient funds

    account1.displayAccountInfo()
    account2.displayAccountInfo()


if __name__ == "__main__":
    main()

            



        