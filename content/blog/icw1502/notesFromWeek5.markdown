Title: Notes from Week 5
Date: 2015-10-20 09:00
Modified: 2015-10-20 09:00
Tags: iOS, swift, icw1502
Summary: Notes from Week 5

## Table of Contents

* [Playgrounds uploaded to GitHub](#toc1)
* [What we learned this week](#toc2)
* [Week 5 Homework Assignment](#toc3)

## <a name="toc1"></a>Playgrounds uploaded to GitHub

The Week 5 Homework playground, as well as what we did in class have been uploaded to our [class GitHub page](https://github.com/aijaz/icw1502).

## <a name="toc2"></a>What we learned this week

This week we covered Chapter 6 from our text book: Enumerations. We learned how to create enumerations and use them in switch statements. Then we added methods to our enums. We also converted those methods to computed statements. We looked at different types of raw values and associated values and how to bind to those associated values. Finally, we examined what it means for enums to be value types and looked at option sets.  

## <a name="toc3"></a>Week 5 Homework

First, read the book up to the end of Chapter 6

Now, the coding homework: 

* Create an enumeration `Planet` of all of the planets of the solar system. Have the raw values be of type Integer, with Mercury having the value of 1
* Create another enumeration `DistantObject` of the planets where the raw values are Integers whose values are the distance of each planet from the sun, in millions of miles. You can find the values to use [here][planets]. 
* Create a third enum `ObjectInSpace` where the raw values are strings that are equal to the planets names. 
* Modify `ObjectInSpace`. Add a method called `periodOfRevolution` that returns the period of revolution of the planet around the sun, as measured in Earth days. This data can also be found in the previous link. The return type should be `Double`.
* Make a new page in the Playground. Copy all the source. Modify `ObjectInSpace`. Change periodOfRevolution to a computed property.
* Make a new page. Copy all the source. Modify `ObjectInSpace` so that you can have associated values. Add a new enum case to `ObjectInSpace` named 'Satellite'. Let it have an associated value of type `ObjectInSpace` so that we can tell which object a Satellite belongs to. You will get an error in XCode saying you need to make the enum `indirect`. Go ahead and do that by accepting XCode's suggestions. Let the period of revolution for a satellite be the same as that of its associated object.
* Create an `ObjectInSpace` called Earth of enum `.Earth`. Create another object that is its satellite, called `Moon`. Display the period of revolution of `Moon`. 



[planets]: http://www.enchantedlearning.com/subjects/astronomy/planets/





   



