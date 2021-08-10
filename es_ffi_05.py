def move_zeros_copy(lista:list):
    l=[k for k in lista if k!=0] 
    l.extend([0 for _ in range(lista.count(0))])
    return l


def move_zeros_inplace(lista:list):
    n=lista.count(0)
    for _ in range (n):
        lista.remove(0)
    lista.extend(0 for _ in range(n))

def move_zeros(lista:list):
    lista.sort(key=bool, reverse=True)

li=[1,0,1,2,0,1,3]
print('\noriginale')
print(li)
print('\nmove_zeros_copy')
print(move_zeros_copy(li))
print('\nmove_zeros_inplace')
move_zeros_inplace(li)
print(li)
print('\n'+'-'*30)

li=[0,0,0,0,0,0,0]
print('\noriginale')
print(li)
print('\nmove_zeros_copy')
print(move_zeros_copy(li))
print('\nmove_zeros_inplace')
move_zeros_inplace(li)
print(li)
print('\n'+'-'*30)


li=[1]
print('\noriginale')
print(li)
print('\nmove_zeros_copy')
print(move_zeros_copy(li))
print('\nmove_zeros_inplace')
move_zeros_inplace(li)
print(li)

print('\n'+'-'*30)

li=[0,0,0,0,0,0,1]
print('\noriginale')
print(li)
print('\nmove_zeros_copy')
print(move_zeros_copy(li))
print('\nmove_zeros_inplace')
move_zeros_inplace(li)
print(li)