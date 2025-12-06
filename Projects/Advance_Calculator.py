# import math

# # Function definitions
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):  # Corrected to accept two arguments
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# def square_root(x):
#     if x < 0:
#         return "Error! Cannot calculate the square root of a negative number."
#     return math.sqrt(x)

# def power(x, y):
#     return math.pow(x, y)

# def main():
#     print("Select operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Square Root")
#     print("6. Power (x^y)")
    
#     try:
#         choice = int(input("Enter your choice (1-6): "))
#     except ValueError:
#         print("Invalid input. Please enter a number.")
#         return

#     switcher = {
#         1: add,
#         2: subtract,
#         3: multiply,
#         4: divide,
#         5: square_root,
#         6: power
#     }

#     operation = switcher.get(choice)
    
#     if not operation:
#         print("Invalid choice. Please enter a number between 1 and 6.")
#         return

#     # --- KEY CHANGE: Conditional input based on choice ---
#     if choice in [1, 2, 3, 4, 6]:  # Operations needing two numbers
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             result = operation(num1, num2)
#             print(f"The result is: {result}")
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#     elif choice == 5:  # Square root needs one number
#         try:
#             num1 = float(input("Enter a number: "))
#             result = operation(num1)
#             print(f"The result is: {result}")
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

# if __name__ == "__main__":
#     main()
# import random

# target= random.randint(2,100)

# while True:
#     userChoice=int(input("guess the target: "))
#     if(userChoice==target):
#         print("success: correct guess!!")
#         break
#     elif(userChoice < target):
#         print("number is less")
#     elif(userChoice>target):
#         print("number is big")
#     else:
#         print("number is unvalid")


# print("________game over_______")
import random
import string

pass_len=8
charValues=string.ascii_letters+string.digits+string.punctuation

# res=[random.choice(charValues)for i in range(pass_len)]
# print(res)
password=" "
for i in range(pass_len):
    password+=random.choice(charValues)
print("your password:",password)
    