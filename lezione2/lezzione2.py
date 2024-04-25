#Francisco felici
#18/04/24
#es 2.3
"""
nome:str="Andrea"

messaggio:str= f"ciao {nome} andiamo a studiare python insime?"

print(messaggio)
"""
#----------------------------------------------------------------------------
#es 2.4
#Use a variable to represent a person’s name,
#and then print that person’s name in lowercase, uppercase, and title case.

"""

nome:str="Andrea"

nome_lower:str= nome.lower()

nome_upper:str= nome.upper()

nome_title:str=nome.title()

print(f"{nome}, {nome_lower}, {nome_upper}, {nome_title}")

"""
#-----------------------------------------------------------------------
#es: 2-5.
#Famous Quote: 
#Find a quote from a famous person you admire.
#Print the quote and the name of its author. Your output should look something like the following,
#including the quotation marks: Albert Einstein once said,
#“A person who never made a mistake never tried anything new.”

"""
print(f"Isaac Newton una volta disse \"Gli uomini costruiscono troppi muri e mai abbastanza ponti.\"")
"""
#----------------------------------------------------------------------------
#2-6. 
#Famous Quote 2: 
#Repeat Exercise 2-5, but this time, 
#represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message.

"""
famous_person:str=("Isaac Newton")
message:str=("\"Gli uomini costruiscono troppi muri e mai abbastanza ponti.\"")
print(famous_person + " una volta disse " + message)
"""
#----------------------------------------------------------------------------
#2-8. 
#File Extensions: 
#Python has a removesuffix() method that works exactly like removeprefix().
#Assign the value 'python_notes.txt' to a variable called filename.
#Then use the removesuffix() method to display the filename without the file extension, 
#like some file browsers do.

"""
filename:str=("python_notes.txt")
print(filename.removesuffix(".txt"))
"""
#----------------------------------------------------------------------------
#3-1. 
#Names:
#Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

"""
lista_nomi:list=["Gaia","Lorenzo","Oussama"]
for elementi in lista_nomi:
    print(elementi)
"""
#----------------------------------------------------------------------------
#3-2. Greetings:
#Start with the list you used in Exercise 3-1, 
#but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.

"""
lista_frase:list=["come stai?", "con che linguaggio programmi?", "ti aspetto alla metro"]
lista_nomi:list=["Gaia","Lorenzo","Oussama"]
for nome, frase in zip(lista_nomi,lista_frase):
    print(nome,frase)
"""
#----------------------------------------------------------------------------
#3-3. 
#Your Own List: 
#Think of your favorite mode of transportation, such as a motorcycle or a car, 
#and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

"""
car_list:list[str]=("macchina","motocicletta","elicottero")  #i create a list

tras1:str= f"la {car_list[0]} è un buon mezzo per spostarsi,"
tras2:str= f"però vorrei tanto avere una {car_list[1]}."                    #I create a variable for each item in the list and write a custom message to it recalling the specific word via its position in the dictionary
tras3:str= f"Ma con il traffico che c'è un {car_list[2]} sarebbe ideale"

for elementi in car_list:
    print(tras1)
    print(tras2)            #I create a for loop to write all the variable sentences
    print(tras3)
    break
"""
#----------------------------------------------------------------------------
#3-4.
#Guest List: 
#If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

""""""
invitati:list[str]=("Monica","Giorgio","Alex")  

invito:str= f" ti invito a cena domani alle 20:00"

for elementi in invitati:
    print(invitati[0] + invito)
    print(invitati[1] + invito)            #I create a for loop to write all the variable sentences
    print(invitati[2] + invito)
    break