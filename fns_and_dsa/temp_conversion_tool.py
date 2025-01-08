FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp = float(input("Enter the temperature today: "))
    choice = input("Is the temperature you entered in Celcius(C) or Fahrenheit(F)??? (C/F)").upper()
    try:
        match choice:
            case "F":
                cel = convert_to_celsius(temp)
                print(f"{temp}°F is {cel}°C")

            case "C":
                fah = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {fah}°F")

    except ValueError as e:
        print(e)
        print("Invalid temperature. Please enter a numeric value.")
    
if __name__ == "__main__":
    main()

