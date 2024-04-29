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

"""
invitati:list[str]=("Monica","Giorgio","Alex")  

invito:str= f" ti invito a cena domani alle 20:00"

for elementi in invitati:
    print(invitati[0] + invito)
    print(invitati[1] + invito)            #I create a for loop to write all the variable sentences
    print(invitati[2] + invito)
    break

"""
#----------------------------------------------------------------------------
#3-5
#Changing Guest List:
#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

"""
invitati:list[str]=["Monica","Giorgio","Alex"]

invito:str= f" ti invito a cena domani alle 20:00"

for elementi in invitati:
    print(invitati[0] + invito)
    print(invitati[1] + invito)            #I create a for loop to write all the variable sentences
    print(invitati[2] + invito)
    break
print(invitati[0])
invitati[0]="Adriana"
print(invitati)
"""
#----------------------------------------------------------------------------
#3-6. 
#More Guests: 
#You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.
"""
invitati:list[str]=["Monica","Giorgio","Alex"]

invito:str= f" ti invito a cena domani alle 20:00"

for elementi in invitati:
    print(invitati[0] + invito)
    print(invitati[1] + invito)            #I create a for loop to write all the variable sentences
    print(invitati[2] + invito)
    break
print(invitati[0]+" non potrà più partecipare")
invitati[0]="Adriana"                             #remuve "monica" end adding "adriana" in the guests list
print(invitati)

print("ho trovato un tavolo più grande")
invitati.insert(0,"balotelli")
invitati.insert(2,"salvatore")                    #adding 3 mor quests
invitati.append("pippo")

for elementi in invitati:
    print(invitati[0] + invito)
    print(invitati[1] + invito)            
    print(invitati[2] + invito)
    print(invitati[3] + invito)
    print(invitati[4] + invito)          
    print(invitati[5] + invito)
    break

"""
#----------------------------------------------------------------------------
#3-7. 
#Shrinking Guest List: 
#You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""
invitati:list[str]=["Monica","Giorgio","Alex"]

invito:str= f" ti invito a cena domani alle 20:00"

for elementi in invitati:
    print(invitati[0] + invito)
    print(invitati[1] + invito)            #I create a for loop to write all the variable sentences
    print(invitati[2] + invito)
    break
print(invitati[0]+" non potrà più partecipare")
invitati[0]="Adriana"                             #remuve "monica" end adding "adriana" in the guests list
print(invitati)

print("ho trovato un tavolo più grande")
invitati.insert(0,"balotelli")
invitati.insert(2,"salvatore")                    #adding 3 mor quests
invitati.append("pippo")

for elementi in invitati:
    print(invitati[0] + invito)
    print(invitati[1] + invito)            
    print(invitati[2] + invito)
    print(invitati[3] + invito)
    print(invitati[4] + invito)          
    print(invitati[5] + invito)
    break
print("il tavolo più grande non arriverà in tempo per la cena quindi ho posto solo per due persone")

elementi_cancellati=[]       #list for the deleted elements
# Iterate the list end remove the elements
while len(invitati)>2:
    elemento_rimosso = invitati.pop()
    elementi_cancellati.append(elemento_rimosso)

# print the message for each deleted element element
for elemento in elementi_cancellati:
    print(f"mi dispiace {elemento} ma non sei più invitato")

invito2:str=f" sei ancora tra gli invitati, ti aspetto domani alle 20:00"

for elementi in invitati:
    print(invitati[0] + invito2)
    print(invitati[1] + invito2)
    break
del(invitati[1])
del(invitati[0])
print(invitati)
"""
#----------------------------------------------------------------------------
#3-8. 
#Seeing the World: 
#Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
"""
posti_da_visitare:list[str]=["Miami","Stonehenge","Egitto","Alaska","Bari"]
print("Ordine originale:")
print(posti_da_visitare)

print("In ordine alfabetico:")
print(sorted(posti_da_visitare))
print("Verifica")
print(posti_da_visitare)        #I check to see if the list is still in its original order

print("Al contrario")
print(sorted(posti_da_visitare,reverse=True))
print("Verifica")
print(posti_da_visitare)        #I check to see if the list is still in its original order

