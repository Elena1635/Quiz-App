def unique_pair_sum(numbers, target):
    result = set()
    seen = set()

    for num in numbers:
        complement = target - num

        if complement in seen:
            result.add(tuple(sorted((num, complement))))
        seen.add(num)

    return result

def get_input():
    while True:
        try:
            user_input = input("Introduceti numerele, separate prin spatiu: ")

            if len(user_input.split()) < 2:
                print("Eroare: Trebuie să introduci cel puțin două numere.")
                continue

            numbers = [int(x) for x in user_input.split()]

            target = int(input("Introduceti valoarea tinta: "))

            return numbers, target
        except ValueError:
            print("Eroare: Introduceti doar numere intregi. Incercati din nou!")

numbers, target = get_input()

result = unique_pair_sum(numbers, target)

if result:
    print("Perechile unice care adunate dau valoarea țintă sunt:")
    for pair in result:
        print(pair)
else:
    print("Eroare: Nu există perechi de numere care să dea valoarea țintă.")
