def safe_divide(numerator, denominator):
    answer = 0.0
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        answer = numerator/denominator
        if ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {answer}" 
    except ValueError:
        print("Error: Please enter numeric values only.")
    