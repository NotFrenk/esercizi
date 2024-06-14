
### CLASSE: Paziente
# Creare un file chiamato "paziente.py".
# In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

# Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo 
# (si usi il tipo String).
# - Definire i seguenti metodi:

#     costruttore della classe paziente, il quale richiede in input il codice identificativo, 
# il quale deve essere un attributo privato.

#     setIdCode(idCode): consente di impostare il codice identificativo del paziente.

#     getidCode(): consente di ritornare il codice identificativo del paziente.

#     patientInfo(): stampa in output le informazioni del paziente in questo modo:

#         "Paziente: {nome} {cognome}
#          ID: {codice identificativo}"

from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, idCode):
        super().__init__(first_name, last_name)
        
        if isinstance(idCode, str):
            self.__idCode = idCode
        else:
            self.__idCode = None
            print("Il codice identificativo inserito non è una stringa!")

    def setIdCode(self, idCode):
        if isinstance(idCode, str):
            self.__idCode = idCode
        else:
            print("Il codice identificativo inserito non è una stringa!")

    def getidCode(self):
        return self.__idCode
    
    def patientInfo(self):
        if self.__idCode is not None:
            print(f"Paziente: {self.getName()} {self.getLastname()} \n ID: {self.__idCode}")
        else:
            print("Informazioni incomplete sul paziente!")


# paziente = Paziente("Marco", "Bianchi", "123456")
# paziente.greet()
# paziente.patientInfo()
# paziente.setIdCode(789)  # Errore: Il codice identificativo inserito non è una stringa!
# paziente.setIdCode("789012")
# print(paziente.getidCode())  # 789012
# paziente.patientInfo()