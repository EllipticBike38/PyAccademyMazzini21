linee = [[b.strip('.,?\'!').lower() for b in a.split()] for a in open('prova 1.txt').readlines()]
linea_old = ['']
ans = ''
for linea in linee:
    if linea_old0 == '':
        linea_old0 = linea[0]
        continue
    if linea_old0 < linea[0]:
        ans += linea[linee.index(linea)]+' '
        linea_old0 = linea
        continue
    break
else:
    print(f'Il segreto è ---> {ans}')
    exit()
print('non c\'era niente da decodificare')
