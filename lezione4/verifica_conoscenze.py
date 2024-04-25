"""
#1
Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i tuoi sospettati. La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!

Qual è il problema?

Non puoi semplicemente confrontare le stringhe lettera per lettera. Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t). Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).

Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e t (la folla) come input. Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. Altrimenti restituisce False. Dimostra le tue abilità da detective e svela la verità nascosta!

For example:

Test	Result
print(is_subsequence("abc", "ahbgdc"))
True
print(is_subsequence("axc", "ahbgdc"))
False

#2
Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). Questi gioielli hanno vari valori, alcuni più preziosi di altri. Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.

Qual è la svolta?

Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). A noi però interessano solo valori distinti, ovvero gioielli con valori unici.

Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). Se nello scrigno sono presenti almeno tre valori distinti, la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.

Ma c'è un problema!

Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.

For example:

Test	Result
print(third_max([3, 2, 1]))
1
print(third_max([1, 2]))
2
print(third_max([2, 2, 3, 1]))
1


#3
Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

Esempio:

construct_rectangle(4)

L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.

For example:

Test	Result
print(construct_rectangle(4))
[2, 2]


#4
Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). 
La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note. Ricorda, 
una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.

Colpire le note giuste:

Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], 
la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. 
La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).


"""
def find_lhs(nums: list[int]) -> int:
    duplicates_with_counts = []    #i create a list for the final output 
    seen = []                      #another list for count how many times are repeated the numbers in "nums"
# i add in "seen" the repeated numbers
    for i in nums:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 0
    
#counting the numbers in "seen"
    for i, count in seen.items():
        if count > 1:
            duplicates_with_counts.append([i, count]) #adding the counted numbers in "duplicates_with_counts"
        else:
            print("NO")
    print(duplicates_with_counts)
    return find_lhs

"""
#5
Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

For example:

Test	
stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
print(word_frequency(text, stopwords))

soluzione
{'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}
"""
