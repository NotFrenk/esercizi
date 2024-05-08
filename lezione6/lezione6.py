class Restaurant:
    def __init__(self, name:str, cuisin_type:str):
        self.name: str = name
        self.cuisin_type: str = cuisin_type
    
    def describe_restourant(self):
        print(f"Restaurant(Name={self.name},"\
              + f"cusine={self.cuisin_type})")
        
    def open_restaurant(self):
        print(f"il ristorante {self.name} è aperto")

        #da finire



#----------------------------------------------------------------------------------------------------

class Utente:

    def __init__ (self,
                  first_name:str,
                  second_name:str,
                  age:str,
                  cf:str,
                  email:str):
        
        self.first_name : str = first_name
        self.second_name : str = second_name
        self.age : int = age
        self.cf : str = cf
        self.email : str = email

    def __str__ (self):
        return f"user(name={self.first_name},"\
            +f"surname={self.second_name})"

user1 = Utente(
    first_name="lorenzo"
    second_name="maggi"
    age=
)

print(user1)

#da finire