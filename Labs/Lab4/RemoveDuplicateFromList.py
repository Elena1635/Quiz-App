def create_list_from_input():
    print("Introdu elementele listei, separate prin spațiu:")
    user_input = input()
    return user_input.split()

def remove_duplicates_from_word(word):

    return ''.join(sorted(set(word), key=word.index))

def remove_duplicates(input_list):

    return list(dict.fromkeys(input_list))

user_list = create_list_from_input()

user_list_no_duplicates_in_words = [remove_duplicates_from_word(word) for word in user_list]

unique_list = remove_duplicates(user_list_no_duplicates_in_words)

print("Lista fără duplicate în cuvinte și în listă este:")
print(unique_list)
