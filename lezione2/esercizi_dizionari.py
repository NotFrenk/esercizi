
"""
We have a menu at a restaurant.
The available dishes are: pasta, pizza, salad, wine, water
Their prices are: 10.50, 9.00, 6.50, 4.00, 2.30
1. Save this information into a dictionary called menu.
2. From menu, access the prices of pasta and wine. Save them in separate variables.
3. Print the prices of pasta and wine.ù
"""
menù:dict ={
    "pasta":10.50,
    "pizza":9.00,
    "insalata":6.50,
    "vino":4.00,
    "acqua":2.30
    }
prezzo_pasta=menù["pasta"]
prezzo_vino=menù["vino"]
print("prezzo pasta:", prezzo_pasta)
print("prezzo del vino:",prezzo_vino)