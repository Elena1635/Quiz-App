def run_length_encoding(text):
    if not text:
        return ""
    encoded = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(f"{text[i - 1]}{count}")
            count = 1

    encoded.append(f"{text[-1]}{count}")

    return "".join(encoded)

text = input("Introduceți un șir de caractere: ")
output = run_length_encoding(text)
print(output)