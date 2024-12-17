def create_tuple_from_input():
    print("Introdu elementele tuplului, separate prin spațiu:")
    user_input = input()
    tuple_elements = tuple(user_input.split())  
    return tuple_elements

def search_in_tuple(tpl, element):
    if element in tpl:
        return tpl.index(element)
    else:
        return -1

my_tuple = create_tuple_from_input()

print("Introdu elementul pe care dorești să îl cauți:")
search_element = input()

position = search_in_tuple(my_tuple, search_element)

if position != -1:
    print(f"Elementul '{search_element}' a fost găsit în tuplu la poziția {position}.")
else:
    print(f"Elementul '{search_element}' nu se află în tuplu.")
