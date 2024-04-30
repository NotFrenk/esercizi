# Francisco Leon Felici


#---------------------------------------------------------------------------------
#4-1. 
#Pizzas: 
#Think of at least three kinds of your favorite pizza. 
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, 
#instead of printing just the name of the pizza. 
#For each pizza, you should have one line of output containing a simple statement 
#like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#such as I really love pizza!
"""
pizze_preferite:list=["margherita","diavola","4 formaggi"]
for pizze in pizze_preferite:
    print(f"La {pizze_preferite[0]} è buona e semplice\n")
    print(f"La {pizze_preferite[1]} ha il salame e picca\n")
    print(f"La {pizze_preferite[2]} ha un sacco di formaggio sopra\n")
    break

print("I love pizza")

"""
#---------------------------------------------------------------------------------
#4-2. 
#Animals: 
#Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, 
#and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, 
#such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!
"""
animali:list=["aquila","fenicottero","pinguino"]
for nomi_animali in animali:
    print(f"L\'{animali[0]} è un rapace maestoso.\n")
    print(f"Il {animali[1]} ha un becco lungo e un piumaggio rosa.\n")
    print(f"Il {animali[2]} non sa volare ma nuota benissimo.\n")
    break
print("Tutti e tre gli animali qua sopra hanno in comune che sono tutti e 3 \"uccelli\"")
"""
#---------------------------------------------------------------------------------
#4-3. 
#Counting to Twenty: 
#Use a for loop to print the numbers from 1 to 20, inclusive.
"""
print("Numer1 da 1 a 21")
for numero in range(1,21):
    print(numero)
"""
#---------------------------------------------------------------------------------
#4-4. 
#One Million: 
#Make a list of the numbers from one to one million, 
#and then use a for loop to print the numbers. 
#(If the output is taking too long, 
#stop it by pressing CTRL-C or by closing the output window.)
"""
numeri:range=[]
for i in range(11):
    numeri.append(i)
print(numeri)

"""

#---------------------------------------------------------------------------------
#4-5. 
#Summing a Million: 
#Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.
"""
minimo=min(numeri)
massimo=max(numeri)
somma=sum(numeri)
print(minimo)
print(massimo)
print(somma)
"""
#---------------------------------------------------------------------------------
#4-6. 
#Odd Numbers: 
#Use the third argument of the range() 
#function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.
"""
numeri_dispari=range(1,21,2)
for numero in numeri_dispari:
    print(numero)
"""
#---------------------------------------------------------------------------------
#4-7. 
#Threes: 
#Make a list of the multiples of 3, from 3 to 30. 
#Use a for loop to print the numbers in your list.
"""
multipli=range(3,31,3)
for numero in multipli :
    print(numero)
"""
#---------------------------------------------------------------------------------
#4-8. 
#Cubes: 
#A number raised to the third power is called a cube. 
#For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes 
#(that is, the cube of each integer from 1 through 10), 
#and use a for loop to print out the value of each cube.
"""
for num in range(1, 11):
    cube = num ** 3
    print(f"The cube of {num} is: {cube}")
"""

