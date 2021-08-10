

def flat(lista: list):
    def check(i):
        return (hasattr(i, '__iter__') and not (isinstance(i, str) and len(i) > 0))
    ans = lista[:]
    while any(check(i) for i in ans):
        lista_di_supporto = []
        for el in ans:
            if check(el):
                lista_di_supporto.extend(el)
                continue
            lista_di_supporto.append(el)
        ans = lista_di_supporto[:]
    return ans


print(flat(
    [
        1,
        2,
        (3, 4),
        5,
        'sei',
        [7, (8, [9, (10, 11, 12), 10])],
        '',
        []
    ]
))
