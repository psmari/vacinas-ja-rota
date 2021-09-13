from busca import busca
from copy import deepcopy
from view.interface import *

sol = busca()

# AMPLITUDE - PROBLEMA COM DESTINO ÚNICO
origem = "ALENCAR"
destino1 = []
# destino = ["SILVA"]
destino = ["WAGNER", "YORK", "SILVA"]
destino1 = deepcopy(destino)

if len(destino) == 1:
    caminho = sol.amplitudeUnitario(origem, destino[0])
    print("\n> Amplitude com destino único: ", caminho)

    caminho = sol.profundidadeUnitario(origem, destino[0])
    print("\n> Profundidade com destino único: ", caminho)

else:
    caminho = sol.amplitudeMulti(origem, destino1)
    print("\n> Amplitude com destino múltiplo: ", caminho)

    caminho = sol.profundidadeMulti(origem, destino1)
    print("\n> Profundidade com destino múltiplo: ", caminho)

# PROFUNDIDADE LIMITADA

origem = "ALENCAR"
destino = "SILVA"

caminho = sol.profundidade_limitada(origem, destino, 2)
print("\nProfundidade Limitada (2)..: ", caminho)

caminho = sol.profundidade_limitada(origem, destino, 3)
print("\nProfundidade Limitada (3)..: ", caminho)

caminho = sol.profundidade_limitada(origem, destino, 5)
print("\nProfundidade Limitada (5)..: ", caminho)

# APROFUNDAMENTO ITERATIVO

caminho = sol.aprofundamento_iterativo(origem, destino)
print("\nAprof. Iterativo...:", caminho)

# INTERFACE
buildGUI()
