# GDG Python Echo Bot
Piccolo bot di esempio utilizzato nel talk "Python from Zero".

## Creazione del bot su Telegram
1. Con il vostro account Telegram, cercare il bot [@BotFather](https://t.me/botfather)
2. Inviate il comando `/newbot`
3. Inserite un nome per il vostro bot: quello che vi piace di più!
4. Definite un nickname per il bot, che deve necessariamente finire con "bot" (es: "pythonbot")
5. Fatto! A questo punto BotFather vi darà un **Token**, salvato perchè andrà inserito nel codice sorgente.

[Qui](https://core.telegram.org/bots#6-botfather) ci sono informazioni aggiuntive su questa operazione.

## Configurazione

```bash
	# Scaricate la repository, con git o manualmente
	git clone https://github.com/xLinkOut/python-from-zero
	cd python-from-zero/bot
	# Installate le dipendenze
	pip install -r requirements.txt
	# Sostituire YOUR_TOKEN con il token del vostro bot datovi da BotFather
	sed 's/INSERT_TOKEN_HERE/YOUR_TOKEN/' -i Bot.py
	# Tutto pronto! Per eseguirlo...
	python3 Bot.py
```