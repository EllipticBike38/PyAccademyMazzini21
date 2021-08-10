stringa='Questa è una frase di non molte parole e il numero 1234. lo sai?'

l_s=stringa.split()
simboli=[]
buffer=0
for i in range(len(l_s)):
     while l_s[i] is not '' and not l_s[i][0].isalpha() :
        if buffer:
             buffer-=1
             continue
        n=''.join([x for x in l_s[i] if not x.isalpha()])
        buffer=len(n)-1
        simboli.append((i,n))
        l_s[i]=l_s[i][1:]
     buffer=0
     while  l_s[i] is not '' and not l_s[i][-1].isalpha():
        if buffer:
             buffer-=1
             continue
        n=''.join([x for x in l_s[i] if not x.isalpha()])
        buffer=len(n)-1
        simboli.append((i,n))
        l_s[i]=l_s[i][1:]
     l_s[i]=' '+l_s[i][::-1]
simboli.sort(key=lambda x: x[0], reverse=True)
for el in simboli:
    l_s.insert(el[0],el[1])
s=''.join(l_s,)
print(simboli)
print (s)
