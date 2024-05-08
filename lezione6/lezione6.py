#Francisco Felici

#9-1. 
#Restaurant: 
#Make a class called Restaurant. 
#The __init__() method for Restaurant should store two attributes: 
#a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


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
#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
#and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.


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