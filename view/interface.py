from tkinter import *
from PIL import ImageTk, Image
from view.grafo import *


def buildGUI():
    root = Tk()
    root.title("VacinasJá")

    # FRAMES
    inputFrame = Frame(
        root,
        padx=10,
        pady=10,
    )
    grafoFrame = LabelFrame(
        root,
        text=" Grafo ",
        padx=10,
        pady=10,
    )

    Label(inputFrame, text="input").pack()

    # GRAFO
    img = ImageTk.PhotoImage(Image.open("./view/sprites/circle-blue.png"))
    for posto in grafo:
        Label(grafoFrame, image=img).grid(column=posto[1], row=posto[0])
        Label(
            grafoFrame,
            text=posto[2],
            font=("Ubuntu", 13),
        ).grid(column=posto[1], row=posto[0])

    inputFrame.pack(padx=10, pady=10)
    grafoFrame.pack(padx=10, pady=10)
    root.mainloop()
