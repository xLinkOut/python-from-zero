def adiacenti(n): # Funzione
	return n-1,n+1  # Ritorna due valori
print(adiacenti(5)) # E' una tupla!
x,y = adiacenti(5) # I valori restituiti
print(x)          # vengono assegnati in ordine
print(y)
