Title: Notes from Week 11
Date: 2015-11-29 11:45
Modified: 2015-11-29 11:45
Tags: iOS, swift, icw1502
Summary: Notes from Week 11

## Table of Contents

* [Code uploaded to GitHub](#toc1)
* [What we learned this week](#toc2)
* [Week 11 Homework Assignment](#toc3)

## <a name="toc1"></a>Code uploaded to GitHub

The code that we wrote this week in class has been uploaded to our [class GitHub page](https://github.com/aijaz/icw1502).

## <a name="toc2"></a>What we learned this week

This week we learned about UITabBarControllers, UINavigationControllers and UIImagePickerControllers. First, we made a simple project using a UITabBarController that displayed two view controllers with differently-colored views. We learned about the relationship between the view controllers, and how the UITabBarItem controlled the display of the tabs. We did all this in the storyboard, without writing a single line of code. 

Then we added our HypnoRect app from a few weeks ago into a new tab in our new project. We saw how copying storyboard scenes over essentially means we copied the XML over. That XML includes all the `IBOutlet`s and `IBAction`s that we defined a few weeks ago. We had to remember to copy all the classes over, so that we wouldn't have 'dangling references' from the XML.

Then we learned about UINavigationControllers and added last week's Book project to our TabBar project. We moved the saving logic from the "done" button to `viewWillDisappear`. We saw how our segues 'automatically' became push segues because the view controllers were now part of a UINavigationController's stack. 

Then we looked at various ways to add an item to our data source and the related UITableView. We considered adding a segue directly from a UIBarButton to a new UIViewController, and alternatively adding an IBAction that programmatically performed a segue. We finally decided to reuse our edit code and insert a new UINavigationController whose root view controller is what's normally the second view controller on the stack during the edit use case. 

Finally we learned about UIImagePickerViewController and UIImages. We were introduced to NSFileManager and the Documents directory.

## <a name="toc3"></a>Week 11 Homework

Your homework for this week is to create a new project that has a single UIViewController. That controller should have 1 button and 1 image view. When you tap the button, the app should check to see if the camera is present. If so, it should prompt you to choose between the camera and the photo album as sources for the image. If a camera is not present, it should not prompt you, but take you directly to your photo album so that you can select an image. 

When you select an image, the app should save the image onto the file system, in the Documents directory. If there already is a file there, it should be overwritten. That way, we will never have more than one file saved in the documents directory. The image should be saved in the JPEG format. The image should also be displayed in the image view.

For this homework assignment you will need to use frameworks that we have not covered in class. By now you should be comfortable reading documentation. To prompt the user to choose between the Camera and Photo Library you will need to use a `UIAlertController`. Do *not* use the old `UIAlertView` because that class has been deprecated in iOS 8. 

To convert a UIImage to data (`NSData`), you will need to use the `UIImageJPEGRepresentation` function. To save `NSData` to the file system you will need to use an `NSFileManager`.  

If you get stuck on something, feel free to Google for answers, ask me, or ask your fellow students on the WhatsApp group or email list. 
