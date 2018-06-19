print('Launching MuteImprov');

import os;

from tkinter import *;
from pathlib import Path;
from gui import MainWindow;
from automating import Controller;



print('Starting selenium controller');

controller = Controller();
controller.OpenBrowser();

print('selenium controller started');



title = "Space Gones - Histoires muettes";
dimension = "1000x600";

tk = Tk();
tk.title(title);
tk.geometry(dimension);

window = MainWindow(tk);
window.pack(side = TOP, fill = BOTH, expand = True);


window.OnSimpleTextSubmitted(lambda text: controller.SetSimpleText(text));
window.OnTimedTextSubmitted(lambda text: controller.SetTimedText(text));
window.OnTheEndSubmitted(lambda: controller.StartTheEnd());



tk.mainloop();



print('Exiting program');