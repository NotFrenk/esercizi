# Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. 
# La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

# Classe Contatore
# Attributi:
# - conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

# Metodi:
# - __init__(): Inizializza l'attributo conteggio a 0.
# - setZero(): Imposta il conteggio a 0.
# - add1(): Incrementa il conteggio di 1.
# - sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. 
# Se il conteggio è già 0, stampa un messaggio di errore.
# - get(): Restituisce il valore corrente del conteggio.
# - mostra(): Stampa a schermo il valore corrente del conteggio.

# For example:
# Test 	

# c = Contatore()  
# c.add1() 
# c.mostra()

# Result

# Conteggio attuale: 1
"""
class Contatore:
    def __init__(self):
        self.conteggio:int=0
    
    def setZero(self):
        self.conteggio = 0

    def add1(self):
        self.conteggio += 1

    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print(f'Non è possibile eseguire la sottrazione')
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f'Conteggio attuale: {self.get()}')


c = Contatore()  
c.add1() 
c.mostra()
"""


# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, 
# modificare, e cercare ricette basate sugli ingredienti. 
# Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): 
# Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
# Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): 
# Aggiunge un ingrediente alla ricetta specificata. 
# Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

#     - remove_ingredient(recipe_name, ingredient): 
# Rimuove un ingrediente dalla ricetta specificata. 
# Restituisce la ricetta aggiornata o un messaggio di errore 
# se l'ingrediente non è presente o la ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): 
# Sostituisce un ingrediente con un altro nella ricetta specificata. 
# Restituisce la ricetta aggiornata o un messaggio di errore se 
# l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): 
# Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): 
# Mostra gli ingredienti di una specifica ricetta. 
# Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): 
# Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
# Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
"""
class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def create_recipe(self, name: str, ingredients):
        if name in self.recipes:
            return f'ERRORE: {name} --> questa ricetta esiste già'
        self.recipes[name] = list(ingredients)
        #return f'Ricetta {name} creata con successo'
        return {name: ingredients}
    
    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return f'ERRORE: {recipe_name} --> questa ricetta non esiste'
        if ingredient  in self.recipes[recipe_name]:
            return f'ERRORE: {ingredient} --> questo ingrediente esiste già nella ricetta {recipe_name}'
        else:
            self.recipes[recipe_name].append(ingredient)
        #return f'Ingrediente {ingredient} AGGIUNTO alla ricetta {recipe_name}'
        return {recipe_name: self.recipes[recipe_name]}
    
    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return f'ERRORE: {recipe_name} --> questa ricetta non esiste'
        if ingredient not in self.recipes[recipe_name]:
            return f'ERRORE: {ingredient} --> questo ingrediente non esiste nella ricetta {recipe_name}'
        self.recipes[recipe_name].remove(ingredient)
        return f'Ingrediente {ingredient} RIMOSSO dalla ricetta {recipe_name}'
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in self.recipes:
            return f'ERRORE: {recipe_name} --> questa ricetta non esiste'
        if old_ingredient not in self.recipes[recipe_name]:
            return f'ERRORE: {old_ingredient} --> questo ingrediente non esiste nella ricetta {recipe_name}'
        self.recipes[recipe_name].remove(old_ingredient)
        self.recipes[recipe_name].append(new_ingredient)
        return f'Ingrediente {old_ingredient} sostituito con {new_ingredient} nella ricetta {recipe_name}'

    def list_recipes(self):
        if not self.recipes:
            return 'nessuna ricetta trovata'
        return f'ricette disponibili: {",".join(self.recipes.keys())}'
    
    def list_ingredients(self, recipe_name):
        if recipe_name not in self.recipes:
            return f'ERRORE: {recipe_name} questa ricetta non esiste'
        return {'ricetta': recipe_name, 'ingredienti': list(self.recipes[recipe_name])}
    
    def search_recipe_by_ingredient(self, ingredient):
        found_recipes = [name for name , ingredients in self.recipes.items() if ingredient in ingredients]
        if not found_recipes:
            return {'errore': f'nessuna ricetta trovata con l\'ingrediente {ingredient}'}
        return {'ricette_con_ingrediente': ingredient, 'ricette': found_recipes}

 	

manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))
"""

# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
# Attributi:

#     marca (stringa)
#     modello (stringa)
#     anno (intero)

# Metodi:

#     __init__(self, marca, modello, anno): 
# metodo costruttore che inizializza gli attributi marca, modello e anno.
#     descrivi_veicolo(self): 
# metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     numero_porte (intero)

# Metodi:

#     __init__(self, marca, modello, anno, numero_porte): 
# metodo costruttore che inizializza gli attributi della classe base e numero_porte.
#     descrivi_veicolo(self): 
# metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, 
# nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

# Metodi:

#     __init__(self, marca, modello, anno, tipo): 
# metodo costruttore che inizializza gli attributi della classe base e tipo.
#     descrivi_veicolo(self): 
# metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, 
# nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".

"""
class Veicolo:
    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca 
        self.modello = modello
        self.anno = anno


    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte:int):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}')

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo:str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')


	
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo()
auto.descrivi_veicolo()
moto.descrivi_veicolo()
"""

# Obiettivo
# L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali 
# usando la programmazione orientata agli oggetti in Python.

# Descrizione del problema
# Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. 
# Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
# - In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
# - n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
# Specifiche tecniche
# 1. Classe Specie

# - Attributi:
# nome (str): Nome della specie.
# popolazione (int): Popolazione iniziale.
# tasso_crescita (float): Tasso di crescita annuo percentuale.
# - Metodi:
# __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): 
# Costruttore per inizializzare gli attributi della classe.
# cresci(self): 
# Metodo per aggiornare la popolazione per l'anno successivo.
# anni_per_superare(self, altra_specie: 'Specie') -> int: 
# Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
# getDensita(self, area_kmq: float) -> int: 
# Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².
 
# 2. Sottoclassi BufaloKlingon e Elefante

# Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie 
# e devono inizializzare il nome della specie rispettiva.
 
# Formule Matematiche:
# Aggiornamento della popolazione per l'anno successivo:
# Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
# Calcolo della densità di popolazione:
# Formula: popolazione / area_kmq
# Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
# Calcolo degli anni necessari per superare la popolazione di un'altra specie:
# Hint: 
# Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie 
# finché la popolazione di questa specie non supera quella dell'altra. 
# Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000. 


class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione_iniziale
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione *= (1 + self.tasso_crescita / 100)

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 0
        popolazione_self = self.popolazione
        popolazione_altra = altra_specie.popolazione
        while popolazione_self <= popolazione_altra and anni < 1000:
            popolazione_self *= (1 + self.tasso_crescita / 100)
            popolazione_altra *= (1 + altra_specie.tasso_crescita / 100)
            anni += 1
        return anni if anni < 1000 else -1

    def getDensita(self, area_kmq: float) -> int:
        anni = 0
        popolazione_self = self.popolazione
        while popolazione_self / area_kmq < 1 and anni < 1000:
            popolazione_self *= (1 + self.tasso_crescita / 100)
            anni += 1
        return anni if popolazione_self / area_kmq >= 1 else -1


class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__('Bufalo Klingon', popolazione_iniziale, tasso_crescita)


class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__('Elefante', popolazione_iniziale, tasso_crescita)


# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")











