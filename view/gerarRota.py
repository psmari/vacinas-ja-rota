from tkinter import messagebox
from busca import busca

sol = busca()


def gerarRota(btn, origem, destino):
    if origem == destino:
        messagebox.showwarning(
            "Atenção",
            "A origem e o destino não devem ser o mesmo local",
        )

        return "erro"

    func = {
        0: sol.amplitudeUnitario(origem, destino),
        1: sol.profundidadeUnitario(origem, destino),
        2: sol.amplitudeMulti(origem, [destino]),
        3: sol.profundidadeMulti(origem, [destino]),
        4: sol.profundidade_limitada(origem, destino, 5),
        5: sol.aprofundamento_iterativo(origem, destino),
        6: sol.bidirecional(origem, destino),
    }

    caminho = func.get(btn)

    if caminho == "caminho não encontrado":
        messagebox.showwarning("Atenção", "Não foi possível gerar a rota.")

    return caminho
