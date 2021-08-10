nomefile=''
#testo_f=open(nomefile).read()
testo_f='ho fatto la cacca'
testo=set(testo_f.replace("'","' ").split())
scores={'cacca':0, 'la':1}
ans=sum(scores[n] for n in testo if n in scores)
print(ans)