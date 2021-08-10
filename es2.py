#Scrivere un programma che chieda all'utente di indovinare una password ma che
#dia solo 3 possibilità, fallite le quali il programma termina stampando:
#"E troppo complicato per voi"


#Scrivere un programma che chieda due numeri.Se la somma dei due numeri supera
# 100,stampate:"Numero troppo grande"


#Srivere un programma che chieda all'utente il nome.Se il nome è il vostro,
#il programma dovrà rispondere con un "Questo è un bel nome".Se il nome inserito
#è "John Cleese" o "Michel Palin" il programma dovrà rispondere con una battuta
# ;) mentre tutti gli altri casi l'output del programma sarà un semplice
#"Tu hai un bel nome!"
##ESERCIZIO 1
print('-'*10+'ES. 1'+'-'*10)
psw='livuoiqueiK1W1?'
counter=0
tentativo=''
while counter<3:
    tentativo=input(f'inserire la password, {3-counter} tentativi rimasti\n')
    if  tentativo==psw: 
        print("sei dentro")
        break
    counter+=1
else:print("E troppo complicato per voi")
##esercizio 2
print('-'*10+'ES. 2'+'-'*10)
a, b=-1,-1
while 1:    
    while 1:
        try: 
            a, b=[int (x) for x in input('inserisci due numeri interi\n').split()]   
            break
        except ValueError: print('\npreferirei due interi, grazie')
    
    if a+b>100: print("Numero troppo grande")
    else:
        print(a+b)
        break
##ESERCIZIO 3
print('-'*10+'ES. 3'+'-'*10)
nome=input('inserisci un nome\n').lower()
if nome=='andrea':print("Questo è un bel nome")

elif nome in ["John Cleese" , "Michel Palin"]:
     print('un uomo entra in un cafè. Splash')

else: print("Tu hai un bel nome!")