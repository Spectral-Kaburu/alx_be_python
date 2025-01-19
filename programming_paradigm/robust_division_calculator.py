def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        try:
            answer = numerator/denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    return f"The result of the division is {answer}"
