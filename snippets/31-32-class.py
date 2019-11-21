class Veicolo:

	numero_di_ruote = 0
	targa = ""

	def __init__(self, ruote):
		self.numero_di_ruote = ruote
		print(f"Creazione veicolo con {self.numero_di_ruote} ruote.")


	def immatricola(self, nuova_targa):
		self.targa = nuova_targa
		print(f"Immatricolato veicolo con targa {self.targa}.")


	def stampa_targa(self):
		print(self.targa)


veicolo = Veicolo(4)
veicolo.immatricola("AA123BB")
veicolo.stampa_targa()