def bubble_sort(l:list):
    for i in range(-1,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l
import random
import timeit
lista=[random.randint(0,30) for _ in range (20)]

def binary_search(l:list,n):
    ll=len(l)
    if (ll%2==1 or ll==1) and l[ll]==n:
        return ll
    
    try:
        if l[ll]<=n: return binary_search(l[:ll],n)
    except:
        print(ll)
    a = binary_search(l[ll:],n)
    if a is None:
        return None
    return a+ll
        

if __name__=='__main__':
    print(lista)
    lista=bubble_sort(lista)
    print(lista)
    n=lista[random.randint(0,19)]
    print(lista)
    indice = binary_search(lista, n)
    print(indice)


    print(timeit.timeit('bubble_sort(lista)',setup= 'from Marulli_es2 import bubble_sort, lista',number=1))