from tkinter import *
from PIL import ImageTk, Image
from busca import busca
from dados import nos
from view.colors import *
from view.grafo import *
from view.buildGrafo import buildGrafo

sol = busca()


btnNames = [
    "Amplitude Unitario",
    "Profundidade Unitario",
    "Amplitude Multipla",
    "Profundidade Multipla",
    "Profundidade Limitada",
    "Aprofundamento Iterativo",
    "Bidirecional",
]


def botoes(btn, origem, destino):
    switcher = {
        0: sol.amplitudeUnitario(origem, destino),
        1: sol.profundidadeUnitario(origem, destino),
        2: sol.amplitudeMulti(origem, [destino]),
        3: sol.profundidadeMulti(origem, [destino]),
        4: sol.profundidade_limitada(origem, destino, 5),
        5: sol.aprofundamento_iterativo(origem, destino),
        6: sol.bidirecional(origem, destino),
    }

    return switcher.get(btn, "nothing")


def buildGUI():
    root = Tk()
    root.title("VacinasJá")
    root.config(background=CLR_BACKGROUND)

    background = ImageTk.PhotoImage(Image.open("./view/sprites/map.png"))
    origem = StringVar(root)
    origem.set("UCHOA")
    destino = StringVar(root)
    destino.set("DUARTE")

    # FRAMES
    menuFrame = Frame(
        root,
        background=CLR_BACKGROUND,
    )
    origemFrame = LabelFrame(
        menuFrame,
        padx=4,
        pady=4,
        text=" Origem ",
        font=("TkDefaultFont", 12, "bold"),
        foreground=CLR_FONT,
        background=CLR_BACKGROUND,
    )
    destinoFrame = LabelFrame(
        menuFrame,
        padx=4,
        pady=4,
        text=" Destino ",
        font=("TkDefaultFont", 12, "bold"),
        foreground=CLR_FONT,
        background=CLR_BACKGROUND,
    )
    opcoesFrame = LabelFrame(
        menuFrame,
        padx=4,
        pady=4,
        text=" Algoritimos ",
        font=("TkDefaultFont", 12, "bold"),
        foreground=CLR_FONT,
        background=CLR_BACKGROUND,
    )
    grafoFrame = Frame(
        root,
        background=CLR_BACKGROUND,
    )

    # INPUT
    origemField = OptionMenu(origemFrame, origem, *nos)
    origemField.config(
        width=20,
        font=("TkDefaultFont", 9, "bold"),
        activeforeground=CLR_DEFAULT,
    )
    origemField.grid(column=0, row=0, padx=4, pady=4)

    destinoField = OptionMenu(destinoFrame, destino, *nos)
    destinoField.config(
        width=20,
        font=("TkDefaultFont", 9, "bold"),
        activeforeground=CLR_DEFAULT,
    )
    destinoField.grid(column=0, row=1, padx=4, pady=4)

    # BOTOES
    for botao in range(6):
        Button(
            opcoesFrame,
            width=22,
            text=btnNames[botao],
            font=("TkDefaultFont", 9, "bold"),
            activeforeground=CLR_DEFAULT,
            command=lambda botao=botao, origem=origem, destino=destino: buildGrafo(
                root, botoes(botao, origem.get(), destino.get()), background
            ),
        ).grid(column=0, row=botao, padx=4, pady=4)

    # DESENVOLVEDORES
    nomes = Label(
        menuFrame,
        text="Joel dos Anjos\n"
        + "\nMarco Antônio\n"
        + "\nMariana Pereira\n"
        + "\nPedro Luis",
        font=("TkDefaultFont", 9, "bold"),
        anchor="w",
        justify=LEFT,
        foreground=CLR_FONT,
        background=CLR_BACKGROUND,
    )

    # GRAFO
    Label(grafoFrame, image=background).grid(column=1, row=1, columnspan=16, rowspan=14)
    buildGrafo(root, [], background),

    # BUILD INTERFACE
    origemFrame.pack(padx=8, pady=8)
    destinoFrame.pack(padx=8, pady=8)
    opcoesFrame.pack(padx=8, pady=8)
    nomes.pack(padx=12, pady=8, fill=BOTH)
    menuFrame.grid(column=0, row=0)
    grafoFrame.grid(column=1, row=0)

    root.mainloop()
