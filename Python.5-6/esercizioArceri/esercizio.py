import dbclient as db
cur = db

print("Cosa vuoi fare? ")
print("         1: SCRITTURA")
print("         2: LETTURA") 
print("         3: EXIT ")

ris = input("decidi operazione")

while ris != "3":

    if ris == "1":
        sQuery = input("inserisci la tua query:\n")
        res = db.write_in_db(cur, sQuery)

        if (res ==0):
            print("Query eseguita")
        else:
            print("Query non valida")
    elif ris == "2":
        sQuery = input("inserisci la tua query:\n")
        res = db.read_in_db(cur, sQuery)

        if (res == -1):
            print("Query non valida")
        else:
            if res ==0:
                print("nessun record\n")
            else:
                lRecord=db.read_next_row(cur)
                while lRecord [0]==0:
                    print(lRecord)
                    lRecord = db.read_next_row(cur)
                    

    else:
        print("\n Operazione non valida!!")
        ris = input("decidi operazione")
        print("         1: SCRITTURA")
        print("         2: LETTURA") 
        print("         3: EXIT ")