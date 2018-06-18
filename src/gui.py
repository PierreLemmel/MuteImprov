import tkinter as tk;

class MainWindow(tk.Frame):

	def __init__(self, parent):
		tk.Frame.__init__(self, parent);
		
		row = 0;
		self.__initializeSimpleTextRow(row);
		row += 1;


	def __initializeSimpleTextRow(self, row):
		col = 0;

		self.simpleTextLabel = tk.Label(self, text='Saisir un texte :');
		self.simpleTextLabel.grid(row=row, column=col);
		col += 1;

		self.simpleTextEntry = tk.Entry(self);
		self.simpleTextEntry.grid(row=row, column=col);
		col += 1;

		self.simpleTextBtn = tk.Button(self, text='Afficher', command=self.__onSimpleTextClick);
		self.simpleTextBtn.grid(row=row, column=col);
		col += 1;


	def __onSimpleTextClick(self):
		print('onSimpleTextClick');
