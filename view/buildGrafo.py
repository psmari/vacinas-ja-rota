from tkinter import *
from view.constants import GRAFO, CLR_SELECTED, CLR_DEFAULT
from view.interface import *


def buildGrafo(master, caminho):
    for posto in GRAFO:
        Label(
            master,
            text=f" {posto[2]} ",
            font=("TkDefaultFont", 9, "bold"),
            foreground="white",
            background=CLR_SELECTED if posto[2].upper() in caminho else CLR_DEFAULT,
        ).grid(column=posto[1], row=posto[0])
