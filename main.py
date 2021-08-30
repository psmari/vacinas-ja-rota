from busca import busca
from copy import deepcopy

sol = busca()

# PROBLEMA COM DESTINO ÚNICO
origem = "ALENCAR"
destino = "SILVA"
caminho = sol.amplitudeUnitario(origem, destino)
print("\n> Amplitude com destino único: ", caminho)

# PROBLEMA COM MAIS DE UM DESTINO
origem  = "ALENCAR"
destino = ["WAGNER","YORK","SILVA"]
destino1 = deepcopy(destino)

caminho = sol.amplitudeMulti(origem, destino1)
print("\n> Amplitude com destino único múltiplo: ", caminho)