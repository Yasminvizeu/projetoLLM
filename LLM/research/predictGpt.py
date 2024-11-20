from encodeDecode import textoCriptografado


print(len(textoCriptografado))
print(textoCriptografado)
for i in range(len(textoCriptografado)-1):
    x= textoCriptografado[:i]
    y= textoCriptografado[i+1]
    if x != []:
        print(f'quando os dados forem : {x} o alvo é {y}')
