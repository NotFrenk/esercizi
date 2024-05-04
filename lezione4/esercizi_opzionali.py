#1. School Grading System:
#Create a function that takes a student's nome and their scores in different subjects as input.
#The function calculates the average score and prints the student's nome, average, 
#and a message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.
"""
def calcola_media(nome:str, voti:int):
    media_voti:int=sum(voti)//len(voti)
    result= "Passed" if media_voti >=60 else "Failed"
    print(f"\n{nome} ha come media: {media_voti}.\nResult:\t{result}")

registro:dict= [
    {"nome": "Alice", "voti": [70, 80, 90]},
    {"nome": "Bob", "voti": [50, 60, 55]},
    {"nome": "Charlie", "voti": [80, 75, 65]}
]
for studente in registro:
    calcola_media(studente["nome"], studente["voti"])
"""
#------------------------------------------------------------------------------------------
#2. Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
"""
import random

def indovina_il_numero():
#srivo allutente le regole del gioco
    print("\t\t<NEW GAME>\n" 
    "Il gioco consiste nel indovinare il numero pensato dalla macchina in \"n\" tentativi.\n"
    "dovrai inserire \"da quale\" numero \"a quale\" numero la macchina deve pensare il numero che dovrai indovinare.\n")

    #contatore di tentativi
    numero_tentativi:int=0 

#controllo dell'inserimento di 'possibilità'    
    while True:
        possibilità = input("In quanti tentativi vuoi provare ad indovinare?\n")
        try:
            possibilità = int(possibilità)  # Converte il valore inserito in un intero
            if possibilità <= 0:
                print("Inserisci un valore maggiore di 0")
            else:
                print("Ok, giocherai con", possibilità, "tentativi.")
                break  # Esce dal loop se il valore è valido
        except ValueError:
            print("Devi inserire un numero intero valido.")


    #controllo dell'inserimento di 'input_numero_minimo'    
    while True:
        input_numero_minimo=input("Numero MINIMO :") #faccio inserire allutente il primo numero
        try:
            input_numero_minimo = int(input_numero_minimo)  # Converte il valore inserito in un intero
            print("Ok, il numero minimo è:", input_numero_minimo)
            break  # Esce dal loop se il valore è valido
        except ValueError:
            print("Devi inserire un numero intero valido.")


        #controllo dell'inserimento di 'input_numero_massimo'    
    while True:
        input_numero_massimo=input("Numero MASSIMO :") #faccio inserire il secondo numero
        try:
            input_numero_massimo = int(input_numero_massimo)  # Converte il valore inserito in un intero
            print("Ok, il numero massimo è:", input_numero_massimo)
            break  # Esce dal loop se il valore è valido
        except ValueError:
            print("Devi inserire un numero intero valido.")

    numero_casuale = random.randint(input_numero_minimo, input_numero_massimo) #la mcchina decide che numero casuale prendere nel range dei numeri inseriti dallutente

    print("\n\t\t-----SCEGLIENDO IL NUMERO------\nOra che è tutto pronto POSSIAMO COMINCIARE\n")

    while numero_tentativi < possibilità:
        while True:
            guess=input("\n Prova ad indovinare \n") 
            try:
                guess = int(guess)  # Converte il valore inserito in un intero
                #controllo che 'guess'sia all'interno dei parametri 'input_numero_minimo' e 'input_numero_massimo'
                if guess < input_numero_minimo:
                    print("ERRORE\n <--- OUT OF BOUND ")
                elif guess > input_numero_massimo:
                    print("ERRORE\n ---> OUT OF BOUND")
                else:
                    break  # Esce dal loop se il valore è valido
            except ValueError:
                print("Devi inserire un numero intero valido.")

        numero_tentativi +=1 #aumente il counter di tentativi di 1 

        if guess < numero_casuale:
            print("PECCATO, il numero misterioso è MAGGIORE")
        elif guess > numero_casuale:
            print("PECCATO, il numero misterioso è MINORE")
        else:
            print("HAI INDOVINATO")
            break

    else:
        print("\n\t\tHAI ESAURITO LE TUE POSSIBILITA'\n"
              f"il numero misterioso era: {numero_casuale}")




indovina_il_numero()

"""

