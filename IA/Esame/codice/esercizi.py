import pandas as pd

custumers = pd.read_csv("/home/user/Scrivania/FullStack/esercizi/IA/Esame/dati/retail/customer.csv")
products = pd.read_csv("/home/user/Scrivania/FullStack/esercizi/IA/Esame/dati/retail/product.csv")
transactions = pd.read_csv("/home/user/Scrivania/FullStack/esercizi/IA/Esame/dati/retail/transaction.csv")


custumers.rename(columns={"Col1": "CustomerID", "Col2": "Country"}, inplace=True)
products.rename(columns={"Col1": "StockCode", "Col2": "Description"}, inplace=True)

print(custumers.head())
print(products.head())
print(transactions.head())

merge_df = pd.merge(custumers, transactions, on ="CustomerID", how="inner")
print(merge_df.head())

