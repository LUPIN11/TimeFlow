import tkinter as tk
from tools.data_struct import *

clock = Clock()

ROOT_WIDTH = 600
ROOT_HEIGHT = 600

root = tk.Tk()
root.title("Time Flow")
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")

page_manager = PageManager()