print("modifichiamo l'ordine")
posti_da_visitare.reverse()
print(posti_da_visitare)
posti_da_visitare.reverse()
print(posti_da_visitare)

print("usando '.sort'")
posti_da_visitare.sort()
print(posti_da_visitare)
print("alfabeto al contrario")
posti_da_visitare.sort(reverse=True)
print(posti_da_visitare)

"""
#----------------------------------------------------------------------------
#3-9. 
#Dinner Guests:
#Working with one of the programs from Exercises 3, 
#use len() to print a message indicating the number of people you’re inviting to dinner.
"""
numero_invitati=len(invitati)
print("Gli invitati sono", numero_invitati)
"""
#----------------------------------------------------------------------------
#3-10.
#Every Function: 
#Think of things you could store in a list. 
#For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items 
#and then uses each function introduced in this chapter at least once.
"""
lista:list=["sardegna","montagna","parenti in toscana"]
print("Posti da visitare questa estate:" ,lista)

#I modify "montagna" to add something more specific
lista[1]="andare sul Terminillo"
print("ho modificato qualcosa",lista)

#I'll add something else
lista.append("viaggio con gli amici")
print("ho aggiunto qualcosa",lista)

#remove something
lista.pop(0)
print("purtroppo ho dovuto togliere qualcosa dalla lista",lista)
"""

#----------------------------------------------------------------------------
#6-1. 
#Person: 
#Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. 
#Print each piece of information stored in your dictionary.
"""
profile:dict={
    "first name":"Francisco",
    "last name":"Felici",
    "age":"20",
    "city":"Roma"
}
for info in profile:
    print(profile[info])
"""
#----------------------------------------------------------------------------
#6-2. 
#Favorite Numbers: 
#Use a dictionary to store people’s favorite numbers. 
#Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary.
#Print each person’s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.
"""
favorite_numbers:dict={
    "Andrea":72,
    "Marco":69,
    "Francisco":8,
    "Monica":4,
    "Dani":23
}
for info in favorite_numbers:
    print(favorite_numbers)
    break
