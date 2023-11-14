
#Create a Python file named lab_7-1.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Create a function called greeting()
def greeting():
    #Add a docstring to the function that explains how the function can only print "Hello World" on one line
    """This function can only print hello world on one line."""
    #Add a statement in the function to print "Hello World!"
    print("Hello World!")
#Add a statement that returns the docstring for the greeting function
help(greeting)
#Add another statement to call the function
greeting()
