from tkinter import *
from PIL import ImageTk, Image
from view.grafo import *


def buildGrafo(root, rebuild):
    global grafoFrame
    global background

    if rebuild:
        grafoFrame.destroy()

    grafoFrame = LabelFrame(root, text=" Grafo ")

    Label(grafoFrame, image=background).grid(column=1, row=1, columnspan=16, rowspan=14)

    for posto in grafo:
        Label(
            grafoFrame,
            text="\n  " + posto[2] + "  \n",
            foreground="white",
            background="#1BA1E2",
            font=("TkDefaultFont", 8),
        ).grid(column=posto[1], row=posto[0])

    grafoFrame.grid(column=0, row=2, padx=5, pady=5)


def buildGUI():
    root = Tk()
    root.title("VacinasJá")
    root.geometry("942x694")

    global grafoFrame
    global background

    background = ImageTk.PhotoImage(Image.open("./view/sprites/graph.png"))

    # FRAMES
    inputFrame = Frame(root)
    opcoesFrame = Frame(root)
    grafoFrame = LabelFrame(root, text=" Grafo ")

    # INPUT
    Label(inputFrame, text="input").grid(column=0, row=0)

    # OPÇÕES
    Button(
        opcoesFrame,
        text="AMPLITUDE",
        command=lambda: buildGrafo(root, True),
    ).grid(column=0, row=0)
    Button(
        opcoesFrame,
        text="PROFUNDIDADE",
        command=lambda: buildGrafo(root, True),
    ).grid(column=1, row=0)
    Button(
        opcoesFrame,
        text="APROFUNDAMENTO",
        command=lambda: buildGrafo(root, True),
    ).grid(column=2, row=0)

    # BUILD INTERFACE
    inputFrame.grid(column=0, row=0, pady=5)
    opcoesFrame.grid(column=0, row=1)
    buildGrafo(root, False)

    root.mainloop()
