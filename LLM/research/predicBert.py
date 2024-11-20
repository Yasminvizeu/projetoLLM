from encodeDecode import textoCriptografado
from random import randint

for i in range(len(textoCriptografado)):
    x= textoCriptografado
    y= textoCriptografado.copy()
    idx_mask = randint(0,len(textoCriptografado)-1)
    y[idx_mask] = '<mask>'
    print(f'quando os dados forem : {x} o alvo é {y}')
