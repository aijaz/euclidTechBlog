Title: Notes from Week 6
Date: 2015-10-25 16:00
Modified: 2015-10-25 16:00
Tags: iOS, swift, icw1502
Summary: Notes from Week 6

## Table of Contents

* [Playgrounds uploaded to GitHub](#toc1)
* [What we learned this week](#toc2)
* [Week 6 Homework Assignment](#toc3)

## <a name="toc1"></a>Playgrounds uploaded to GitHub

The Week 6 Homework playground, as well as what we did in class have been uploaded to our [class GitHub page](https://github.com/aijaz/icw1502).

## <a name="toc2"></a>What we learned this week

This week we learned about Structs. We leard how to create them, and how to add computed properties and methods. We learned about custom getters and setters and also about `willSet` and `didSet`. We implemented the 'CustomStringConvertible' and 'Equatable' protocols. We looked at access levels and learned how to compose complex structs out of simpler structs. 

## <a name="toc3"></a>Week 6 Homework

First, read the book up to the end of Chapter 7

Now, the coding homework. The code you write for this homework will be used in our iOS project, so make sure you complete the assignment.

* Create a struct called `Item`. It should have the following properties: 
    * itemID : Int
    * name : String
    * manufacturer: String, optional
    * dateBought: NSDate (You will need to import 'Foundation' to get this), optional
    * valueWhenBought: Int (in cents), optional
    * currentValue: Int (in cents)
    * picture: UIImage: (You will need to import 'UIKit' to get this), optional
    * serialNumber: String, optional
    * productURL: NSURL, optional
    * notes: String, optional

* Create a struct called `ItemDataSource`. It should have the following properties: 
    * items: An array of `Item`s.
    
* Give `ItemDataSource` the following methods: 
    * itemAtIndex - This should take one parameter that's an Int and it should return an Item that's the appropriate item in the `items` array. If the Int passed in is less than zero or too large, then it should throw a NegativeNumberException or NumberTooLargeException. Look at your notes from week 5 ('Enums') to refresh your memory.

* Have `Item` conform to `CustomStringConvertible`
    * Let the `description` of an `Item` be the value of the `Name` property.



   