"""
#----------------------------------------------------------------------------
#6-3. 
#Glossary: 
#A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, 
#or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
glossario = {
    'Variabile:': 'Un contenitore per immagazzinare dati in un programma.',
    'Funzione:': 'Un blocco di codice riutilizzabile che esegue una specifica azione.',
    'Condizione:': 'Una struttura di controllo che permette di eseguire azioni diverse in base a una condizione.',
    'Lista:': 'Una collezione ordinata di elementi, modificabile e indicizzata.',
    'Dizionario:': 'Una collezione di coppie chiave-valore, non ordinata e modificabile.'
}
for a,b in glossario.items():
    print(f"{a}\n{b}\n")

"""
#----------------------------------------------------------------------------
#6-7. 
#People: 
#Start with the program you wrote for Exercise 6-1.
#Make two new dictionaries representing different people, 
#and store all three dictionaries in a list called people. 
#Loop through your list of people. As you loop through the list, 
#print everything you know about each person.
"""
profile1:dict={
    "first name":"Francisco",
    "last name":"Felici",
    "age":"20",
    "city":"Roma"
}

profile2:dict={
    "first name":"Silvio",
    "last name":"rossi",
    "age":"21",
    "city":"Moldavia"
}

profile3:dict={
    "first name":"Gabry",
    "last name":"lungu",
    "age":"18",
    "city":"Romania"
}

people:list=[profile1,profile2,profile3]    
    
for profile in people:
    print("\ninfo:")
    for chiave,valore in profile.items():
        print(f"{chiave}:{valore}")
"""
#----------------------------------------------------------------------------
#6-8. 
#Pets: 
#Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you know about each pet.
"""
animale1:dict={
    "kind of animal":"Gatto",
    "owner’s name":"Francisco"
}
commento1:str=(f"Il gatto è bello")

animale2:dict={
    "kind of animal":"Serpente",
    "owner’s name":"Monica"
}
commento2:str=(f"il serpente sibila")

animale3:dict={
    "kind of animal":"Pappagallo",
    "owner’s name":"Olivia"
}
commento3:str=(f"il pappagallo ripete le cose")

pets:list=[animale1,animale2,animale3]


for animale in pets :
    print("\nInfo")
    print(f"{animale1}\n{commento1}\n")
    print(f"{animale2}\n{commento2}\n")
    print(f"{animale3}\n{commento3}\n")
    break
"""
#----------------------------------------------------------------------------
#6-9.
#Favorite Places: 
#Make a dictionary called favorite_places. 
#Think of three names to use as keys in the dictionary, 
#and store one to three favorite places for each person. 
#To make this exercise a bit more interesting, 
#ask some friends to name a few of their favorite places. 
#Loop through the dictionary, and print each person’s name and their favorite places.
"""favorite_places:dict={
    "francisco":["New York","Venezia","Las Palmas"],
    "silviu":["Roma","San Pietroburgo","San Paolo"],
    "gabriele":["Torino","Amsterdam","Firenze"]
}

for nome,posto in favorite_places.items():
    print(f"\nI posti preferiti di {nome} sono:")
    for i in posto:
        print(f"{i}")
"""
#----------------------------------------------------------------------------
#6-10. 
#Favorite Numbers: 
#Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#Then print each person’s name along with their favorite numbers.
"""
favorite_numbers:dict={
    "Andrea":[72,21,3],
    "Marco":[69,45,32],
    "Francisco":[8,5,2],
    "Monica":[4,9,0],
    "Dani":[23,76,7]
}
for persona,numeri in favorite_numbers.items():
    print(f"I numeri preferiti di {persona} sono:")
    for i in numeri:
        print(f"-  {numeri}")
        break
"""
#----------------------------------------------------------------------------
#6-11. 
#Cities: 
#Make a dictionary called cities. 
#Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city 
#and include the country that the city is in, its approximate population, 
#and one fact about that city. 
#The keys for each city’s dictionary should be something like 
#country, population, and fact. 
#Print the name of each city and all of the information you have stored about it.
"""
cities:dict={
    "Amsterdam":{
        "paese":"Olanda",
        "popolazione":"821.752",
        "curiosità":"Ad Amsterdam ci sono più biciclette che persone"
        },

    "San Paolo":{
        "paese":"Brasile",
        "popolazione":"12,33 milioni",
        "curiosità":"Ogni ora, lungo la Avenida Paulista, passano ben 5.700 auto e 1.400 autobus"
        },
        
    "Roma":{
        "paese":"Italia",
        "popolazione":"2,873 milioni",
        "curiosità":"Ci sono più fontane a Roma che in qualsiasi altra città del mondo"
    }
}
for città,info in cities.items():
    print(f"{città}")
    print(f"paese:{info["paese"]}")
    print(f"popolazione:{info["popolazione"]}")
    print(f"curiosità:{info["curiosità"]}")
"""
#----------------------------------------------------------------------------
#6-12.
#Extensions: 
#We’re now working with examples that are complex enough that they can be extended in any number of ways. 
#Use one of the example programs from this chapter, 
#and extend it by adding new keys and values, 
#changing the context of the program, or improving the formatting of the output.
"""
cities:dict={
    "Amsterdam":{
        "paese":"Olanda",
        "popolazione":"821.752",
        "curiosità":"Ad Amsterdam ci sono più biciclette che persone",
        "lingua":"Olandese"
        },

    "San Paolo":{
        "paese":"Brasile",
        "popolazione":"12,33 milioni",
        "curiosità":"Ogni ora, lungo la Avenida Paulista, passano ben 5.700 auto e 1.400 autobus",
        "lingua":"Portoghese"
        },
        
    "Roma":{
        "paese":"Italia",
        "popolazione":"2,873 milioni",
        "curiosità":"Ci sono più fontane a Roma che in qualsiasi altra città del mondo",
        "lingua":"Italiano"
    },

    "londra":{
        "paese":"Inghilterra",
        "popolazione":"8,982 milioni",
        "curiosità":"La metropolitana di Londra è la più antica al mondo",
        "lingua":"Inglese"
    }
}
for città,info in cities.items():
    print(f"{città.upper()}")
    print(f"Paese:\t{info["paese"]}")
    print(f"Popolazione:\t{info["popolazione"]}")
    print(f"Curiosità:\t{info["curiosità"]}")
    print(f"Lingua:\t{info["lingua"]}\n")
"""
