import pandas as pd
import numpy as np

texto = {'texto':['voce esta aprendendo transformer',
                  'talvez voce esteja começando a gostar',
                  ]}

# Conversão
texto = pd.DataFrame(texto)

# Transforma em matriz, separando a string por espaço
dummies = pd.get_dummies(texto['texto'].str.split(' ', expand=True).stack(), prefix='word')

print(dummies)
