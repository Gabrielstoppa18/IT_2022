
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import resolvedor
alg= resolvedor.SA()
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1097x689")
window.title("Product Allocation")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 689,
    width = 1097,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    548.0,
    344.0,
    image=image_image_1
)

canvas.create_rectangle(
    5.684341886080802e-14,
    0.0,
    452.00000000000006,
    689.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    972.0,
    583.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=alg.sa,
    relief="flat"
)
button_1.place(
    x=105.00000000000006,
    y=276.0,
    width=242.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=alg.save_xls,
    relief="flat"
)
button_2.place(
    x=105.00000000000006,
    y=407.0,
    width=242.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=alg.arm.openFile,
    relief="flat"
)
button_3.place(
    x=105.00000000000006,
    y=143.0,
    width=242.0,
    height=60.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    946.0,
    145.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
