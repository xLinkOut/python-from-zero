def somma(x, y=1): # Definiamo una funzione somma che
    return x + y   # prende due argomenti, di cui y = 1 di default.
print(somma(1,2))  # Chiamiamo la funzione con due parametri
risultato = somma(5,7) # Salviamo il risultato in una variabile
print(risultato)        # 
print(somma(5)) # Chiamiamo la funzione con un solo paramtro
operandi = [6,7] # Definiamo una lista di numeri
print(somma(operandi[0],operandi[1])) # Si ma... scomodo
print(somma(*operandi)) # "Esplode" in automatico la lista
operandi = {'x':6,'y':7} # Si può usare anche un dict
print(somma(**operandi)) # "Esplode" il dizionario assegnado
            # il valore di ogni chiave al 
            # parametro corrispondente
