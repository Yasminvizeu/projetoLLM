from charToVec import caracteres

letraIndex = {lt: i for i, lt in enumerate(caracteres)}
indexLetra = {i: lt for i, lt in enumerate(caracteres)}

encode = lambda s: [letraIndex[c] for c in s]
decode = lambda l: ''.join([indexLetra[i] for i in l])

textoCriptografado = encode("estamos aprendendo tranformers")
textoDescriptografado = decode(encode("vamos aprender"))
print(textoCriptografado)