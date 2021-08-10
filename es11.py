# --applicazioni di zip
def what_date_is_the_n_day_of_the_year(n):
    mm = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno',
          'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
    durations = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    coppie = list(zip(durations, mm))

    calendario = list(map(lambda x: x[0]*((x[1]+' ')).split(), coppie))
    calendar = list()
    for x in calendario:
        calendar.extend(x)
    print(calendar[:n-1].count(calendar[n-1])+1, calendar[n-1])


def lista_dei_primi_n_quadrati(n):
    return list(map(lambda x: x*x, range(n+1)))


print(*lista_dei_primi_n_quadrati(10))
what_date_is_the_n_day_of_the_year(365)
