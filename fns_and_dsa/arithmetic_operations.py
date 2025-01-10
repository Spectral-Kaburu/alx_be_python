def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "divide":
            if num2 == 0:
                print("Invalid input. You cannot divide by 0.")
                pass
            elif num2 != 0:
                return num1 / num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        
def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation to be performed ('add', 'subtract', 'divide', 'multiply': )")
    perform_operation(num1, num2, operation)

if __name__ == "__main__":
    main()
    