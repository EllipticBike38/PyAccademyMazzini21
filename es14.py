def consecutive_combo(a: list, b: list):
    c = (a + b).sort()
    return len(c) == max(c) - min(c) + 1




def arithmetic_operation(stringa: str):
    operatori = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y
    }
    stringa = stringa.split()
    try:
        return operatori[stringa[1]](int(stringa[0]), int(stringa[2]))
    except ZeroDivisionError:
        return -1
    except KeyError:
        return ('operatore non valido')
    except ValueError:
        return ('stringa non conforme')


def bisec_sqrt(n):
    def f(x): return x ** 2 - n
    a = 0
    b = n

    def med(): return (a + b) / 2
    medio = med()
    zero = f(med())
    while not -0.1 < zero < 0.1:
        medio = med()
        zero = f(medio)
        if zero < 0:
            a = medio
        else:
            b = medio
    return round(medio, 3)


def will_hit(expression: str, coordinates: tuple):
    exp_list = expression[4:].replace('x', ' * x').split()
    # exp= '2', '*', 'x', '+', '5'

    x_value = int(exp_list[0])*coordinates[0]

    return coordinates[1] == arithmetic_operation(f'{x_value} {exp_list[-2]} {exp_list[-1]}')


def id_mtrx(n):
    if not isinstance(n, int):
        return 'Error'
    if n == 0:
        return []
    return [[0 if i != j else 1 for i in range(abs(n))] for j in range(abs(n))][::n//abs(n)]


def split(stringa: str):
    lista = stringa.replace(')(', ').(').split('.')

    lista2 = []
    for el in lista:
        if el.count(')')-el.count('(') > 0:
            lista2[-1] += el
            while lista2[-1].count(')')-lista2[-1].count('(') > 0:
                lista2[-2] += lista2[-1]
                lista2 = lista2[:-1]
        else:
            lista2.append(el)
    return lista2


print(split("((())())(()(()()))"))


def split(stringa: str):
    lista = [stringa[:i].count(')')-stringa[:i].count('(')
             for i in range(len(stringa))][1:]
    if stringa.count(')')-stringa.count('(')!=0: raise ValueError
    string = list(stringa)
    print(lista)
    for indice in range(len(lista)):
        if lista[indice] == 0:
            string.insert(indice+1+string.count('.'), '.')
    return ''.join(string).split('.')


print(split("((()))(())()()(()())"))

print(id_mtrx(0), sep='\n')

print(will_hit("y = -4x + 6", (1, 2)))


print(bisec_sqrt(5.2))

print(arithmetic_operation("12 // 0"))

print(consecutive_combo([-10,-9,-8], [-7,-1]))
