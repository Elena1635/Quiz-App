import string
def word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

text = input("Introduceti un text: ")
result = word_frequency(text)

print("Frecvența cuvintelor:")
for word, frequency in result.items():
    print(f"{word}: {frequency}")
