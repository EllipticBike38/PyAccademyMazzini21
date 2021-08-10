import datetime


def steganografia():
    char_to_int = {
        'uno': 1,
        'due': 2,
        'tre': 3,
        'quattro': 4,
        'cinque': 5,
        'sei': 6,
        'sette': 7,
        'otto': 8,
        'nove': 9,
        'dieci': 10,
        'undici': 11,
        'dodici': 12,
        'tredici': 13,
        'quattordici': 14,
        'quindici': 15,
        'sedici': 16,
        'diciasette': 17,
        'diciootto': 18,
        'dicianove': 19,
        'venti': 20,
    }

    testo_da_controllare = open('es12.txt',encoding='utf-8')
    cached = 0
    ans = ''
    for line in testo_da_controllare.readlines():
        if len(line) > 0 and line != '\n' and cached < ord(line[0].lower()):
            num = [char_to_int[k]
                   for k in char_to_int for word in line.split() if k in word][0]
            ans += line.split()[num-1]+' '
            cached = ord(line[0].lower())
            continue
        elif not (len(line) > 0 and line != '\n'):
            continue
        ans = 'non è un testo segreto'
        break
    print(ans)


'''def pentagonal_numbers(n):
    ans=1
    if n>1:
        ans=5*(n-1)+pentagonal_numbers(n-1)
    return ans
 '''


def pentagonal_numbers(n): return 5*((n)*(n-1)//2)+1 if n > 0 else 0
#pentagonal_numbers = lambda n: 5*((n)*(n-1)//2)+1 if n > 0 else 0


def has_friday_13(mm, yy): return datetime.date(yy, mm, 1).weekday() == 6
#has_friday_13 = lambda mm,yy: datetime.date(yy, mm, 1).weekday() == 6



def italian_grammar(verb: str):
    if len(verb) < 4 or not verb.endswith('are'):
        return('non è un verbo della prima')

    verb = verb[:-3]
    prefs = ('io', 'tu', 'egli', 'noi', 'voi', 'essi')
    suffs = ('o', 'i', 'a', 'iamo', 'ate', 'ano')
    return'\n'.join((p+' '+verb+s).replace('ii', 'i') if not((verb[-1] in 'cg') and s[0] == 'i') else p+' '+verb+'h'+s for p, s in zip(prefs, suffs))


steganografia()
print()
print(pentagonal_numbers(10))
print()
print(has_friday_13(9, 2019))
print()

print(italian_grammar('giocare')
      )
