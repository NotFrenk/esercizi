# Classe del Account:
#     Attributi:
#         account_id: str - identificatore univoco per l'account.
#         balance: float - il saldo attuale del conto.
#     Metodi:
#         deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#         get_balance(): restituisce il saldo corrente del conto.
# Classe Bank:
#     Attributi:
#         accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#     Metodi:
#         create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#         deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#         get_balance(account_id): restituisce il saldo del conto con l'ID specificato.


class Account:
    def __init__(self, account_id:str):
        self.account_id = account_id
        self.balance:float = 0.0

    def deposit(self, amount: float):
        self.balance += amount
      
        
    def get_balance(self):
        return int(self.balance)

        
class Bank:
    def __init__(self):
        self.accounts:dict[str, Account] = {}

    def create_account(self, account_id):
        if account_id in self.accounts.keys():
            print('Account with this ID already exists')
        else:
            self.accounts[account_id] = Account(account_id)
        return self.accounts[account_id]

    def deposit(self, account_id, amount):
        if account_id in self.accounts.keys():
            self.accounts[account_id].deposit(amount)
        else:
            print('account non trovato')
            
    def get_balance(self, account_id):
        if account_id in self.accounts.keys():
            return self.accounts[account_id].get_balance()
        else:
            print('Account not found')
        
        
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

 	

bank = Bank()
try:
    bank.get_balance("456")
except ValueError as e:
    print(e)