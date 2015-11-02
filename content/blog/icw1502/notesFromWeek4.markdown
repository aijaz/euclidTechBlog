Title: Notes from Week 4
Date: 2015-10-11 12:00
Modified: 2015-10-11 12:00
Tags: iOS, swift, icw1502
Summary: Notes from Week 4

## Table of Contents

* [Playgrounds uploaded to GitHub](#toc1)
* [What we learned this week](#toc2)
* [Week 4 Homework Assignment](#toc3)

## <a name="toc1"></a>Playgrounds uploaded to GitHub

All the playgrounds we've used in class have been uploaded to our [class GitHub page](https://github.com/aijaz/icw1502).

## <a name="toc2"></a>What we learned this week

This week we covered Chapter 5 from our text book. We looked at `inout` parameters briefly, and promised each other we wouldn't use them. Then we learned about closures and the what optimizations we can make when a closure is the last parameter in a function call. After that we learned about Generics. We ended the day looking at Array transformation functions. We wrote our own version of `map` by making an extension to `Array`. 

## <a name="toc3"></a>Week 4 Homework

First, read the book up to the end of Chapter 5

Now, the coding homework: 

To find the length of a `String` call the `lengthOfBytesUsingEncoding()` method. For example, to find the length of the string "Aijaz", do the following:

    "Aijaz".lengthOfBytesUsingEncoding(NSUTF8StringEncoding) // should return 5

I don't like typing all that over and over again.

Make an extension function to `String` called len that returns the length of the string by calling lengthOfBytesUsingEncoding as shown above

To sort an array, call the `sort` function. This function takes an optional closure that defines how to sort the array. The closure takes two parameters, both of the same type of the Elements of the array. The closure should return true if the first parameter should appear before the second, and false otherwise. If you don't specify a closure, the array is sorted in a default manner (lexically for strings).

Create an array called `words` that contains the following words: 

* the
* quick
* brown
* fox
* jumps 
* over
* a 
* lazy
* dog

Sort the array `words` lexically and store the result in an array named `lexical`.

`lexical` should look like this:

    ["a", "brown", "dog", "fox", "jumps", "lazy", "over", "quick", "the"]

Sort the array `words` by the length of the words (in increasing order) and store the result in an array named `byWordLengthAscending`

`byWordLengthAscending` should look like this: 

    ["a", "the", "fox", "dog", "over", "lazy", "quick", "brown", "jumps"]

 Sort the array `words` by the length of the words (in decreasing order) and store the result in an array named `byWordLengthDescending`

`byWordLengthDescending` should look like this: 

    ["quick", "brown", "jumps", "over", "lazy", "the", "fox", "dog", "a"]

Make another routine like byWordLengthAscending but with the following change: If two words have the same length, then the word that appears first lexically shows up first. Save this into an array named `byWordLengthAndLexicalAscending`

`byWordLengthAndLexicalAscending` should look like this:     

    ["a", "dog", "fox", "the", "lazy", "over", "brown", "jumps", "quick"]

    // Notice how 'dog', 'fox', and 'the' are now sorted

Make another routine like byWordLengthDescending but with the following change: If two words have the same length, then the word that appears first lexically shows up second. Save this into an array named `byWordLengthAndLexicalDescending`

`byWordLengthAndLexicalDescending` should look like this:     

    ["quick", "jumps", "brown", "over", "lazy", "the", "fox", "dog", "a"]

    // Notice how 'jumps' and 'brown' are now sorted

### Extra Credit

* Modify all functions so that they're case-insensitive    
* Play around with `words`. Try adding some emoji (with Command-Control-Space) and see what happens.





   



