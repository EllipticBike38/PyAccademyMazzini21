
file_testo=open('./tetso greco/testo_greco.txt', encoding='utf-8')

ans_en=''
ans_it=''


testo=file_testo.readlines()
t_dritto=[]
rev=False
for linea in testo:
    if linea=='':continue
    if rev==False:
        rev=True
        t_dritto.append(linea)
    if rev:
        t_dritto.append(linea[::-1])


gr_en=dict()
en_it=dict()
gr_en_file=open('./tetso greco\Vocabolario_greco-inglese.csv', encoding='utf-8')
#gr_en_file=open('./tetso greco\diction.csv', encoding='utf-8')
en_it_file=open('./tetso greco\Vocabolario_inglese-italiano.csv', encoding='utf-8')
e_i_p=en_it_file.read()

en_it_file.seek(0)
for l in gr_en_file.readlines():
    k=l[:l.index(';')]
    supp=l[l.index(';')+1:]
    if ';' in supp:
        supp=supp.rstrip('\n')
        for el in supp.split(';'):
            if el in e_i_p:
                gr_en[k]=el
                break
        else:  gr_en[k]=supp[0]
    else:
        en=supp[:supp.index('\n')]
        gr_en[k]=en



for l in en_it_file.readlines():
    k=l[:l.index(';')]
    supp=l[l.index(';')+1:]
    if ';' in supp:
        supp=supp.rstrip('\n')
        for el in supp.split(';'):
            if el in e_i_p:
                en_it[k]=el
                break
        else:  en_it[k]=supp[0]
    else:
        en=supp[:supp.index('\n')]
        en_it[k]=en





PUN=',.:;\n\''
for linea in t_dritto:
    for parola in linea.split():
        try:
            parola=parola.lower()
            if parola.rstrip(PUN)==parola:
                ans_en+=gr_en[parola]+' '
            else:
                pparola=parola.rstrip(PUN)
                simb=parola[len(pparola):]
                ans_en+=gr_en[ pparola]+simb+' '
        except KeyError:
            pass
        ans_en+='[unavailable]'
a=''
while a!=ans_en:
    a=ans_en
    ans_en=ans_en.replace('[unavailable][unavailable]','[unavailable]')
ans_en=ans_en.replace('[unavailable]','[...] ')
print(ans_en+'\n')
en_m=ans_en.replace('[unavailable]','')+''
for k in en_it.keys():
        if k in en_m:
            en_m=en_m.replace(' '+k+' ',' '+en_it[k].upper()+' ')
            en_m=en_m.replace(' '+k+',',' '+en_it[k].upper()+',')

        pass
#print(gr_en)
print(en_m)