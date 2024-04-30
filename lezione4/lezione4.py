#Francisco Leon Felici

#8-1. 
#Message: 
#Write a function called display_message() 
#that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.
"""
def display_message():
    message = "In this chapter, we are learning about conditional statements and functions."
    print(message)

# Calling the function to display the message
display_message()
"""

#--------------------------------------------------------------------------------
#8-2. 
#Favorite Book: 
#Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, 
#such as "One of my favorite books is Alice in Wonderland". 
#Call the function, making sure to include a book title as an argument in the function call.
"""
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")
"""

#--------------------------------------------------------------------------------
#8-3. 
#T-Shirt: 
#Write a function called make_shirt() 
#that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. 
#Call the function a second time using keyword arguments.
"""
def make_shirt(size,message):
    print(f"creando una maglietta: {size}\ncon sopra scritto: {message}\n")
make_shirt("grande", "Ciao\n")
make_shirt(size="media", message="cioa")
"""
#--------------------------------------------------------------------------------
#8-4. 
#Large Shirts: 
#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, 
#and a shirt of any size with a different message.
"""
def make_shirt(size="XL",message="I love Python"):
    print(f"Creating a {size} shirt with the message: {message}")
make_shirt()
make_shirt(size="medium")
make_shirt(size="S",message="che bello python")
"""
