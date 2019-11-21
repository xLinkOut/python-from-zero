username = "Luca" 					# Stringa username
print("Ciao %s!" % username) 		# %-formatting (C-like)
print("Ciao {0}!".format(username)) # str.format()
print(f"Ciao {username}!") 			# <Formatted string literals>, disponibili in Python >= 3.6
