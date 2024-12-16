def multiples_finder(number, limit):
    multiples = [i for i in range(1, limit + 1) if i % number == 0]
    return multiples

def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Te rog introdu un număr valid.")


number = get_valid_input("Introdu un număr:")
limit = get_valid_input("Introdu limita până la care să fie calculați multiplii:")


print(f"Multiplii numărului {number} până la limita {limit} sunt: {multiples_finder(number, limit)}")
