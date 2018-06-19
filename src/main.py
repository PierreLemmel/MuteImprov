print('Launching MuteImprov');

import os;

from tkinter import *;
from pathlib import Path;
from gui import MainWindow;


title = "Space Gones - Histoires muettes";
dimension = "1000x600";

tk = Tk();
tk.title(title);
tk.geometry(dimension);

window = MainWindow(tk);
window.pack(side=TOP, fill=BOTH, expand=True);

tk.mainloop();


print('Exiting program');