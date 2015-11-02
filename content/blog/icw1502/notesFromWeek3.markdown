Title: Notes from Week 3
Date: 2015-10-3 08:00
Modified: 2015-10-03 08:00
Tags: iOS, swift, icw1502
Summary: Notes from Week 3

## What we learned this week

Today we covered Chapter 3 and 4 of our text book:


* let
* var
* Type inference
* Numeric Types
* nil
* Higher Order functions
* Type Alias
* Collections
* Enumeration
* Value types and Reference Types
* Dictionaries
* Optionals in Dictionaries
* guard
* if let

## Homework

* We skipped a few sections. Read the book upto the end of Chapter 4
* Test out inout and var parameters with brother/secondSon
* Create a function called 'double' that takes in an integer and returns that integer multiplied by 2
* Create a similar function called square that squares the input
* Create a similar function called factorial that returns the factorial of the input
* EXTRA CREDIT: Create two factorial functions - One that works recursively and one that works iteratively (with a loop)
* Create an array of your functions

Create another function called performOperations that takes in a list of functions like you created, and a list of numbers. The function should call each operation on each number and print out the value

Run performOperations like this: 

    let operations = [double, square, factorialRecursive, factorialIterative]

    performOperations(operations, onNumbers: [0, 1, 2, 3])

    // This should print: 
    0 => 0
    0 => 0
    0 => 0
    0 => 0
    --
    1 => 2
    1 => 1
    1 => 1
    1 => 1
    --
    2 => 4
    2 => 4
    2 => 2
    2 => 2
    --
    3 => 6
    3 => 9
    3 => 6
    3 => 6
    --

Create a function called createMultiplierWithOperand that takes in one Integer named 'operand'. This function should return a function that takes in an Integer and returns that Integer multiplied by 'operand'.  For example: 

    let treble = createMultiplierWithOperand(3)
    
    let newOps = [double, treble, square]
    performOperations(newOps, onNumbers: [3, 5, 9])
    
    This prints: 
    3 => 6
    3 => 9
    3 => 9
    --
    5 => 10
    5 => 15
    5 => 25
    --
    9 => 18
    9 => 27
    9 => 81
    --
