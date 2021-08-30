# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:52:41 2021

@author: Neto
"""

from busca import busca

sol = busca()

origem = "ALENCAR"
destino = "SILVA"

caminho = sol.amplitude(origem, destino)
print("\n> Amplitude: ", caminho)
