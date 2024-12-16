def is_palindrome(text):
    text = ''.join(c for c in text if c.isalnum()).lower()
    return text == text[::-1]

user_input = input("Introduceti un cuvant sau o fraza pentru a verifica daca este palindrom: ")

if is_palindrome(user_input):
    print("Este un palindrom!")
else:
    print("Nu este un palindrom.")



