Title: Notes from Week 10
Date: 2015-11-21 22:20
Modified: 2015-11-21 22:20
Tags: iOS, swift, icw1502
Summary: Notes from Week 10

## Table of Contents

* [Code uploaded to GitHub](#toc1)
* [What we learned this week](#toc2)
* [Week 10 Homework Assignment](#toc3)

## <a name="toc1"></a>Code uploaded to GitHub

The code that we wrote this week in class has been uploaded to our [class GitHub page](https://github.com/aijaz/icw1502).

## <a name="toc2"></a>What we learned this week

This week we learned about UITableViewControllers. First we learned about UITableViews and the responisibilities of UITableViewDataSource and UITableViewDelegate. Then we created a tableview controller to display our model information (a list of books). At first we used a single UITableViewCell of the 'Subtitle' type. Then we created another dynamic prototype of type 'Right Detail.' We chose different reuseIdentifiers based on whether our books were in English or Arabic. We learned about how UITableViewCells are reused and dequeued.

Then we learned how to create custom UITableViewCells. Even though we had two types of dynamic prototype cells, we learned that we could use the same model (UITableViewCell) for each, because only the presentation was changing, not the actual properties of the classes. 

After that we created a second UITableViewController, this time with static cells, to show details of each book. We created a segue from each prototype cell to the new UITableViewController. Then we added a third UIViewController called NumericEntryViewController (like last week's homework) to the storyboard to allow us to change the number of pages in a book. We looked at how to pass information from the detail view controller to the numeric entry view controller. 

Finally we looked at how to pass data from the detail view controller back down to our original data model (the array of books). We discussed how our decision to use value types influenced our code. We also discussed how our code would change if we used reference types (classes). 

## <a name="toc3"></a>Week 10 Homework

Add a view to the top of your main UITableViewController. Add a button there called 'Edit'. When the button is tapped, toggle `tableView.editing` from false to true and back. 

Uncomment out the `canEditRow`, `commitEditingStyle`, `moveRowAtIndexPath`, and `canMoveRowAtIndexPath` functions. Add code to `commitEditingStyle` and `moveRowAtIndexPath` to modify the model data. Look at the `removeAtIndex` and `insert` functions of `Array`. Make sure that you can remove and rearrange the books. 

Also, create another UIViewController called textEntryViewController. Use that to allow you to change the name of the title and author of the book. Don't worry about changing the language just yet. 

We covered a lot of stuff this week. If you have any questions at all, please let me know. I want to make sure you're comfortable with this material. It's important stuff.

