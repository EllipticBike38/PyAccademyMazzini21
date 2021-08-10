#Scrivere un programma che in un file di testo cerchi una parola data in input,
#ne conti le occorrenze e indichi in che riga occorre


##ESERCIZIO 1


'''while 1:
    print('-'*10+'ES. 1'+'-'*10)
    n_file='es3.txt'
    #w=input('parola da cercare:\t')
    w='gatto'
    print('parola di default "gatto"')
    righe=list()
    file=open(n_file,encoding='utf-8')
    a=file.readlines()
    for n,riga in zip(range(len(a)), a):
        riga=riga.lower()
        for car in riga:
            
            if car=="'":
                riga= riga.replace(car,'\' ')
            if car.isalnum is False :
                riga=riga.replace(car,' ')
        if w in riga:    righe.append(n)
    print(f'occorre in {len(righe)} righe: ',*map(lambda x:x+1,righe))'''



#Scrivere un programma che identifica i numeri all'interno di un file di testo e calcola
#a) le occorrenze delle cifre(da 1 a 9)
#b) i numeri con l'occorrenza minima
#c) i numeri con l'occorrenza massima

print('-'*10+'ES.2'+'-'*10)
n_file='es3B.txt'
righe=list()
nn={'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
counter=dict()
file=open(n_file,encoding='utf-8')
righe.extend([int(y) for y in x.split()] for x in file.readlines())
for riga in righe:
    for el in riga:
        for c in str(el):
            nn[c]+=1
        if str(el) not in counter.keys():
            counter[str(el)]=1
        else: counter[str(el)]+=1
nn.pop('0')
counter_l=list((k,v) for k,v in counter.items())

minn=min(counter_l, key= lambda x:x[1])
maxx=max(counter_l, key= lambda x:x[1])

min_l=list([c for c in counter_l if c[1]==minn[1]])
max_l=list([c for c in counter_l if c[1]==maxx[1]])

print(f'le occorrenze delle cifre da 1 a 9:\n',str(nn).replace(',',',\n') ,'\n\n\n'
f'Il valore massimo::\n\t',str(max_l).replace('),',')\n\t').removeprefix('[').removesuffix(']').replace('(','' ).replace(')','' ).replace(',',':'),'\n\n'
f'Il valore minimo:\n\t',str(min_l).replace('),',')\n\t').removeprefix('[').removesuffix(']').replace('(','' ).replace(')','' ).replace(',',':'),'\n\n')