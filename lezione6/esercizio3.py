class Animal:
    def __init__ (self, name: str, legs:int=0):
        self.name=name
        self.legs=legs

    def set_legs(self, new_legs:int):
        if new_legs>=0:
            self.legs=new_legs
        else:
            self.legs=0

    def get_legs(self):
        return self.legs
    
    def __str__ (self):
        return f"{self.name.capitalize{}}(legs={})"
        
animale= Animal ("Alex", 4)
animale2=Animal ("pippo", 2)

print(animale)
lista:list=[animale,animale2]
for i in lista:
     print(i)

