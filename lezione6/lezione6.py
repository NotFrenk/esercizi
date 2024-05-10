#Francisco Felici

#9-1. 
#Restaurant: 
#Make a class called Restaurant. 
#The __init__() method for Restaurant should store two attributes: 
#a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
"""
class Food:

    

    def __init__(self, dish_name: str, price: float, available: bool = True):

        self.dish_name: str = dish_name.lower()

        self.price: float = price

        self.available: bool = available

        

    def change_price(self, new_price: float):

        self.price = new_price

    

    def switch_availability(self):

        self.available = not self.available

        

    def __str__(self) -> str:

        return f'Food(dish={self.dish_name}, price={self.price})'

        

class Menu:

    

    def __init__(self, foods: list[Food] = []):

        self.foods: list[Food] = foods

        

    def add_food(self, food: Food):

        if food.available:

            is_in: bool = False

            for food_in_menu in self.foods:

                if food_in_menu.dish_name == food.dish_name:

                    is_in = True

                    break

            if not is_in:

                self.foods.append(food)

        

    def remove_food(self, food: Food):

        self.foods.remove(food)

        

    def clean_menu(self):

        foods_temp: list[Food] = self.foods

        for food in foods_temp:

            if not food.available:

                self.remove_food(food)



class Restaurant:

    

    def __init__(self,

                 name: str,

                 cuisine_type: str,

                 number_served: int = 0,

                 open: bool = False):

        

        self.name: str = name

        self.cuisine_type: str = cuisine_type

        self.number_served: int = number_served

        self.open: bool = open

        self.menu: Menu = Menu()

        

    def open_restaurant(self):

        print(f'Il ristorante {self.name} è aperto')

        self.open = True

        

    def increment_number(self):

        if self.open:

            self.number_served += 1

        

    def close_restaurant(self):

        self.number_served = 0

        self.open = False

        

    def add_item(self, food: Food):

        self.menu.add_food(food)

        

    def remove_item(self, food: Food):

        self.menu.remove_food(food)

        

    def clean_menu(self):

        self.menu.clean_menu()

        

        

r1 = Restaurant(name="La Vecchia Roma", cuisine_type="Romana")

carbonara = Food(dish_name="Carbonara", price=10.5)

pizza_margherita = Food(dish_name="Pizza Margherita", price=8)

r1.add_item(carbonara)

r1.add_item(pizza_margherita)

print(r1.menu.foods)

carbonara.switch_availability()

r1.clean_menu()

print(r1.menu.foods)

r1.add_item(carbonara)

carbonara.switch_availability()

r1.add_item(carbonara)

print(r1.menu.foods)
print(" ")
"""

#9-3. Users: Make a class called User. 
#Create two attributes called first_name and last_name, 
#and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.
#//////////AND
#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
#Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

"""
class User:
    def __init__(self, first_name: str,last_name:str, age:int,height:float):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.height = height
        self.attempts = 0
        


    def greet_user(self):
        print(f"Hi {self.name}, how are you?")


    def increment_login_attempts(self):

        self.attempts += 1
        


    def reset_login_attempts(self):
        
        self.attempts = 0
        


    def __str__(self) -> str:
        return f"User={self.name,self.surname}, age ={self.age}, height ={self.height} m"

    


lorenzo = User("Lorenzo", "Maggi", 22, 1.80)
print(lorenzo) 
lorenzo.greet_user()
lorenzo.increment_login_attempts()
print(lorenzo)
lorenzo.reset_login_attempts()
print(lorenzo)
lorenzo.increment_login_attempts()
lorenzo.increment_login_attempts()
lorenzo.increment_login_attempts()
lorenzo.increment_login_attempts()
lorenzo.increment_login_attempts()
print(lorenzo.attempts)
lorenzo.reset_login_attempts()
print(lorenzo.attempts)
print(" ")
"""


#-------------------------------------------------------------------------------------------------------------
#9-6. 
#Ice Cream Stand: 
#An ice cream stand is a specific kind of restaurant. 
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 
#or Exercise 9-4. Either version of the class will work; 
#just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. 
#Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 
"""
class IceCreamStand(Restaurant):
    def __init__(self, name: str,cuisine_type: str,flavors: str , number_served: int = 0, open: bool = False):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("-", flavor)

ice_cream_stand = IceCreamStand("Scoops & More", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint Chip"])

ice_cream_stand.display_flavors()

print(" ")
"""

#-------------------------------------------------------------------------------------------------------------
#9-7. 
#Admin: 
#An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
#Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 
"""
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, height: float, privileges: list[str]):
        super().__init__(first_name, last_name, age, height)
        self.privileges = privileges

    def show_priviliges(self):
        print("Here are your privileges: ")
        for i in self.privileges:
            print(i)


admin_privileges = Admin("Lorenzo","Maggi",22,1.80,["can add post", "can delete post", "can ban user", "can promote user", "can delete all"])
admin_privileges.show_priviliges()
"""

#-------------------------------------------------------------------------------------------------------------
#9-8. 
#Privileges: Write a separate Privileges class. 
#The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
#Create a new instance of Admin and use your method to show its privileges.
"""
class Privileges:
    def __init__(self, privileges: list[str]):
        self.privileges = privileges

    def show_privileges(self):
        print("Here are your privileges:")
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, height: float, privileges: list[str]):
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges(privileges)

admin_privileges = Admin("Oussama", "Hliwa", 22, 176, ["can add post", "can delete post", "can ban user", "can promote user", "can delete all"])
admin_privileges.privileges.show_privileges()
"""


#-------------------------------------------------------------------------------------------------------------
#9-10. 
#Imported Restaurant: 
#Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. 
#Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
