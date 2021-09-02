from busca import busca
from copy import deepcopy

sol = busca()

# AMPLITUDE - PROBLEMA COM DESTINO ÚNICO
origem = "ALENCAR"
destino = "SILVA"
caminho = sol.amplitudeUnitario(origem, destino)
print("\n> Amplitude com destino único: ", caminho)

# AMPLITUDE - PROBLEMA COM MAIS DE UM DESTINO
origem  = "ALENCAR"
destino = ["WAGNER","YORK","SILVA"]
destino1 = deepcopy(destino)

caminho = sol.amplitudeMulti(origem, destino1)
print("\n> Amplitude com destino múltiplo: ", caminho)

# PROFUNDIDADE - PROBLEMA COM DESTINO ÚNICO
origem = "ALENCAR"
destino = "SILVA"

caminho = sol.profundidadeUnitario(origem,destino)
print("\n> Profundidade com destino único: ", caminho)

# PROFUNDIDADE  - PROBLEMA COM MAIS DE UM DESTINO
origem  = "ALENCAR"
destino = ["WAGNER","YORK","SILVA"]
destino1 = deepcopy(destino)

caminho = sol.profundidadeMulti(origem,destino1)
print("\n> Profundidade com destino múltiplo: ", caminho)

