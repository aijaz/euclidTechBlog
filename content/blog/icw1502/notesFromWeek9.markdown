Title: Notes from Week 9
Date: 2015-11-20 22:20
Modified: 2015-11-20 22:20
Tags: iOS, swift, icw1502
Summary: Notes from Week 9

## Table of Contents

* [Code uploaded to GitHub](#toc1)
* [What we learned this week](#toc2)
* [Week 9 Homework Assignment](#toc3)

## <a name="toc1"></a>Code uploaded to GitHub

The code that we wrote this week in class has been uploaded to our [class GitHub page](https://github.com/aijaz/icw1502).

## <a name="toc2"></a>What we learned this week

This week we learned about UIViewControllers. We created IBOutlets and IBActions for our buttons. First we created them in code using a XIB file to design the view. We learned how to present and dismiss views. We looked at several different ways to share data between view controllers. We tried a tightly coupled solution, which we dismissed as a poor design. We tried delegation, and then we used a protocol-based solution, passing closures to the presented view controllers. 

Then we learned how to create view controllers in our stroryboard. We learned about segues and learned how to identify different segues in `prepareForSegue`. Finally we learned about the life cycle of view controllers and the various methods that are called, such as `viewDidLoad` and `viewWillAppear` and `viewWillDisappear`.

## <a name="toc3"></a>Week 9 Homework

For this week's homework please make a new view controller called NumericInputViewController. This VC should have one UITextField. Implement it like we did in class. 

Add a new button to your week 8 HypnoRect view that displays this new VC when tapped. When the user taps done on the VC, if they typed in a valid Int from 1 to 20 set the lineWidth of the rectangles to that number. Otherwise set it to 5. 

Extra credit: when the VC is shown, pre populate the text field with the current line width. 

