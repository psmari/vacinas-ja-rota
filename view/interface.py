from tkinter import *
from PIL import ImageTk, Image
from view.grafo import *


def buildGrafo(root, rebuild, caminho):
    global grafoFrame
    global background

    if rebuild:
        grafoFrame.destroy()

    grafoFrame = LabelFrame(root, text=" Grafo ")

    Label(grafoFrame, image=background).grid(column=1, row=1, columnspan=16, rowspan=14)

    ordemPosto = 1
    for posto in grafo:
        Label(
            grafoFrame,
            text=f"X\n{posto[2]}",
            foreground="white",
            background="#1BA1E2",
            font=("TkDefaultFont", 10),
        ).grid(column=posto[1], row=posto[0])

        for lugar in caminho:
            if posto[2].upper() == lugar:
                Label(
                    grafoFrame,
                    text=f"{ordemPosto}\n{posto[2]}",
                    foreground="white",
                    background="green",
                    font=("TkDefaultFont", 10),
                ).grid(column=posto[1], row=posto[0])

                ordemPosto += 1

    grafoFrame.grid(column=1, row=0, rowspan=2, padx=4, pady=4)


def buildGUI(
    caminhoAmplitudeUnitario,
    caminhoProfundidadeUnitario,
    caminhoAmplitudeMulti,
    caminhoProfundidadeMulti,
    caminhoProfundidadeLimitada,
    caminhoAprofundamentoIterativo,
):
    root = Tk()
    root.title("VacinasJá")

    global grafoFrame
    global background

    background = ImageTk.PhotoImage(Image.open("./view/sprites/graph.png"))

    # FRAMES
    inputFrame = LabelFrame(root, text=" Lugares ", padx=4, pady=4)
    opcoesFrame = LabelFrame(root, text=" Algoritimos ", padx=4, pady=4)
    grafoFrame = LabelFrame(root, text=" Grafo ")

    # INPUT
    Label(inputFrame, text="input").grid(column=0, row=0)

    # OPÇÕES
    botaoNum = 0
    botoes = [
        ["Amplitude Unitario", caminhoAmplitudeUnitario],
        ["Profundidade Unitario", caminhoProfundidadeUnitario],
        ["Amplitude Multipla", caminhoAmplitudeMulti],
        ["Profundidae Multipla", caminhoProfundidadeMulti],
        ["Profundidade Limitada", caminhoProfundidadeLimitada],
        ["Aprofundamento Iterativo", caminhoAprofundamentoIterativo],
    ]

    for botao in botoes:
        Button(
            opcoesFrame,
            width=24,
            text=botao[0],
            command=lambda: buildGrafo(root, True, botao[1]),
        ).grid(column=0, row=botaoNum)

        botaoNum += 1

    # BUILD INTERFACE
    inputFrame.grid(column=0, row=0, padx=(4, 2), pady=4)
    opcoesFrame.grid(column=0, row=1, padx=(4, 2), pady=4)
    buildGrafo(root, False, caminhoAmplitudeUnitario)

    root.mainloop()
