import random

def number_guessing_game():
    number = random.randint(1, 100)
    print("Ghicește numărul între 1 și 100")

    while True:
        try:
            guess = int(input("Introdu numărul: "))
            if guess < number:
                print("Prea mic")
            elif guess > number:
                print("Prea mare")
            else:
                print(f"Corect! Numărul a fost: {number}")
                break
        except ValueError:
            print("Te rog introdu un număr valid.")

number_guessing_game()
