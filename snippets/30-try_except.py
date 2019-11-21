def divisione(x,y):
    try:
        return x // y
    except ZeroDivisionError:
        print("Non posso dividere per 0!")
        # Se non ritorno nulla, automaticamente ritorna None

print(divisione(12,4))
print(divisione(12,0))