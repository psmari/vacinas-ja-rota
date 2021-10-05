from tkinter import *
from view.grafo import *
from view.interface import *


def buildGrafo(root, caminho, background):
    global grafoFrame

    grafoFrame = LabelFrame(root, text=" Grafo ")

    Label(grafoFrame, image=background).grid(column=1, row=1, columnspan=16, rowspan=14)

    if caminho != "caminho não encontrado":
        for posto in grafo:
            Label(
                grafoFrame,
                text=f" {posto[2]} ",
                foreground="white",
                background="#1F8A70",
                font=("TkDefaultFont", 9, "bold"),
            ).grid(column=posto[1], row=posto[0])

            for lugar in caminho:
                if posto[2].upper() == lugar:
                    Label(
                        grafoFrame,
                        text=f" {posto[2]} ",
                        foreground="white",
                        background="#BEDB39",
                        font=("TkDefaultFont", 9, "bold"),
                    ).grid(column=posto[1], row=posto[0])
    else:
        Label(
            grafoFrame,
            text="\n   Caminho não encontrado   \n",
            foreground="white",
            background="#FD7400",
            font=("TkDefaultFont", 14, "bold"),
        ).grid(column=8, row=7)

    grafoFrame.grid(column=1, row=0, rowspan=3, padx=4, pady=4)
