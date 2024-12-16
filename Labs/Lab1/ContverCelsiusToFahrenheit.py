def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 +32
celsius = float(input("Introdu temperatura în grade Celsius:"))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C este egal cu {fahrenheit}°F. ")