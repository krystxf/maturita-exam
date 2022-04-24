#!/usr/bin/python

from tkinter import *
from PIL import ImageTk, Image
import time
import threading

from robot import *
from playground import *
from keyboard_controls import *


def Get_image(filename):
    image = ImageTk.PhotoImage(Image.open(
        filename).resize((40, 40), Image.ANTIALIAS))
    return image


root = Tk()
root.title("Kadel")


Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)

for row in range(0, 4):
    Grid.columnconfigure(root, row, weight=1)

images = {"LEFT": Get_image("images/vlevo.png"), "DOWN": Get_image("images/dolu.png"),
          "UP": Get_image("images/nahoru.png"), "RIGHT": Get_image("images/vpravo.png")}

user_code_executing = False

# bind vim controls
root.bind("<Key>", lambda event: keypress(event, karel))

canvas = Canvas(root, bg="white")
playground = Playground(canvas, 10, 10)
karel = Robot(playground, images)

# input
text_input = Text(root).grid(row=0, column=0, sticky="nsew")

text_input = Text(root)
text_input.grid(row=0, column=0, sticky="nsew")

# output
text_output = Label(root, text="some commands").grid(
    row=1, column=0, sticky="nsew")

# controls
button_rotate = Button(root, text="rotate", command=karel.Rotate,
                       padx=40, pady=20).grid(row=2, column=0, sticky="we")
button_step = Button(root, text="step", command=karel.Step,
                     padx=40, pady=20).grid(row=2, column=1, sticky="we")


button_reset = Button(root, text="reset", command=karel.Reset,
                      padx=40, pady=20).grid(row=2, column=2, sticky="we")
button_fill = Button(root, text="fill", command=karel.Fill, padx=40, pady=20).grid(
    row=2, column=3, sticky="we")
button_erase = Button(root, text="erase", command=karel.Erase, padx=40, pady=20).grid(
    row=2, column=4, sticky="we")


def Run_code():
    commands = text_input.get(0.0, END).split("\n")

    def Execute():
        global user_code_executing
        user_code_executing = True
        for command in commands:
            karel.Execute(command)
            time.sleep(1)
        user_code_executing = False

    if not user_code_executing:
        new_thread = threading.Thread(target=Execute)
        new_thread.start()


button_run = Button(root, text="run", command=Run_code, padx=40, pady=20).grid(
    row=2, column=4, sticky="we")

# canvas
canvas.grid(row=0, column=1, rowspan=2,  columnspan=5, sticky="nsew")


root.mainloop()
