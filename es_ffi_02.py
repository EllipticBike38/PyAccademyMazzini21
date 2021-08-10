def rgb(r, g, b):
    rgb=[r,g,b]
    h='0123456789abcdef'
    for i in range(len(rgb)):
        if rgb[i] < 0 : rgb[i] = '00'
        elif rgb[i] > 255 : rgb[i]='ff'
        else:rgb[i] = h[(rgb[i]//16)] + h[(rgb[i]%16)]
    #your code here :)
    return('#'+''.join(rgb).upper())


esadec = input('dammi l\'esadecimale\n').lower()


def hex_to_dec(esa):
    if len(esa) != 7:
        raise ValueError('lunghezza sbagliata')
    if esa[0] != '#':
        raise ValueError('dov\'è il #? mascalzone')
    rgb= [int(esa[i]+esa[i+1], base=16) for i in (1, 3, 5)]
    return dict(zip('rgb',rgb))

def hex_to_channels(esa, initial_char='%', channel_digit=3, channels='abcd'):
    len_esa=channel_digit*len(channels)+len(initial_char)
    if len(esa) != len_esa:
        raise ValueError('lunghezza sbagliata')
    if esa[0] != initial_char:
        raise ValueError(f'dov\'è il {initial_char}? mascalzone')
    rgb= [int(''.join([esa[i+j] for j in range(channel_digit)]), base=16) for i in range(1,len_esa,channel_digit)]
    return dict(zip(channels,rgb))

print(hex_to_channels(esadec))
