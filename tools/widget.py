import time
import tkinter as tk
from PIL import Image
from PIL.ImageTk import PhotoImage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tools.func_tool import loop, gif2iterator


def Img(page, path, width, height, x, y, **kwargs):
    canvas = tk.Canvas(page.frame, width=width, height=height, **kwargs)
    canvas.create_image((0, 0), image=PhotoImage(Image.open(path)), anchor=tk.NW)
    canvas.place(x=x, y=y)


def Gif(page, path, width, height, x, y, **kwargs):
    canvas = tk.Canvas(page.frame, width=width, height=height, **kwargs)
    canvas.place(x=x, y=y)
    iterator = gif2iterator(path)

    @loop(page.root, 0)
    def play():
        img = next(iterator)
        canvas.create_image((0, 0), image=img, anchor=tk.NW)
        page.frame.update_idletasks()
        page.frame.update()
        time.sleep(0.1)


def Fig(page, fig, x, y):
    canvas = FigureCanvasTkAgg(fig, master=page.frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=x, y=y)


class Label:
    def __init__(self, page, text, width, height, x, y, **kwargs):
        self.text = tk.StringVar()
        self.text.set(text)
        label = tk.Label(page.frame, textvariable=self.text, width=width, height=height, **kwargs)
        label.place(x=x, y=y)

    def refresh(self, text):
        self.text.set(str(text))


def Button(page, width, height, x, y, **kwargs):
    button = tk.Button(page.frame, width=width, height=height, **kwargs)
    button.place(x=x, y=y)


def ScrollableText(page, content, width, height, x, y, x_bar, height_bar, **kwargs):
    text = tk.Text(page.frame, width=width, height=height, **kwargs)
    bar = tk.Scrollbar(page.frame, command=text.yview)
    text.config(yscrollcommand=bar.set)
    text.insert(tk.END, content)
    text.place(x=x, y=y)
    bar.place(x=x_bar, y=y, height=height_bar)


def PopupWindow(page, width, height):
    popup = tk.Toplevel(page.frame)
    popup.title("Popup")
    popup.geometry(f"{width}x{height}")
    return popup
