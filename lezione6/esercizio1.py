class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

alice = Person ("Alice W.", 45)
bob = Person ("BOb M.", 36)

print(f"name= {bob.name}")

if bob.age < alice.age:
    print(f"Il piu vecchio è {alice.name}")

francesco = Person ("Francesco B.", 20)
giulio = Person ("Giulio K.",60)
alessia = Person ("Alessia l.", 18)
lista:list[str,int]=[alice,bob,francesco,giulio,alessia]

c=None
for persone in lista:
    if c==None:
        c=persone.age
    elif c>persone.age:
        c=persone.age
print(c)