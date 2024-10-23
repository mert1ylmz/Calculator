# Calculator
A Calculator With Simple GUI With Python And customtkinter
# Calculator Application

This is a simple calculator application built using Python's `tkinter` and `customtkinter` libraries. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- **Basic Arithmetic Operations**: Perform addition, subtraction, multiplication, and division.
- **Dark Mode Appearance**: Uses `customtkinter` to create a modern dark-themed interface.
- **Clear Functionality**: Allows clearing the input field.
- **Error Handling**: Displays "Error" when an invalid expression is entered.

## Requirements

To run this application, you need the following libraries:
- `tkinter` (standard Python library)
- `customtkinter` (must be installed separately)

### Installing `customtkinter`

To install `customtkinter`, you can use:

```bash
pip install customtkinter
How to Run
Ensure you have Python installed on your system.

Install the required dependencies using the above command.

Run the script:

bash
Kodu kopyala
python calculator.py
Make sure to replace calculator.py with the actual filename if it's different.

Code Overview
The application has the following key components:

App Initialization: The main app window is created with customtkinter.CTk(), set to a fixed size and made non-resizable.
Functions:
clickbutton(item): Updates the expression when a button is clicked.
clearbutton(): Clears the current expression.
equalsbutton(): Evaluates the expression and displays the result.
Input Frame: A frame containing an entry widget to display the current expression or result.
Button Frame: A frame containing all the calculator buttons.
