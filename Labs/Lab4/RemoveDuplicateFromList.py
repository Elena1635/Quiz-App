def create_list_from_input():
    print("Introdu elementele listei, separate prin spațiu:")
    user_input = input()
    return user_input.split()

def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))  # Păstrează ordinea originală și elimină duplicatele

user_list = create_list_from_input()
unique_list = remove_duplicates(user_list)  # Elimină doar duplicatele complete, nu și literele din cuvinte

print("Lista fără duplicate în listă este:")
print(unique_list)
