# workout-tracker
OOP workout tracking system 

What does this system do?
This workout tracking system that I just created lets a user record all of their exercises and it will organize them for the user.  For each exercise you have to add in how long it was and other information about it, so the system can figure out how many calories were burnt. The system will also add up all the time you took to complete your exercises, and will display a clear summary of your entire workout at the end of the user putting in all the information. 

What OOP concepts does it demonstrate?
This system shows off alot of object-oriented concepts. A few of them being the classes and objects concept. In this system these were used to represent the diffrent exercises and the workouts. This system also shows off the use of inheritance, when you create the different exercise types, since its inheriting the types from the Exercise class. Lastly, it shows off encapsulation, since the exercise list is privite inside a different class, but we can access it through methods. 

Reflection questions:
The src structure makes it so you seperate your real code, and tests, to make sure that the project stays clean and to follow the best practices, and layout. 
We do this so that it will call the parent class first before it calls the sub-class to avoid problems. 
It allows us to reuse methods that we used in subclasses so that we dont have to waste time writing it out again we can just eruse it. 
Tests show us what is expected out of the code, and we can use these tests to find out what is going wrong and what you need to change n order for the test to work. 
We do this so that the main branch is always production ready, and is open, and clean for us when we need to actually go throug with the code we just created. 