Title: Notes from Week 8
Date: 2015-11-08 10:20
Modified: 2015-11-08 10:20
Tags: iOS, swift, icw1502
Summary: Notes from Week 8

## Table of Contents

* [Code uploaded to GitHub](#toc1)
* [What we learned this week](#toc2)
* [Week 8 Homework Assignment](#toc3)

## <a name="toc1"></a>Code uploaded to GitHub

The code that we wrote this week in class has been uploaded to our [class GitHub page](https://github.com/aijaz/icw1502).

## <a name="toc2"></a>What we learned this week

This week we learned about UIViews, their frames and bounds and how those change with transformations. We also looked at the Run Loop and what happens when a view is marked dirty with `setNeedsDisplay()`. We learned how view controllers are responsible for views. We first wrote a simple app using a manually-created window and view. Then we subclassed UIView to create a view that knew how to draw itself. It drew a rectangle. 

In our second project we wrote an app that drew concentric rectangles. We used `IBOutlet`s and `IBAction`s to link a slider to our view controller to control the line width. Then we created a custom control that allowed us to select one of many circles to control line width.

## <a name="toc3"></a>Week 8 Homework

Modify our `Rater` custom control. Instead of displaying circles, it should display triangles. In fact, in should be able to display any type of shape that I can draw with a `UIBezierPath`.  Think about the different ways we have learned to eliminate duplicate code and prevent large if-else statements. There are at least two that I can think of. One is more "Swift-ish" than the other. If you get stuck, please feel free to ask for help.

