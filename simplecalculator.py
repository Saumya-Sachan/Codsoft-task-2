def perform_calculation(first_number, second_number, operation):
    if operation == "1":
        return first_number + second_number
    elif operation == "2":
        return first_number - second_number
    elif operation == "3":
        return first_number * second_number
    elif operation == "4":
        if second_number != 0:
            return first_number / second_number
        else:
            return "Error: Division by zero is not allowed."
    elif operation == "5":
        return first_number % second_number
    else:
        return "Invalid operation!"

def main():
    perm = 1
    while perm == 1:
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Remainder")

        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        operation = input("Enter the operation (1/2/3/4/5): ")
        result = perform_calculation(first_number, second_number, operation)

        if isinstance(result, str):
            print(result)  # Print error message
        else:
            print(f"The result is: {result:.3f}")

        try:
            perm = int(input("Enter 1 to continue or 0 to exit: "))
            if perm not in [0, 1]:
                print("Invalid input! Please enter 1 to continue or 0 to exit.")
                perm = 1  
        except ValueError:
            print("Invalid input! Exiting the calculator.")
            perm = 0  # Exit if invalid input

if __name__ == "__main__":
    main()