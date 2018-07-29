usernames = ['Mariusz', 'Sanczo', 'Michal', 'Sandra']

if usernames:
	for powitanie in usernames:
		if powitanie =='Sandra':
			print("Witaj Zlotko, chcesz klapsa ?")
		else:
			print("Witaj " + powitanie)
else:
	print("Ale jak to pusta ?")