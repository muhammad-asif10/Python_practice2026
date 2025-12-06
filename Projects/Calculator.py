# Function definitions remain correct
def add(x, y, z):
    return x + y + z

def subtract(x, y, z):
    return x - y - z


def multiply(x, y, z):
    return x * y * z

def divide(x, y, z):
    # Added a check to prevent division by zero
    if y == 0:
        return "Error! Division by zero."
    return (x / y)/z

def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get the user's choice and convert it to an integer
    # The input() function gets the user's input as a string
    try:
        choice = int(input("Enter your choice (1, 2, 3, 4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return # Exit the function if the input is not a number

    # Get the two numbers for the calculation
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3=float(input("Enter third number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return # Exit the function if the input is not a number

    # Using the switcher dictionary to select the correct function
    switcher = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide
    }

    # Get the function from the switcher dictionary
    operation = switcher.get(choice)

    if operation:
        # Call the selected function with the two numbers and print the result
        result = operation(num1, num2, num3)
        print(f"The result is: {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

# This line calls the main function to run the program
if __name__ == "__main__":
    main()