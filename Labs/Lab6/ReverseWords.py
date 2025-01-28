def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

sentence = input("Introduceți propoziția: ")
output = reverse_words(sentence)

print("Propoziția inversată:", output)