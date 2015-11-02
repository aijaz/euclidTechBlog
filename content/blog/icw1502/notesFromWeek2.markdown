Title: Notes from Week 2
Date: 2015-09-28 08:00
Modified: 2015-09-28 08:00
Tags: iOS, swift, icw1502
Summary: Notes from Week 2

## What we learned this week

This week we covered Chapter 2 of our book, Functions. Specifically, we learned: 

* How to create simple functions with zero or more parameters, and variadic parameters
* How to overload functions
* How to specify local and external labels for function parameters
* How to return single values and anonymous and named tuples from functions

## The Book

As I mentioned last week, we will be using Daniel Steinberg's [A Swift Kickstart][9] as our text book for this course. 

## The Plan for the next few weeks

* Week 3: Chapters 3, 4, and 5
* Week 4: Chapters 6 and 7
* Week 5: Chapters 8 and 9
* Week 6 and later: We'll work on our main iOS project

## Homework

* Complete last week's homework
* Write a function called `carDescription`. It should take the following parameters: 
* `make` - a String. Even though this is the first parameter, its name should be required.
* `model` - a String
* `color` - a String
* `numberOfDoors` - an Int
* `accessories` - zero or more Strings separated by a comma
* This function should return a tuple containing two members: `numberOfAccessories` (and Int) and `description` (a String)
* `numberOfAccessories`, obviously, is the number of accessories that were passed in
* If no accessories were passed in, `description` should be "COLOR N-door MAKE MODEL with no accessories", where COLOR, N, MAKE, and MODEL are the parameters that were passed in. 
* If one or more accessories were passed in, `description` should have multiple lines of text.
* The first line should be "COLOR N-door MAKE MODEL with the following accessories:"
* Each additional line should start with two spaces and then contain the name of an accessory
* If numberOfDoors is not passed in, it should be assumed that there are four doors.

See below for examples
    
    // The print() function accepts a parameter named "terminator". 
    // This is a string that will be printed after all parameters 
    // are printed. The default value of this is "\n" - the 
    // newline character.
    
    let d1 = carDescription(make: "Toyota", 
                            model: "Corolla", 
                            color: "Black", 
                            accessories: "Anti-lock brakes")
    print(d1.numberOfAccessories, terminator: "\n----\n")
    
    
    let d2 = carDescription(make: "Ford", 
                            model: "Focus", 
                            color: "Red", 
                            numberOfDoors: 2)
    print(d2, terminator: "\n----\n")
    
    
    let d3 = carDescription(make: "Honda", 
                            model: "Accord", 
                            color: "White", 
                            accessories: "Anti-lock brakes", 
                                         "Fog lights", 
                                         "Remote Starter")
    print(d3.descriptionText)

    // ------------------------------------------------
    // This should print out the following to console: 
    // 1
    // ----
    // (0, "Red 2-door Ford Focus with no accessories")
    // ----
    // White 4-door Honda Accord with the following accessories:
    //   Anti-lock brakes
    //   Fog lights
    //   Remote Starter

[9]: https://itunes.apple.com/ch/book/a-swift-kickstart/id891801923?isInPurchasedView=true&l=en&mt=11
