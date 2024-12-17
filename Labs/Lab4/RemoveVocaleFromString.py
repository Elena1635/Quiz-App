def remove_vowels(input_string):
    vowels = "aeiouăîâAEIOUĂÎÂ"
    result = ''.join([char for char in input_string if char not in vowels])
    return result

user_input = input("Introdu un șir de caractere: ")

output_string = remove_vowels(user_input)

print("Șirul fără vocale este:")
print(output_string)