#---------------------------------------------------------------------------------
#4-9. 
#Cube Comprehension: 
#Use a list comprehension to generate a list of the first 10 cubes.
"""
cube=[x**3 for x in range(1,11)]
print(cube)
"""
#---------------------------------------------------------------------------------
#4-10. 
#Slices: 
#Using one of the programs you wrote in this chapter, 
#add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. 
#Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. 
#Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. 
#Then use a slice to print the last three items in the list.
"""
lista:list=[1,2,3,4,5,6,7,8,9,10]
for num in lista:
    cube = num ** 3
    print(f"The cube of {num} is: {cube}")



# Printing the first three items in the list
print("The first three items in the list are:", lista[:3])

# Printing three items from the middle of the list
middle_index = len(lista) // 2
print("Three items from the middle of the list are:", lista[middle_index:middle_index + 3])

# Printing the last three items in the list
print("The last three items in the list are:", lista[-3:])
"""
#---------------------------------------------------------------------------------
#4-11. 
#My Pizzas, Your Pizzas: 
#Start with your program from Exercise 4-1. 
#Make a copy of the list of pizzas, and call it friend_pizzas. 
#Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. 
#Print the message My favorite pizzas are:, 
#and then use a for loop to print the first list. 
#Print the message My friend’s favorite pizzas are:, 
#and then use a for loop to print the second list. 
#Make sure each new pizza is stored in the appropriate list.    
"""
pizze_preferite:list=["margherita","diavola","4 formaggi","boscagliola"]
friend_pizzas:list=["margherita","diavola","4 formaggi","capriciosa"]

print("Le mie pizze preferite sono:")
for pizze in pizze_preferite:
    print(pizze)

print("\nLe pizze preferite del m io amico sono:")
for a in friend_pizzas:
    print(a)
"""

#---------------------------------------------------------------------------------
#4-12. 
#More Loops: 
#All versions of foods.py in this section have avoided using for loops when printing, 
#to save space. Choose a version of foods.py, 
#and write two for loops to print each list of foods.
"""
print("Numer1 da 1 a 21")
for numero in range(1,21):
    print(numero)
"""

#---------------------------------------------------------------------------------
#4-15. 
#Code Review: 
#Choose three of the programs you’ve written in this chapter 
#and modify each one to comply with PEP 8
"""

"""

#---------------------------------------------------------------------------------
#5-1. 
#Conditional Tests: 
#Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.
"""
car = 'subaru'
print(car)

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs the amount of letters in the car name == '4'? I predict False.")
print(len(car)==4)

print("\nIs the amount of letters in the car name == '6'? I predict True.")
print(len(car)==6)

print("\nIs car in 'ferrari, audi, lamborghini'? I predict False.")
print(car in["ferrari","audi","lamborghini"])

print("\nIs car in 'ferrari, audi,'subaru',lamborghini'? I predict True.")
print(car in["ferrari","audi","subaru","lamborghini"])

print("\nIs car name == 'urabus'? I predict False.")
print(car == 'urabus')

print("\nIs car name != 'urabus'? I predict True.")
print(car == 'subaru')

print("\nIs the amount of letters in the car name > '10'? I predict False.")
print(len(car)>10)

print("\nIs the amount of letters in the car name < '10'? I predict True.")
print(len(car)<10)
"""

#---------------------------------------------------------------------------------
#5-2. 
#More Conditional Tests: 
#You don’t have to limit the number of tests you create to 10. 
#If you want to try more comparisons, write more tests and add them

#to conditional_tests.py. Have at least one True and one False result for each of
#the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list
"""
car = 'subaru'
print(car)

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car =='SUBARU'? I predict False.")
print(car.lower()=='SUBARU')

print("\nIs car =='subaru'? I predict True.")
print(car.lower()=='subaru')

print("\nIs the amount of letters in the car name <= '4'? I predict False.")
print(len(car)<=4)

print("\nIs the amount of letters in the car name >= '4'? I predict True.")
print(len(car)>=6)

x:int=11
y:int=3
z:int=7

print(f"\n{x,z,y}")

print("\nè 'z' > di 'x'? I predict False.")
print(z>x)

print("\nè 'y' < di 'x'? I predict True.")
print(y<x)

print("\nIs car in 'ferrari, audi, lamborghini'? I predict False.")
print(car in["ferrari","audi","lamborghini"])

print("\nIs car in 'ferrari, audi,'subaru',lamborghini'? I predict True.")
print(car in["ferrari","audi","subaru","lamborghini"])
"""
#---------------------------------------------------------------------------------
#5-3.
#Alien Colors #1: 
#Imagine an alien was just shot down in a game. 
#Create a variable called alien_color and assign it a value 
#of 'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green. 
#If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. 
#(The version that fails will have no output.)
"""
Li ho fatti tutti e 3 insime
"""
#---------------------------------------------------------------------------------
#5-4. 
#Alien Colors #2: 
#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#• If the alien’s color is green, 
#print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, 
#print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and another that runs the else block.
"""
Li ho fatti tutti e 3 insime

"""
#---------------------------------------------------------------------------------
#5-5.
#Alien Colors #3: 
#Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
alien_color:str=input("di che colore è l'alieno?\n| 'green' | 'yellow' | 'red' |\n")
if alien_color == "yellow":
    print("you erned '10 POINTS'")
