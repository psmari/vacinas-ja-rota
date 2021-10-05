from tkinter import *
from PIL import ImageTk, Image
from busca import busca
from dados import nos
from view.grafo import *
from view.buildGrafo import *

sol = busca()


def btnFunc(btn, origem, destino):
    if btn == "Amplitude Unitario":
        return sol.amplitudeUnitario(origem, destino)
    elif btn == "Profundidade Unitario":
        return sol.profundidadeUnitario(origem, destino)
    elif btn == "Amplitude Multipla":
        return sol.amplitudeMulti(origem, [destino])
    elif btn == "Profundidae Multipla":
        return sol.profundidadeMulti(origem, [destino])
    elif btn == "Profundidade Limitada":
        return sol.profundidade_limitada(origem, destino, 5)
    elif btn == "Aprofundamento Iterativo":
        return sol.aprofundamento_iterativo(origem, destino)
    elif btn == "Bidirecional":
        return sol.bidirecional(origem, destino)


def buildGUI():
    root = Tk()
    root.title("VacinasJá")

    global grafoFrame

    background = ImageTk.PhotoImage(Image.open("./view/sprites/graph.png"))
    origem = StringVar(root)
    origem.set("UCHOA")
    destino = StringVar(root)
    destino.set("DUARTE")

    # FRAMES
    origemFrame = LabelFrame(root, text=" Origem ", padx=4, pady=4)
    destinoFrame = LabelFrame(root, text=" Origem ", padx=4, pady=4)
    opcoesFrame = LabelFrame(root, text=" Algoritimos ", padx=4, pady=4)
    grafoFrame = LabelFrame(root, text=" Grafo ")

    # INPUT
    origemField = OptionMenu(origemFrame, origem, *nos)
    origemField.config(width=16)
    origemField.grid(column=0, row=0)

    destinoField = OptionMenu(destinoFrame, destino, *nos)
    destinoField.config(width=16)
    destinoField.grid(column=0, row=1)

    # OPÇÕES
    botaoNum = 0
    botoes = [
        "Amplitude Unitario",
        "Profundidade Unitario",
        "Amplitude Multipla",
        "Profundidae Multipla",
        "Profundidade Limitada",
        "Aprofundamento Iterativo",
        "Bidirecional",
    ]

    for botao in botoes:
        Button(
            opcoesFrame,
            width=24,
            text=botao,
            command=lambda botao=botao: buildGrafo(
                root, btnFunc(botao, origem.get(), destino.get()), background
            ),
        ).grid(column=0, row=botaoNum)

        botaoNum += 1

    # BUILD INTERFACE
    origemFrame.grid(column=0, row=0, padx=(4, 2), pady=4)
    destinoFrame.grid(column=0, row=1, padx=(4, 2), pady=4)
    opcoesFrame.grid(column=0, row=2, padx=(4, 2), pady=4)
    buildGrafo(root, btnFunc(botoes[0], origem.get(), destino.get()), background)

    root.mainloop()
