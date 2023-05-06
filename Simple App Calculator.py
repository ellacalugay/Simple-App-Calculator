# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #5 | Simple App Calculator

#Pseuodocode
# Create a while loop with a True condition.
while True:
    try:
        # Ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division).
        operation = str(input("Please choose among the four operation - Addition, Subtraction, Multiplication, Division: "))

        # Ask the user for two numbers
        print("Kindly input two numbers.")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Initizalize result variable.
        result = ()

        # Perform the calculation based on the operation that the user wants
        if operation == "Addition":
            # If the operation is Addition, add the two numbers.
            result = num1 + num2
        elif operation == "Subtraction": 
            # If the operation is Subtraction, subtract the second number from the first number
            result = num1 - num2
        elif operation == "Multiplication": 
            # If the operation is Multiplication, multiply the two numbers.
            result = num1 * num2
        elif operation == "Division": 
            # If the operation is Division, divide the first number by the second number.
            result = num1 / num2
        else:
            print("Invalid Operation")
            result = None
        # Display the result
        if result is not None:
            print("Results:", result)
            print("Operation completed.")

        # Ask if the user wants to try again or not.
        # If yes, repeat the process.
        try_again = input("Do you want to try again? (yes/no): ")
        # If no, Display “Thank you!” and exit the program.
        if try_again == "no":
            print("Thank you.")
            break # exit the loop

    #Use Python Function and appropriate Exceptions to capture errors during runtime.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero value for the second number.")