a=open('Brano.txt')
k= a.read().split('.')
b=open('Vocabolario.txt').read()
print(type(b))

def ricerca_dato_nome(stringa:str, file_letto_splittato:list):
    ans=list()
    for i in file_letto_splittato:
        if stringa in i: ans.append(k.index(i))
    return ans    
 
def ricerca_dati_file(vocabolario_letto:str, file_letto_splittato:list):
    ans=list()
    for i in vocabolario_letto.split('\n'):
        ans.append(ricerca_dato_nome(i, file_letto_splittato))
    return ans

if __name__=='__main__':
    ans=ricerca_dati_file(b,k)
    c=b.split('\n')
    for j in c:
        for j2 in c:
            if j!=j2 and j in j2:
                for el in ans[c.index(j2)]:
                    if el in ans[c.index(j)]:
                        ans[c.index(j)].remove(el)
    for stringa,el in zip(c, ans):
        print('\n\n'+stringa+'\n',*el)
        if len(el)>0:
            sort_a=sorted([(el1, k[el1]) for el1 in el], key=lambda x: len(x[1]), reverse=True)[0]
            print('\t',sort_a[0],'-->',sort_a[1])