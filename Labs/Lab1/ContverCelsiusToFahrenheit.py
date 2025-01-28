"""
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 +32
celsius = float(input("Introdu temperatura în grade Celsius:"))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C este egal cu {fahrenheit}°F. ")
"""
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def get_float_input(mesaj):
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Eroare: Te rog să introduci un număr valid!")

celsius = get_float_input("Introdu temperatura în grade Celsius: ")
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C este egal cu {fahrenheit:.2f}°F.")
