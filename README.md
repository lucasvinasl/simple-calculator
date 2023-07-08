# Simple Calculator
My first project developed in the basic module of the course "Python for data analysis" at DataScience Academy, a basic operations calculator.
In this calculator I used only the OS library to clean the screen at the end of operations.
The code was a little different from what the teacher developed in the course.
I implemented a stop condition using the "while" loop, as well as error handling in the divide-by-zero operation using "try except".

This code implements a basic python calculator. It allows the user to choose from various mathematical operations (sum, subtraction, multiplication and division) and perform calculations with two numbers. The program will continue to run until the user decides to leave.

Code Summary:

     The "calSOMA", calSUB, "calPROD" and "calDIV" functions are defined to perform corresponding mathematical operations: sum, subtraction, multiplication and division.
     The main code starts with a loop while the "parada" variable is 0.
         Displays available operation options.
         The user selects an operation by typing the corresponding number.
         Depending on the selected operation, the user is requested to insert two numbers.
         The calculation is performed and the result is displayed on the screen.
         If a zero division exception occurs during division operation, an error message is displayed.
         The user is requested to inform if they want to do another operation or leave.
         The "OS.System ('cls')" command is used to clean the console screen.
     When the user decides to leave, a closing message is displayed.

To execute the calculator, run the Python code. The program will start and you will be able to perform multiple mathematical operations until you decide to leave.
