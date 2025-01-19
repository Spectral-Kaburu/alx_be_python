def safe_divide(numerator, denominator):
    answer = 0.0
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        try:
            answer = numerator/denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            if answer:
                return f"The result of the division is {answer}" 
            return   
    except ValueError:
        print("Error: Please enter numeric values only.")
    