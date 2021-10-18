from tkinter import *
from tkinter import messagebox
from view.constants import GRAFO, CLR_SELECTED, CLR_DEFAULT
from view.interface import *


def buildGrafo(master, caminho):
    if type(caminho[0]) is str:
        messagebox.showwarning(
            "Atenção",
            "Não foi possível encontrar o destino.",
        )

    Label(
        master,
        text=f" Peso: {caminho[1]} ",
        font=("TkDefaultFont", 9, "bold"),
        foreground="white",
        background=CLR_SELECTED,
    ).grid(column=15, row=13, columnspan=2)

    for posto in GRAFO:
        Label(
            master,
            text=f" {posto[2]} ",
            font=("TkDefaultFont", 9, "bold"),
            foreground="white",
            background=CLR_SELECTED if posto[2].upper() in caminho[0] else CLR_DEFAULT,
        ).grid(column=posto[1], row=posto[0])
