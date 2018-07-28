zbanowani = ['kurczelapki', 'carolina', 'mateousz', 'cezary']

print ("Sprawdz czy zbanowany ?")
user = input()

if user not in zbanowani:
    print (user.title()+ " Mozesz pisac do woli :)")


else:
    print (user.title() + " Ty kanalio ! Poszedl won !")

print ("\n Czy chcesz sie dodac do listy za free ? \n Yes or No ?")
yn = input()

if yn == 'Yes':

        zbanowani.append(user)
        print (" Dodano " + user.title() + ", milej zabawy, badz nie :P")
else:
        print ("No dobra okey.. :(")
print("\noto lista: \n")
print (zbanowani)