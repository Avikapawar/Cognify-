# Task: Temperature Conversion
# Create a Python program that converts
# temperatures between Celsius and
# Fahrenheit. Prompt the user to enter a
# temperature value and the unit of
# measurement, and then display the
# converted temperature.

temperature = float(input("Enter the Temperature: "))
unit = input("Enter the Unit (Celsius (c) or Fahrenheit (f)): ")

def celsius(temp):
    f = temp * (9/5) + 32
    print(f"Celsius to Fahrenheit:{f}F", )

def fahrenheit(temp):
    c = (temp - 32) * (5/9)
    print(f"Fahrenheit to Celsius:{c}C")

if unit.lower() == "c":
    celsius(temperature)
elif unit.lower() == "f":
    fahrenheit(temperature)
else:
    print("Invalid unit")