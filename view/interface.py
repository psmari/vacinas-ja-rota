from tkinter import *
from PIL import ImageTk, Image
from dados import nos
from view.constants import *
from view.buildGrafo import buildGrafo
from view.gerarRota import gerarRota


def buildGUI():
    root = Tk()
    root.title("VacinasJá")
    root.config(background=CLR_BACKGROUND)

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
    for botao in range(7):
        Button(
            opcoesFrame,
            width=22,
            text=BTN_NAMES[botao],
            font=("TkDefaultFont", 9, "bold"),
            activeforeground=CLR_DEFAULT,
            command=lambda botao=botao, origem=origem, destino=destino: buildGrafo(
                root,
                gerarRota(
                    botao,
                    origem.get(),
                    destino.get(),
                ),
            ),
        ).grid(column=0, row=botao, padx=4, pady=4)

    # GRAFO
    background = ImageTk.PhotoImage(Image.open("./view/sprites/map.png"))
    Label(root, image=background).grid(column=1, row=0, columnspan=16, rowspan=16)
    buildGrafo(root, []),

    # BUILD INTERFACE
    origemFrame.pack(padx=8, pady=8)
    destinoFrame.pack(padx=8, pady=8)
    opcoesFrame.pack(padx=8, pady=8)
    menuFrame.grid(column=0, row=0, rowspan=14, pady=(0, 80))

    root.mainloop()
