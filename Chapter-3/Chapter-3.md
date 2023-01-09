# 1. Why are functions advantageous to have in your programs?
Functions are like mini programs inside a program. A major job of the function is to group code that gets run multiple times.


# 2. When does the code in a function execute: when the function is defined or when the function is called?
The code in a function is executed when the function is called. The pointer first checks if the function is defined or not and if it is, it goes to the function call part and if the function is called the function gets executed.


# 3. What statement creates a function?
`def <function_name>(parameters):` creates a function.


# 4. What is the difference between a function and a function call?
function is already defined and it has some computation to it where as function call is the part where we call the function's name to run it.


# 5. How many global scopes are there in a Python program? How many local scopes?
There is one global scope and local scope. 


# 6. What happens to variables in a local scope when the function call returns?
When the function call returns the local scope variables are destroyed and all the values are forgotten.


# 7. What is a return value? Can a return value be part of an expression?
The value that a function call evaluates to is called the return value of the function. When an expression is used with a return statement, the return value is what this expression evaluates to.                                      


# 8. If a function does not have a return statement, what is the return value of a call to that function?
If a function does not have a return statement, the return value of that function call returns `None`.


# 9. How can you force a variable in a function to refer to the global variable?
We can add a global statement which will force a funtion to refer to the global value without creating a local variable.


# 10. What is the data type of None?
The datatype of None is NoneType.


# 11. What does the import areallyourpetsnamederic statement do?
It will import all the functions inside the module areallyourpetsnamederic.


# 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
To use the function we need to do spam.bacon()


# 13. How can you prevent a program from crashing when it gets an error?
To prevent a program from crashing when it gets an error we use the try-except statement.


# 14. What goes in the try clause? What goes in the except clause?
The code that could potentially crash is put in the try clause and and in the except clause we give the error to look out for. When an error is caught in the try clause the execution immediately moves to the try clause and after that the code execution continues as normal.

# PROJECT
[The collatz sequence](https://github.com/Aaryanajith/amFOSS-Python/blob/main/Chapter-3/The_Collatz_Sequence.py)
