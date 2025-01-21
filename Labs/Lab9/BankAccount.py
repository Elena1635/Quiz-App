class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self._balance += amount
                print(f"{amount} RON au fost depuși în cont.")
            else:
                print("Suma trebuie să fie pozitivă!")
        except ValueError:
            print("Introduceți o sumă validă!")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"{amount} RON au fost retrași din cont.")
            else:
                print("Fonduri insuficiente sau sumă invalidă!")
        except ValueError:
            print("Introduceți o sumă validă!")

    def get_balance(self):
        return self._balance

cont = BankAccount(1000)

while True:
    actiune = input("Alegeți acțiunea (depozit/retragere/exit): ").strip().lower()
    if actiune == "depozit":
        suma = input("Introduceți suma de depus: ")
        cont.deposit(suma)
    elif actiune == "retragere":
        suma = input("Introduceți suma de retras: ")
        cont.withdraw(suma)
    elif actiune == "exit":
        break
    else:
        print("Acțiune invalidă! Alegeți între 'depozit', 'retragere' sau 'exit'.")

    print("Sold curent:", cont.get_balance())
