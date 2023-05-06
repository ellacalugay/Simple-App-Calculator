# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #5 | Simple App Calculator

#Pseuodocode
# Ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division).
operation = str(input("Please choose among the four operation - Addition, Subtraction, Multiplication, Division: "))
# Ask the user for two numbers
print("Kindly input two numbers.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Perform the calculation based on the operation that the user wants
if operation == "Addition":
    # If the operation is Addition, add the two numbers.
    result = num1 + num2
# Display the result
# Ask if the user wants to try again or not.
# If yes, repeat the process.
# If no, Display “Thank you!” and exit the program.
# Use Python Function and appropriate Exceptions to capture errors during runtime.