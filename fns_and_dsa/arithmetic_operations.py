def perform_operation(num1, num2, operation):
    eq = str(num1) + operation + str(num2)
    match operation:
        case "add":
            eq = str(num1) + "+" + str(num2)
            return eval(eq)
        case "divide":
            if num2 == 0:
                print("Invalid input. You cannot divide by 0.")
                pass
            else:
                eq = str(num1) + "/" + str(num2)
                return eval(eq)
        case "subtract":
            eq = str(num1) + "-" + str(num2)
            return eval(eq)
        case "multiply":
            eq = str(num1) + "*" + str(num2)
            return eval(eq)
        
def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation to be performed ('add', 'subtract', 'divide', 'multiply': )")
    perform_operation(num1, num2, operation)

if __name__ == "__main__":
    main()
    