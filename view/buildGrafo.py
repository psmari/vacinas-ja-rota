from tkinter import *
from view.colors import *
from view.grafo import *
from view.interface import *


def buildGrafo(root, caminho, background):
    grafoFrame = Frame(root, background=CLR_BACKGROUND)

    Label(grafoFrame, image=background).grid(column=1, row=1, columnspan=16, rowspan=14)

    for posto in grafo:
        Label(
            grafoFrame,
            text=f" {posto[2]} ",
            font=("TkDefaultFont", 9, "bold"),
            foreground="white",
            background=CLR_SELECTED if posto[2].upper() in caminho else CLR_DEFAULT,
        ).grid(column=posto[1], row=posto[0])

    if caminho == "caminho não encontrado":
        Label(
            grafoFrame,
            text="\n   Caminho não encontrado   \n",
            foreground=CLR_FONT,
            background=CLR_ALERT,
            font=("TkDefaultFont", 14, "bold"),
        ).grid(column=0, row=0, columnspan=16, rowspan=14)

    grafoFrame.grid(column=1, row=0)
