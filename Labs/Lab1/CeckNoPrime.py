def este_numar_prim(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

numar = int(input("Introduceți un număr pentru a verifica dacă este prim:"))
if este_numar_prim(numar):
    print(f"{numar} este număr prim.")
else:
    print(f"{numar} nu este un număr prim.")