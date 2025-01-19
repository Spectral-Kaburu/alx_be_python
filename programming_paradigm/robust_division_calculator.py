def safe_divide(numerator, denominator):
    answer = 0.0
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        try:
            answer = numerator/denominator
            return f"The result of the division is {answer}" 
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    