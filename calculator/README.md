# Calculator

A simple calculator that performs basic arithmetic operations.

## Features
- Addition (+)
- Subtraction (-)
- Multiplication (×)
- Division (÷)
- Handles division by zero (error message, no crash)
- Input validation for invalid choices

## How to run

```bash
python calculator.py

Welcome to the Simple Calculator!
Please select an operation:
1. Add
2. Subtract
3. Multiply
4. Divide

Enter your choice (1/2/3/4): 1
Enter first number: 10
Enter second number: 5
The result of 10.0 + 5.0 is: 15.0

Error handling
Division by zero: Displays "Error: Division by zero is not allowed"

Invalid choice: Displays "Invalid choice! Please select a valid operation"

What I learned
- Writing functions in Python (def, return)

- User input handling with input()

- Converting strings to numbers with float()

- Conditional statements (if/elif/else)

- Using while loops for repetition

- Error handling for edge cases (division by zero)

calculator.py
├── Add()         # Addition function
├── Subtract()    # Subtraction function
├── Multiply()    # Multiplication function
├── Divide()      # Division function (with zero check)
└── Main loop     # Menu + user interaction
