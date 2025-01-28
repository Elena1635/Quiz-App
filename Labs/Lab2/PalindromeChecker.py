def is_palindrome(text):
    text = ''.join(c for c in text if c.isalnum()).lower()
    if not text:  # Verificăm dacă șirul curățat este gol
        return False
    return text == text[::-1]

user_input = input("Introduceți un cuvânt sau o frază pentru a verifica dacă este palindrom: ")

if is_palindrome(user_input):
    print("Este un palindrom!")
else:
    print("Nu este un palindrom.")