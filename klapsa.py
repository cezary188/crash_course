usernames = ['Mariusz', 'Sanczo', 'Michal', 'Sandra']

if usernames:											#w tym warunku po samym wpisaniu NAZWY listy python sam sprawdza czy jest  pusta jak tak to przechodzi do korespondujacego else na dole
	for powitanie in usernames:
		if powitanie =='Sandra':
			print("Witaj Zlotko, chcesz klapsa ?")
		else:
			print("Witaj " + powitanie)
else:
	print("Ale jak to pusta ?")