from tkinter import messagebox
from busca import busca

sol = busca()


def gerarRota(btn, origem, destino):
    if origem == destino:
        messagebox.showwarning(
            "Atenção",
            "A origem e o destino não devem ser o mesmo local",
        )
    elif btn == 0:
        return [sol.amplitudeUnitario(origem, destino), 0]
    elif btn == 1:
        return [sol.profundidadeUnitario(origem, destino), 0]
    elif btn == 2:
        return [sol.amplitudeMulti(origem, [destino]), 0]
    elif btn == 3:
        return [sol.profundidadeMulti(origem, [destino]), 0]
    elif btn == 4:
        return [sol.profundidade_limitada(origem, destino, 5), 0]
    elif btn == 5:
        return [sol.aprofundamento_iterativo(origem, destino), 0]
    elif btn == 6:
        return [sol.bidirecional(origem, destino), 0]
    elif btn == 7:
        return sol.custo_uniforme(origem, destino)
    elif btn == 8:
        return sol.greedy(origem, destino)
    elif btn == 9:
        return sol.a_estrela(origem, destino)
