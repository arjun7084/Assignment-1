def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit

while True:
    print("\nWelcome To Temperature Converter:")
    print("Chose The Operator:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")

    choice = input("Enter the choice [1,2,3]: ")
    if choice == "1":
        fahrenheit= float(input('Fahrenheit temperature: '))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    elif choice=="2":
        celsius =float(input('Celcius temperature: '))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Please enter valid choice. ")