usernames = ['snv', 'abraabra', 'noweki', 'masta5', 'cezary188']

print ("Wybierz login ")
login = input()

if login:
    for zajete in usernames:
        if login == zajete:
            print ("nazwa juz zajeta, wybierz inna !")
        else:
            print ("Login wolny")
                                                                   #zatrzymuje petle inaczej dostaniemy tyle
                                                                        #komunikatow "Login wolny ile jest wpisow w bazie

else:
    print ("Nie wpisales loginu !")