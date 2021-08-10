def syllab(stringa:str)-> str:
    '''sillaba le parole persiane'''
    ans=[]
    for c in stringa: 
        if c in 'aAeiou':
            ans.insert(-1,'.')
        ans.append(c)
    ans=''.join(ans[1:])
    return ans

def divs(n:int):
    if n in (0,1):yield n
    else:    
        for i in range(2,n+1):
            #print('i:', i)
            if n%i==0: yield i

def ecg_seq(n:int):
    lista=[]
    actual=1
    lista.append(actual)
    yield actual
    actual=2
    lista.append(actual)
    yield actual
    while actual!=n:
        l=len(lista)
        i=2
        while l==len(lista):
            for div_i in divs(i):
                #print('div_i: ',div_i)
                if i not in lista and div_i in divs(actual) :
                    k=1
                    actual=i
                    lista.append(actual)
                    yield actual
                    break
            i+=1

    pass

def ecg_seq_index(n:int):
    ans=-1
    for i in ecg_seq(n):
        print(i, end=' | ')
        ans+=1
    return ans

def longest_nonrepeating_substring(stringa:str):
    ans=''
    lenght=len(stringa)
    for el in range(lenght):
        i=0
        c=''
        while el+i<lenght and stringa[el+i]not in c: 
            c+=stringa[el+i]
            i+=1
        if len(c)>len(ans): ans=c
    return ans

def poker_hand_ranking(l:str):
    l=l.split()
    l=['11'+x[-1] if 'J'in x else 
    '12'+x[-1] if 'Q'in x else 
    '13'+x[-1] if 'K'in x else
    '14'+x[-1] if 'A'in x else x for x in l]
    seeds=[]
    nums=[]
    for x in l: 
        seeds.append(x[-1])
        nums.append(int(x[:-1]))
    rules=(
        ('Royal Flush', 'min(nums)==10 and max(nums)==14 and len(set(seeds))==1' ),
        ('Straight Flush', '(all((x in (14,2,3,4,5)) for x in nums) or (max(nums)-min(nums))==4)  and len(set(seeds))==1' ),
        ('Three of a Kind', 'len(set(nums))==2 and max(list(map(nums.count,nums)))==4'),
        ('Full House', 'len(set(nums))==2 and max(list(map(nums.count,nums)))==3' ),
        ('Flush', 'len(set(seeds))==1'),
        ('Straight', 'all((x in (14,2,3,4,5)) for x in nums) or (max(nums)-min(nums))==4'),
        ('Three of a Kind', 'len(set(nums))==3 and max(list(map(nums.count,nums)))==3'),
        ('Two Pairs', 'len(set(nums))==3 and max(list(map(nums.count,nums)))==2'),
        ('Pair', 'len(set(nums))==4'),
        ('High Card', 'True')
    )
    i=0
    while not eval(rules[i][1]):i+=1
    return rules[i][0]
    

choises={
    'def':['non nai scelto nulla, premi invio per uscire',''],
    'ecg':['inserisci il numero da trovare:\n', 'ecg_seq_index'],
    'syl':['inserisci la parola:\n', 'syllab'],
    'lon':['inserisci la striga di cui vuoi trovare la più lunga substr senza ripetizioni\n','longest_nonrepeating_substring'],
    'car':['inserisci la tua mano di carte:\n', 'poker_hand_ranking']
    }
choises.setdefault('def',['non nai scelto nulla, premi qualsiasi dati per uscire',''])

if __name__=='__main__':
    key=input('cosa vuoi fare?'
    '\n\tecg -- trovare l\'indice di un n nella sequenza ecg'
    '\n\tsyl -- sillabare parole persiane'
    '\n\tcar -- ricavare la mano vittoriosa'
    '\n\tlon -- trovare la substringa più lunga senza ripetizioni\n\n')
    choises.setdefault(key,choises['def'])
    value=input(choises[key][0])
    if choises[key][1] != '':print(eval(choises[key][1])(value))