elif alien_color == "green":
    print("you erned '5 POINTS'")
elif alien_color == "red":
    print("you erned '15 POINTS'")
else:
    print("ERRORE")
"""
#---------------------------------------------------------------------------------
#5-6. 
#Stages of Life: 
#Write an if-elif-else chain that determines a person’s stage of life. 
#Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.
"""
age =int(input("inserire età"))
if age < 2:
    print("the person is a baby")
elif age < 4:
    print("the person is a toddler")
elif age < 13:
    print("the person is a kid")
elif age < 20:
    print("the person is a teenager")
elif age < 65:
    print("the person is an adult")
elif age > 64:
    print("the person is an elder")
else:
    print("ERRORE")
"""

#---------------------------------------------------------------------------------
#5-7. 
#Favorite Fruit: 
#Make a list of your favorite fruits, 
#and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
#If the fruit is in your list, the if block should print a statement, such as You really like Apples!
"""
favorite_fruits:str=["mango","mela","pera",]
if "mango" in favorite_fruits:
    print("buono il mango")
if "cocco" not in favorite_fruits:
    print("il frutto 'cocco' non è nella lista")
if "mela" in favorite_fruits:
    print("buono il mela")
if "pera" in favorite_fruits:
    print("buono il pera")
if "pomodoro" not in favorite_fruits:
    print("il 'pomodoro' non è nella tua lista")
"""

#---------------------------------------------------------------------------------
#5-8. 
#Hello Admin: 
#Make a list of five or more usernames, including the name 'admin'. 
#Imagine you are writing code that will print a greeting to each user after they log in to a website. 
#Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, 
#would you like to see a status report?
#• Otherwise, print a generic greeting, such as c Jaden, thank you for logging in again.
"""
lista:str=["marco","lollo","admin","franco"]
for utenti in lista:
    if utenti!="admin":
        print(f"Hello {utenti.title()}")
    else:
        print(f"Hello admin, would you like to see a status report?")
"""
#---------------------------------------------------------------------------------
#5-9. 
#No Users: 
#Add an if test to hello_admin.py to make sure the list of users is not empty.
#• If the list is empty, print the message We need to find some users!
#• Remove all of the usernames from your list, and make sure the correct message is printed.
"""
lista:str=[]
if lista ==[]:
    print("We need to find some users!")
else:
    for utenti in lista:
        if utenti!="admin":
            print(f"Hello {utenti.title()}")
        else:
            print(f"Hello admin, would you like to see a status report?")
"""

#---------------------------------------------------------------------------------
#5-10. 
#Checking Usernames: 
#Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. 
#Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. 
#If it has, print a message that the person will need to enter a new username. 
#If a username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. 
#If 'John' has been used, 'JOHN' should not be accepted. 
#(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
"""
current_users:list=["marco","lollo","danila","franco","ginevra"]
new_users:list=["osama","lorenzo","danila","franco","gaia"]
comparazione:list=[user.lower() for user in current_users]
for nuovi_utenti in new_users:
    if nuovi_utenti.lower() in current_users:
        print("gia in uso")
    else:
        print("the username is available")
"""
#---------------------------------------------------------------------------------
#5-11. 
#Ordinal Numbers: 
#Ordinal numbers indicate their position in a list, such as 1st or 2nd. 
#Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
#Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", 
#and each result should be on a separate line.
"""
numbers = list(range(1, 10))


for number in numbers:

    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
"""

