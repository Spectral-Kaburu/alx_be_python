def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            print("Error: Cannot divide by zero.")
        else:
            answer = numerator / denominator
            print(f"The result of the division is {answer}")
    except ValueError:
        print("Error: Please enter numeric values only.")
