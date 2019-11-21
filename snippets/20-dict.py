
dizionario = {
    "nome": "Python",
    "versione": 3.8,
    ("test","1"): True,
    "dizionario": {
            5: [False,True]
    }
}

print(dizionario)
print(dizionario["nome"])
print(dizionario['versione'])
print(dizionario[("test","1")])
print(dizionario["dizionario"])
print(dizionario["dizionario"][5])
print(dizionario["dizionario"][5][0])
