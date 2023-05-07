# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #5 | Simple App Calculator

# ASCII art for the header with ANSI escape codes for color
print(("\033[38;5;218m" + """
 _____________________
|  _________________  |
| |  Simple      0. | |
| |     Calculator  | |
| |           App   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""+ "\033[0m"))

# Import the necessary module 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Initialize tkinter app
root = tk.Tk()
root.title("Simple Calculator")
root.configure(background='pink')

# Set style
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))

# Create widgets
label_header = tk.Label(root, text="Simple Calculator App", font=('Helvetica', 16, 'bold'), bg='light blue')
label_header.pack(pady=10)

# Create a frame to contain input widgets
frame_input = ttk.Frame(root)
frame_input.pack(pady=15)

# Create a label for the operation dropdown 
label_operation = ttk.Label(frame_input, text="Choose an operation:", foreground="black", background="light coral", font=(20))
label_operation.grid(row=0, column=0, padx=5)

# Create a combobox for the operation dropdown and ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division).
combo_operation = ttk.Combobox(frame_input, values=["Addition", "Subtraction", "Multiplication", "Division"])
combo_operation.grid(row=0, column=1, padx=5)

# Create a label and entry for the first number input
label_num1 = ttk.Label(frame_input, text="First number:", foreground='gold', background="maroon")
label_num1.grid(row=1, column=0, padx=5)
entry_num1 = ttk.Entry(frame_input)
entry_num1.grid(row=1, column=1, padx=5)

# Create a label and entry for the second number input
label_num2 = ttk.Label(frame_input, text="Second number:", foreground='gold', background="maroon")
label_num2.grid(row=2, column=0, padx=5)
entry_num2 = ttk.Entry(frame_input)
entry_num2.grid(row=2, column=1, padx=5)

#Pseuodocode
# Create a while loop with a True condition.
while True:
    try:
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
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Simple App Calculator.")