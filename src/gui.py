import tkinter as tk;

class MainWindow(tk.Frame):

	NSEW = tk.N + tk.S + tk.E + tk.W;

	def __init__(self, parent):
		tk.Frame.__init__(self, parent);
		
		self.__simpleTextSubmittedCallback = None;
		self.__timedTextSubmittedCallback = None;
		self.__theEndSubmittedCallback = None;

		self.__SetupGrid([1, 3, 1]);

		row = 0;
		self.__initializeSimpleTextRow(row);
		row += 1;
		self.__initializeTimedTextRow(row);
		row += 1;
		self.__initializeTheEndRow(row);



	def OnSimpleTextSubmitted(self, callback):
		self.__funcCheck(callback);
		self.__simpleTextSubmittedCallback = callback;


	def OnTimedTextSubmitted(self, callback):
		self.__funcCheck(callback);
		self.__timedTextSubmittedCallback = callback;


	def OnTheEndSubmitted(self, callback):
		self.__funcCheck(callback);
		self.__theEndSubmittedCallback = callback;


	def __SetupGrid(self, weights):
		col = 0;
		for weight in weights:
			self.columnconfigure(col, weight=weight);
			col += 1;


	def __funcCheck(self, func):
		if not callable(func):
			raise ValueError('The input parameter is not a function');


	def __initializeSimpleTextRow(self, row):
		col = 0;

		self.simpleTextLabel = tk.Label(self, text='Saisir un texte :');
		self.simpleTextLabel.grid(row=row, column=col, sticky=self.NSEW);
		col += 1;

		self.simpleTextEntry = tk.Entry(self);
		self.simpleTextEntry.grid(row=row, column=col, sticky=self.NSEW);
		col += 1;

		self.simpleTextBtn = tk.Button(self, text='Afficher', command=self.__onSimpleTextClick);
		self.simpleTextBtn.grid(row=row, column=col, sticky=self.NSEW);
		col += 1;


	def __initializeTimedTextRow(self, row):
		col = 0;
		pass;


	def __initializeTheEndRow(self, row):
		col = 0;
		pass;


	def __onSimpleTextClick(self):
		# @TODO: get text value
		text = "OnSimpleTextClick";
		if self.__simpleTextSubmittedCallback is not None:
			self.__simpleTextSubmittedCallback(text);


	def __onTimedTextClick(selft):
		# @TODO: get text value
		text = "OnTimedTextClick";
		if self.__timedTextSubmittedCallback is not None:
			self.__timedTextSubmittedCallback(text);


	def __onTheEndButtonClick(self):
		if self.__theEndSubmittedCallback is not None:
			self.__simpleTextSubmittedCallback();
