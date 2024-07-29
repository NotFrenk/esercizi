#Scrivi una funzione che, data una lista di parole, ritorni un dizionario che mappa ogni parola alla sua lunghezza.

"""def mappa_parole_a_lunghezza(words: list) -> dict:


print(mappa_parole_a_lunghezza(["apple", "banana", "cherry"]))
"""


#Scrivi una funzione che accetti tre parametri: user, passw e stato dell'account (attivo/non attivo). 
# L'accesso è consentito solo se il nome utente è "manager", la password corrisponde a "67890" e l'account è attivo (True). 
# La funzione ritorna "Ingresso consentito" oppure "Ingresso negato".
"""
def verifica_accesso(user: str, passw: str, stato: bool) -> str:
    if user == 'manager' and passw == '67890' and stato == True:
        return 'Ingresso consentito'
    else:
        return 'Ingresso negato'






print(verifica_accesso("manager", "67890", True))
print(verifica_accesso("manager", "wrongpassword", True))
"""





#Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un dato valore intero definito threshold.

"""
def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
    lista = []
    
    for numero in numbers:
        if numero < threshold:

            




print(moltiplica_numeri([1, 10, 20, 30], 30))

"""



# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di elettrodomestici.
 
# 1. Classe Base: Elettrodomestico
# Crea una classe base chiamata Elettrodomestico con i seguenti attributi e metodi:
 
# Attributi:

#     marca: str
#     modello: str
#     potenza: int

# Metodi:

#     __init__(self, marca: str, modello: str, potenza: int): metodo costruttore che inizializza gli attributi marca, modello e potenza.
#     descrivi_elettrodomestico(self): metodo che stampa una descrizione dell'elettrodomestico nel formato "Marca: 
#           {marca}, Modello: {modello}, Potenza: {potenza}W"

# 2. Classe Derivata: Frigorifero
# Crea una classe derivata chiamata Frigorifero che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:

# Attributi:

#     capacità: int

# Metodi:

#     __init__(self, marca: str, modello: str, potenza: int, capacità: int): 
#           metodo costruttore che inizializza gli attributi della classe base e capacità.
#     descrivi_elettrodomestico(self): 
#           metodo che sovrascrive quello della classe base per includere anche la capacità nella descrizione, nel formato "Marca: {marca}, 
#           Modello: {modello}, Potenza: {potenza}W, Capacità: {capacità}L"

# Classe Derivata: Lavatrice
# Crea una classe derivata chiamata Lavatrice che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:

# Attributi:
# - carico_max: int

# Metodi:
# - __init__(self, marca: str, modello: str, potenza: int, carico_max: int): metodo costruttore che inizializza gli attributi della classe base e carico_max.
# - descrivi_elettrodomestico(self): 
#       metodo che sovrascrive quello della classe base per includere anche il carico massimo nella descrizione, nel formato "Marca: {self.marca}, Modello: {modello}, Potenza: {potenza}W, Carico massimo: {carico_max}kg".


"""class Elettrodomestico:
    def __init__(self, marca: str, modello: str, potenza: int):
        self.marca: str = marca
        self.modello: str = modello
        self.potenza: int = potenza

    def descrivi_elettrodomestico(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W')


class Frigorifero(Elettrodomestico):
    def __init__(self, marca: str, modello: str, potenza: int, capacità: int):
        super().__init__(marca, modello, potenza)
        self.capacità = capacità

    def descrivi_elettrodomestico(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Capacità: {self.capacità}L')


class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, potenza: int, carico_max: int):
        super().__init__(marca, modello, potenza)
        self.carico_max = carico_max

    def descrivi_elettrodomestico(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Carico massimo: {self.carico_max}kg')
"""











# 1. Classe ContactManager:
# Gestisce tutte le operazioni legate ai contatti.
 
# Attributi:

#     contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per valore una lista di numeri di telefono. 
#                                      I numeri di telefono sono espressi sottoforma di stringa.

# Metodi:

#     create_contact(name: str, phone_numbers: list[str]): 
#       Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri di telefono. 
#       Restituisce un nuovo dizionario con il solo contatto appena creato o il messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.

#     add_phone_number(contact_name: str, phone_number: str): 
#       Aggiunge un numero di telefono al contatto specificato. 
#       Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." 
#       se il contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero di telefono è già presente per il contatto specificato.

#     remove_phone_number(contact_name: str, phone_number: str): 
#       Rimuove un numero di telefono dal contatto specificato. 
#       Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." 
#       se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.

#     update_phone_number(contact_name: str, old_phone_number: str, new_phone_number: str): 
#       Sostituisce un numero di telefono con un altro nel contatto specificato. 
#       Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." 
#       se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.

#     list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.

#     list_phone_numbers(contact_name: str): 
#       Mostra i numeri di telefono di un contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di errore "Errore: il contatto non esiste." 
#       se il contatto non esiste.

#     search_contact_by_phone_number(phone_number: str): 
#       Trova e restituisce tutti i contatti che contengono un determinato numero di telefono. 
#       Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato tra i valori 
#       oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono." se nessun contatto contiene il numero di telefono.

class ContactManager:
    def __init__(self):
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self, name: str, phone_numbers: list[str]):
        if name in self.contacts:
            return "Errore: il contatto esiste già."
        self.contacts[name] = phone_numbers
        return {name: self.contacts[name]}
    
    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            return 'Errore: il contatto non esiste.'
        if phone_number in self.contacts[contact_name]:
            return 'Errore: il numero di telefono esiste già.'
        self.contacts[contact_name].append(phone_number)
        return {contact_name:self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            return 'Errore: il contatto non esiste.'
        if phone_number not in self.contacts[contact_name]:
            return 'Errore: il numero di telefono non è presente.'
        self.contacts[contact_name].remove(phone_number)
        return {contact_name:self.contacts[contact_name]}

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contacts:
            return 'Errore: il contatto non esiste.'
        if old_phone_number not in self.contacts[contact_name]:
            return 'Errore: il numero di telefono non è presente.'
        index = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number
        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self):
        return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str):
        if contact_name not in self.contacts:
            return 'Errore: il contatto non esiste.'
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str):
        # result = {name:phone_numbers for name, phone_numbers in self.contacts.items() if phone_number in phone_numbers}
        # if not result:
        #     return 'Nessun contatto trovato con questo numero di telefono.'
        # return result
    
        #lista = [name for name in self.contacts.items() if phone_number in nam]

        for name, valu in self.contacts.items():

            if valu != phone_number:
                return 'Nessun contatto trovato con questo numero di telefono.'
            print(name)     
        


 	

# Creazione di un nuovo gestore di contatti
manager = ContactManager()
# Creazione di nuovi contatti
print(manager.create_contact("Alice", ["123456789"]))
print(manager.create_contact("Bob", ["987654321"]))
print(manager.create_contact("Charlie", ["999999999"]))

print(manager.update_phone_number("Bob", "987654321", "999999999"))

# Ricerca di contatti per numero di telefono
print(manager.search_contact_by_phone_number("999999999"))

        

       



