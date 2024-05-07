class Food:
    def __init__ (self, name:str, price:float, description:str):
        self.name=name
        self.price=price
        self.description=description

    def __str__(self):
        return f" {self.name.capitalize{}}(prive={self.price}, description{self.description})"

cibo1=Food ("lasagna", 5.00, "molto buona, il mio cibo preferito")
cibo2=Food ("patate fritte", 2.50, "le patane so sempre bone")
cibo3=Food ("cioccolato", 3.00, None)

class Menu:
    def __init__ (self, lista_food:list[Food]=[0]):
        self.lista_food:list[Food]=lista_food

    def add_food (self, food:Food):
        self.food.append(food)
    
    def remove_food (self, food:Food):
        if food is self.lista_food:
            self.food.remove(food)

    def __str__(self):
        repr:str=""
        for food in self.lista_food:
            repr+="\n"+str(food)
        return repr[1:]
    


    