from data import *
from page import FrontPage

page_manager.set(FrontPage)

root.mainloop()

# pyinstaller -w --name timeflow --add-data "./images/Boat.gif;." --add-data "./images/Dog.gif;." --add-data "./images/Squidward.gif;." -i "./images/TimeFlow.ico" main.py
