# Data una stringa di numeri, convertirla in lettere.
# input: 123…
# Output: Uno due tre….

# Implementare un codec per alfabeto morse, sia da file che da tastiera.
# L’utente inserisce una frase in codice morse ed il programma la converte in linguaggio naturale e viceversa.

# Implementare il gioco della battaglia navale: il computer genera delle posizioni
#  casuali delle navi che il giocatore deve indovinare entro un certo numero di tentativi.

##es6
'''print('-'*10+'ES. 6'+'-'*10)
nn={'1':'uno','2':'due','3':'tre','4':'quattro','5':'cinque','6':'sei','7':'sette','8':'otto','9':'nove','0':'zero'}
str_in=input('dammi una stringa di numeri\n\n')
#str_in='78pj89'; print( 'stringa di numeri di default: ',str_in)
c=str_in.__iter__()

while 1:
    try:
        a=c.__next__()
        if a in nn:
            print(nn[a], end=' ')
            continue
        print(f'({a} non è un numero)', end=' ')
    except StopIteration:
        print(f'\n\nprint end caused by StopIteration\n')
        break



'''

##es7
'''

def decode(stringa_da_decode):
    stringa_in_morse=''
    stringa_in_alph=''
    if stringa_da_decode[0] in ('.','-'):
        stringa_in_morse=stringa_da_decode.split()
        decoder=dict((x[1],x[0]) for x in alph_morse)
        undecoded=list()
        for el in stringa_in_morse:
            if el in decoder:
                stringa_in_alph+=decoder[el] 
                continue
            if el == '/':
                stringa_in_alph+=' '
                continue
            undecoded.append(el)
            stringa_in_alph+='? '

        print(stringa_in_alph)
        if len(undecoded)>0: print('i seguenti morse non sono stati decodificati: ', *undecoded)
    else:
        stringa_in_alph=stringa_da_decode
        decoder=dict((x[0],x[1]) for x in alph_morse)
        undecoded=list()
        for el in stringa_in_alph.replace(' ','/').replace('\n','/').replace('.','').replace(',',''):
            if el in decoder:
                stringa_in_morse+=decoder[el]+' ' 
                continue
            if el == '/':
                stringa_in_morse+='/ '
                continue
            undecoded.append(el)
            stringa_in_morse+='? '

        print(stringa_in_morse.replace('/ /','/\n'))
        if len(undecoded)>0: print('i seguenti caratteri non sono stati decodificati: ', *undecoded)

################# MAIN ####################
print('-'*10+'ES. 7'+'-'*10)
alph='abcdefghijklmnopqrstuvwxyz0123456789'
alph_morse=list()

with open('morse',encoding='utf-8') as M:
    for a,b in zip(alph,M.readlines()):
        alph_morse.append((a,b[4:-1]))
#print(alph_morse)
morse=list(x[1]for x in alph_morse)

stringa_da_decode=input('Scrivi quel che vuoi come vuoi o un fli .txt\n\n')
#stringa_da_decode='viva vittorio emanuele re di italia'; print('stringa std:', stringa_da_decode, '\n')
if '.txt' in stringa_da_decode:
    file=open(stringa_da_decode)
    decode(file.read())
else: decode(stringa_da_decode)

################# FINE MAIN ####################
'''
##es8
import random
def griglia_vuota(gg):
    ans=True
    for l in gg:
        if any(l):
            ans=False
            break
    return ans

print('-'*10+'ES. 8'+'-'*10)

griglia=list()
rrange=5
navi=0
mosse=list()

'''class casella:
    def __init__(self, c_x:int, c_y:int, value:int, rrange=rrange):
        self.nave=None
        if c_x not in range(rrange) or c_y not in range(rrange) or c_x not in (0,1,2):
            self.c_x=-1
            self.c_y=-1
            self.value=-1
            print('casella non valida')
            return

        self.c_x=c_x
        self.c_y=c_y
        self.value=value

    def validate(self,nave):
        self.value=1
        self.nave=nave


    def colpito(self):
        self.value=2

    def is_empty(self):
        if self.value==0:return True
        else: return False

class griglia:
    def __init__(self, rrange=rrange):
        self.Griglia=dict()
        alph='abcdefghijklmnopqrstuvwxyz'
        for i in alph[:rrange]:
            for j in range(rrange):
                self.Griglia[f'{i}{j}']=casella(alph.index(i),j,0)
        pass

    def add_boat(self,nave):
        
        pass

class nave:
    def __init__(self, len:int, dir:str,cas_inizio:str, griglia:griglia):
        self.len=len
        if dir.lower()=='n':
            n=int(cas_inizio[1])
            self.dmg={cas_inizio[0]+str(n-k):1 for k in range(len)}
        elif dir.lower()=='s':
            n=int(cas_inizio[1])
            self.dmg={cas_inizio[0]+str(n+k):1 for k in range(len)}
        pass'''

for i in range(rrange):
    griglia.append(list())
    for j in range(rrange):
        griglia[i].append(random.choice([0,0,0,0,0,0,1]))
        if griglia[i][j]==1:navi+=1
for i in range(rrange):print(griglia[i])

print(f'La griglia è {rrange}x{rrange}. Le navi sono {navi}, hai {navi+1} possibilità di sbagliare.')

NAVI=navi+1
errori=0

while errori<=NAVI:

    if griglia_vuota(griglia):break

    print('dove vuoi colpire adesso?')
    scelta= input().lower()

    if scelta in mosse: 
        print('già avevi colpito in', scelta)
        continue

    mosse.append(scelta)

    if len(scelta)==2 and scelta[0].isalpha() and scelta[1].isnumeric() and ord(scelta[0])<=ord('a')+rrange and int(scelta[1])<=rrange:
        x=ord(scelta[0])-ord('a')
        y=int(scelta[1])-1

        if griglia[x][y]==1:
            griglia[x][y]=0
            print('colpito e affondato')
            continue

        errori+=1
        print(f'mancato, puoi sbagliare ancora {NAVI-errori} volte' 

        if NAVI-errori>0 else f'mancato,non puoi più sbagliare' 

        if NAVI-errori==0 else f'mancato,non puoi più provare'  )

        continue
        
    print('scelta non valida')
    mosse.pop(-1)

if griglia_vuota(griglia): print('HAI VINTO')
else: print('HAI PERSO')
