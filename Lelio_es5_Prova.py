# ESERCIZIO 1
class Articolo():
    def __init__(self, nome: str, prezzo: int) -> None:
        self.nome = nome
        self.prezzo = prezzo


class Pacco():

    def __init__(self, destinatario: str, id: int, articoli: list = []) -> None:
        self.destinatario = destinatario
        self.id = id
        self.articoli = articoli

    def aggiungi_articoli(self, *args):
        self.articoli.extend([el for el in args if isinstance(el, Articolo)])

    def valore(self):
        return sum([el.prezzo for el in self.articoli])

# ESERCIZIO 2


class Quadrilatero():
    def __init__(self, l1, l2, l3, l4) -> None:
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.__nome = 'Quadrilatero'

    def perimetro(self):
        return self.l1+self.l2+self.l3+self.l4

    def confronto(self, figura):
        p1 = self.perimetro()
        p2 = figura.perimetro()
        if p1 > p2:
            return f'il perimetro del {self} è maggiore del perimetro del {figura}'
        if p1 < p2:
            return f'il perimetro del {self} è minore del perimetro del {figura}'
        return f'il perimetro del {self} è uguale al perimetro del {figura}'

    def __str__(self) -> str:
        return f'{self.__nome} di lati {self.l1} {self.l2} {self.l3} {self.l4}'


class Rettangolo(Quadrilatero):
    def __init__(self, l1, l2) -> None:
        super().__init__(l1, l2, l1, l2)
        self.__nome = 'Rettangolo'

    def area(self):
        return self.l2*self.l1

    def __str__(self) -> str:
        return f'{self.__nome} di lati {self.l1} {self.l2}'


class Rombo(Quadrilatero):
    def __init__(self, l1, d1) -> None:
        super().__init__(l1, l1, l1, l1)
        self.d1 = d1
        self.__nome = 'Rombo'
        self.d2 = self.d2_calc()

    def d2_calc(self):
        d2 = 2*(self.l1**2-(0.5*self.d1)**2)**(1/2)
        if isinstance(d2, complex):
            raise ValueError('too big diagonals')
        return d2

    def area(self):
        return (self.d1*self.d2)/2

    def __str__(self) -> str:
        return f'{self.__nome} di lati {self.l1} e diagonali {self.d1} e {self.d2}'

# ESERCIZIO 3


cities = {
    'chicago': 40,
    'Roma': 30,
    'Benevento': 25,
    'Napoli': -30,
    'Palermo': 200
}


def inserisci_citta(nome, temperatura, cities=cities):
    cities[nome] = temperatura


def elimina_citta(nome, cities=cities):
    if nome in cities:
        cities.pop(nome)


def modifica_temperatura(nome, temperatura, cities=cities):
    inserisci_citta(nome, temperatura)


def cerca_citta(nome, cities=cities):
    return (nome, cities[nome])


def elenca_citta(cities=cities):
    for k, v in cities.items():
        print(k, ':', v, 'C')

# ESERCIZIO 4


def isprime(n: int) -> bool:
    '''restituisce True se n è primo, False altrimenti'''
    return all(n % potenziale_divisore for potenziale_divisore in range(3, int(n**(1/2))+1, 2)) and (n % 2 or n == 2) and n != 1


if __name__ == '__main__':
    quard1 = Quadrilatero(1, 2, 3, 4)
    quard2 = Quadrilatero(1, 2, 3, 4)
    rett = Rettangolo(1, 2)
    romb = Rombo(2, 4)
    print(quard1, 'perimetro: ', quard1.perimetro())
    print(quard1.confronto(quard2))
    print(quard1.confronto(rett))
    print(rett, 'area: ', rett.area())
    print(romb, 'area: ', romb.area())

    cities = {
        'chicago': 40,
        'Roma': 30,
        'Benevento': 25,
        'Napoli': -30,
        'Palermo': 200
    }
    inserisci_citta('Caserta', 12)
    elimina_citta('chicago')
    print(cerca_citta('Roma'))
    elenca_citta()
    for i in range(100000000000000000, 100000000000000010):
        if isprime(i):
            print(i, 'is prime')
        else:
            print(i, 'is not prime')
