#Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
#Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
#in genere utilizzando tutte le lettere originali esattamente una volta.
#For example:
"""
def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    if len(s) != len(t):
        return False
    
    contatore_s = {}
    contatore_t = {}

    for lettera in s:
        if lettera in contatore_s:
            contatore_s[lettera] += 1
        else:
            contatore_s[lettera] = 1

    for lettera in t:
        if lettera in contatore_t:
            contatore_t[lettera] += 1
        else:
            contatore_t[lettera] = 1

    return contatore_s == contatore_t
        
print(anagram("anagram","nagaram"))
"""




#Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.
#La lista di interi è formata così:
#L'elemento in posizione 0 corrisponde alla radice
#Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, 
#significa che il nodo che corrisponde a quell'indice è una foglia.

#Potete utilizzare la classe TreeNode per crearvi prima l'albero - anziché usare la lista tree - 
#e poi visitare l'albero sfruttando gli oggetti di tipo TreeNode.


"""
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    pass







print(symmetric([1,2,2,3,4,4,3]))
"""





#Progettare un semplice sistema bancario con i seguenti requisiti:

    #Classe del Account:
        #Attributi:
            #account_id: str - identificatore univoco per l'account.
            #balance: float - il saldo attuale del conto.
        #Metodi:
            #deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            #get_balance(): restituisce il saldo corrente del conto.
    #Classe Bank:
        #Attributi:
            #accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        #Metodi:
            #create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            #deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            #get_balance(account_id): restituisce il saldo del conto con l'ID specificato.


"""
class Account:
    def __init__(self, account_id: str ):
        self.account_id = account_id
        self.balance = 0.0
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance+=amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def get_balance(self) -> float:
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id:str):
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")
        account = Account(account_id)    
        self.accounts[account_id] = account
        return account
        

    def deposit(self, account_id:str, amount:float):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist.")
        self.accounts[account_id].deposit(amount)
        return True
    
    def get_balance(self, account_id:str):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id].get_balance()
        




bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())


bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))


bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))
"""



#Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.

"""
class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    queue: list[ListNode] = [head]
    
    while queue:
        curr_node = queue.pop()
        if curr_node:
            reversed_list.append(curr_node.val)
            queue.append(curr_node.next)
    return reversed_list[::-1]

def reverse_recursive(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    _reverse(head, reversed_list)
    return reversed_list[::-1]

def _reverse(curr_node: ListNode, reversed_list: list[int]):
    if curr_node:
        reversed_list.append(curr_node.val)
        _reverse(curr_node.next, reversed_list)
        

head = ListNode(val=0, 
                next=ListNode(val=1, 
                              next=ListNode(val=5, 
                                            next=ListNode(val=6))))
print(reverse(head))
"""


# Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

#     Classe Book:
#         Attributi:
#             book_id: str - Identificatore di un libro.
#             title: str - titolo del libro.
#             author: str - autore del libro
#             is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
#         Metodi:
#             borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
#             return_book()- Contrassegna il libro come restituito.

#     Classe Member:
#         Attributi:
#             member_id: str - identificativo del membro.
#             name: str - il nome del membro.
#             borrowed_books: list[Book] - lista dei libri presi in prestito.
#         Metodi:
#             borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
#             return_book(book): rimuove il libro dalla lista borrowed_books.

#     Classe Library:
#         Attributi:
#             books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
#             members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
#         Methodi:
#             add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
#             register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
#             borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
#             return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
#             get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

"""
class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise ValueError("The book is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise ValueError("book is not borrowed")

class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self, book: Book):
        if book.is_borrowed:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise ValueError("Book not borrowed by this member")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
        else:
            raise ValueError("A book with this ID already exists in the library.")

    def register_member(self, member_id: str, name: str):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
        else:
            raise ValueError("A member with this ID is already registered.")

    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members:
            if book_id in self.books:
                member = self.members[member_id]
                book = self.books[book_id]
                member.borrow_book(book)

            else:
                raise ValueError("Book not found")
        else:
            raise ValueError("Member not found")

    def return_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)
        else:
            raise ValueError("Book ID or Member ID not found.")

    def get_borrowed_books(self, member_id: str) -> list:
        if member_id in self.members:
            borrowed_books = []
            for book in self.members[member_id].borrowed_books:
                borrowed_books.append(book.title)
            return borrowed_books
        else:
            raise ValueError("Member ID not found.")"""




# Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

#     Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#     Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#     Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

# Nota:

#     Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#     Solo le celle riempite devono essere convalidate secondo le regole menzionate.

"""
def sudoku(tavola: list[list[int]]) -> bool:
    rows: dict[int, list[int]] = {i: [] for i in range(9)}
    # rows = {0: [], 1: [], ... , 8: []}
    cols: dict[int, list[int]] = {i: [] for i in range(9)}
    squares: dict[int, list[int]] = {f'{i}-{j}': [] for i in range(3) for j in range(3)}
    # squares = dict[int, list[int]] = {i: [] for i in range(9)
    for i in range(9):
       for j in range(9):
           curr_elem: str = tavola[i][j]
           if curr_elem != '.':
                square_i, square_j = i // 3, j // 3
                # square_index = 3 * square_i + square_j
                # if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[square_index]
                if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[f'{square_i}-{square_j}']:
                    return False
                
                rows[i].append(curr_elem)
                cols[j].append(curr_elem)
                squares[f'{square_i}-{square_j}'].append(curr_elem)
                # squares[square_index].append(curr_elem)
    return True
                
# square_i = 0, square_j = 0 -> 0
# square_i = 0, square_j = 1 -> 1
# square_i = 0, square_j = 2 -> 2
# square_i = 1, square_j = 0 -> 3
# square_i = 1, square_j = 1 -> 4
# square_i = 1, square_j = 2 -> 5
# square_i = 2, square_j = 0 -> 6
# square_i = 2, square_j = 1 -> 7
# square_i = 2, square_j = 2 -> 8 ---> 3 * square_i + square_j
"""
