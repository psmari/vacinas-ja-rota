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
caminhoAmplitudeUnitario = []
caminhoProfundidadeUnitario = []
caminhoAmplitudeMulti = []
caminhoProfundidadeMulti = []

if len(destino) == 1:
    caminhoAmplitudeUnitario = sol.amplitudeUnitario(origem, destino[0])
    print("\n> Amplitude com destino único: ", caminhoAmplitudeUnitario)

    caminhoProfundidadeUnitario = sol.profundidadeUnitario(origem, destino[0])
    print("\n> Profundidade com destino único: ", caminhoProfundidadeUnitario)

else:
    caminhoAmplitudeMulti = sol.amplitudeMulti(origem, destino1)
    print("\n> Amplitude com destino múltiplo: ", caminhoAmplitudeMulti)

    caminhoProfundidadeMulti = sol.profundidadeMulti(origem, destino1)
    print("\n> Profundidade com destino múltiplo: ", caminhoProfundidadeMulti)


# PROFUNDIDADE LIMITADA
origem = "ALENCAR"
destino = "SILVA"

caminhoProfundidadeLimitada = sol.profundidade_limitada(origem, destino, 2)
print("\nProfundidade Limitada (2)..: ", caminhoProfundidadeLimitada)

caminhoProfundidadeLimitada = sol.profundidade_limitada(origem, destino, 3)
print("\nProfundidade Limitada (3)..: ", caminhoProfundidadeLimitada)

caminhoProfundidadeLimitada = sol.profundidade_limitada(origem, destino, 5)
print("\nProfundidade Limitada (5)..: ", caminhoProfundidadeLimitada)


# APROFUNDAMENTO ITERATIVO
caminhoAprofundamentoIterativo = sol.aprofundamento_iterativo(origem, destino)
print("\nAprof. Iterativo...:", caminhoAprofundamentoIterativo)


# INTERFACE
buildGUI(
    caminhoAmplitudeUnitario,
    caminhoProfundidadeUnitario,
    caminhoAmplitudeMulti,
    caminhoProfundidadeMulti,
    caminhoProfundidadeLimitada,
    caminhoAprofundamentoIterativo,
)
