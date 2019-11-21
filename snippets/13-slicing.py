s = "Python" # Dichiaro la stringa s
# stringa[inizio:fine]
print(s[1:-2]) 	# Da s[1] a s[-2] (=s[3])
print(s[-1:2]) 	# Non è possibile "reversare" la stringa
print(s[-1:-3]) # Appunto...
print(s[-3:-1]) # Da s[-3] (=s[3]) a s[-1] (=s[5])
print(s[3:5]) 	# Come sopra ma con indici positivi
print(s[-3:5]) 	# Un altro modo ancora...
print(s[-2:1]) 	# Se lo slicing è incompatibile, ritorna una stringa vuota
print(s[5::-1]) # Extended Slices 
