    # Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

def frequency_dict(elements: list):

    dizionario = {}

    for cibo in elements:
        if cibo in dizionario:
            dizionario[cibo] += 1
        else:
            dizionario[cibo] = 1
    return dizionario
    


print(frequency_dict(['mela', 'banana', 'mela']))