def shift(n):
    alph='abcdefghijklmnopqrstuvwxyz'
    return alph[n:]+alph[:n]

#def decode(stringa:str, keyword:str):
#    stringa=stringa.lower()
#    keyword=keyword.lower()
#    alph='abcdefghijklmnopqrtuvwxyz'
#    ans=''
#    for n, char in enumerate(stringa):
#        keyword_n=n%len(keyword)
#        k_sh=alph.index(keyword[keyword_n])
#        k_c=shift(k_sh).index(keyword[keyword_n])
#        str_sh=alph.index(char)
#        str_c=shift(str_sh).index(char)
#        ans+=shift(k_c)[str_sh]
#    return ans

def code(stringa:str, keyword:str):
    stringa=stringa.lower()
    keyword=keyword.lower()
    alph='abcdefghijklmnopqrstuvwxyz'
    ans=''
    for n, char in enumerate(stringa):
        if char not in alph:
            ans+=char
            continue 
        keyword_n=n%len(keyword)
        k_sh=alph.index(keyword[keyword_n])
        str_sh=alph.index(char)
        ans+=shift(str_sh)[k_sh]
    return ans



def decode(stringa:str, keyword:str):
    stringa=stringa.lower()
    keyword=keyword.lower()
    alph='abcdefghijklmnopqrstuvwxyz'
    ans=''
    for n, char in enumerate(stringa):
        if char not in alph:
            ans+=char
            continue 
        keyword_n=n%len(keyword)
        k_sh=alph.index(keyword[keyword_n])
        ans+=shift(shift(k_sh).index(char))[0]
    return ans
frase=input()
codice=code(frase,'verme')
print(codice)

print(decode(codice,'verme'))