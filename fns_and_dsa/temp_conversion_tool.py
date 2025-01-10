# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = input("Enter the temperature to convert:" )
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if unit == "F":
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is equivalent to {celsius:.2f}°C.")
        elif unit == "C":
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equivalent to {fahrenheit:.2f}°F.")
        else:
            raise ValueError("Invalid temperature format. Please use 'C' or 'F' at the end.")

    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value followed by 'C' or 'F'.")

# Entry point of the script
if __name__ == "__main__":
    main()
