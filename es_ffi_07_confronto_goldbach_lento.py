import time


def isprime(n: int) -> bool:
    '''restituisce True se n è primo, False altrimenti'''

    return all(n % potenziale_divisore for potenziale_divisore in range(3, int(n**(1/2))+1, 2)) and (n % 2 or n == 2) and n != 1


def gen_primi(limite_sup: int, limite_inf: int = 2):
    """generatore di numeri primi da limite_inf (default 2) a limite_sup"""

    n = limite_inf+(limite_inf % 2)-1

    if limite_inf <= 2:
        yield 2
        n = 3

    while n < limite_sup:
        if isprime(n):
            yield n
        n += 2


def somme_pari_primi_lento(numero: int):
    '''restituisce le coppie di numeri primi la cui somma genera l'argomento pari'''
    ans = []
    if numero % 2 == 1 or numero == 0:
        return ans

    set_primi = set(gen_primi(numero))
    ans = [str(i)+'+'+str(numero-i)
           for i in set_primi if numero-i in set_primi]

    return ans


def somme_pari_primi(numero: int):
    '''restituisce le coppie di numeri primi la cui somma genera l'argomento pari'''
    ans = []
    if numero % 2 == 1 or numero == 0:
        return ans

    ans = [str(i)+'+'+str(numero-i)
           for i in gen_primi(numero//2+1) if isprime(numero-i)]

    return ans


# ho raccolto i dati e l'ho trovata con excel
def linea_di_tendenza_tempo_di_esecuzione(
    x): return 3E-13*x**2 + 1E-06*x - 0.0368


if __name__ == '__main__':

    numero = int(input('dammi un numero\n'))

    start = time.perf_counter()

    print(
        f'ci dovrebbe mettere circa {linea_di_tendenza_tempo_di_esecuzione(numero)} secondi, se non stessi usando quella sanguisuga di webex' if numero > 50000 else
        f'ci dovrebbe mettere davvero molto poco, nonostante quella sanguisuga di webex')

    ans = somme_pari_primi(numero)
    # print(ans)
    end = time.perf_counter()  # finisce il timer

    print(numero, 'eseguito in ', str(end-start).replace('.', ','),
          'secondi.', f'Ha trovato {len(ans)} coppie')
