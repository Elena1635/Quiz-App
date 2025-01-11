def run_length_encoding(text):
    if not text:
        return ""

    # Inițializăm variabilele pentru compresie
    encoded = []
    count = 1

    # Parcurgem șirul de caractere
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            # Dacă caracterul curent este același ca precedentul, incrementăm count
            count += 1
        else:
            # Dacă caracterul curent diferă, adăugăm caracterul și numărul de apariții
            encoded.append(f"{text[i - 1]}{count}")
            count = 1  # Resetăm count

    # Adăugăm ultimul caracter și numărul de apariții
    encoded.append(f"{text[-1]}{count}")

    # Combinăm lista într-un singur șir și returnăm
    return "".join(encoded)

# Solicitare șir de la utilizator
text = input("Introduceți un șir de caractere: ")
output = run_length_encoding(text)
print(output)
