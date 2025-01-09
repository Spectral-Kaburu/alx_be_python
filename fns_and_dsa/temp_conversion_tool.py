# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
def main():
    try:
        # Prompt the user to enter the temperature and its unit
        temp_input = input("Enter the temperature (e.g., 98.6F or 37C): ").strip().upper()

        # Determine the unit and convert accordingly
        if temp_input.endswith("F"):
            fahrenheit = float(temp_input[:-1])  # Extract the numeric part
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C.")
        elif temp_input.endswith("C"):
            celsius = float(temp_input[:-1])  # Extract the numeric part
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F.")
        else:
            raise ValueError("Invalid temperature format. Please use 'C' or 'F' at the end.")

    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value followed by 'C' or 'F'.")

# Entry point of the script
if __name__ == "__main__":
    main()
