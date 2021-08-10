inp=-1
while inp!=0:
    while 1:
        try:    
            inp=int(input('inserire un un intero:  '))
            break
        except ValueError: print('\npreferirei un intero, grazie')
    if inp==0: 
        print ('uscita in corso...')
        break
    if inp%2==0: print('flip', end=' ')
    if inp%3==0: print('flop', end='')
    print()
print('uscita')