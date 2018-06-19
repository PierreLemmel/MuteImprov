import tkinter as tk;

class MainWindow(tk.Frame):

	childPaddingX = 4;
	childPaddingY = 5;

	buttonWidth = 17;
	buttonHeight = 2;

	NSEW = (tk.N, tk.S, tk.E, tk.W);

	def __init__(self, parent):
		tk.Frame.__init__(self, parent);
		
		self.__simpleTextSubmittedCallback = None;
		self.__timedTextSubmittedCallback = None;
		self.__theEndSubmittedCallback = None;

		hWeights = [0, 1, 0];
		vWeights = [1, 1, 0];

		row = 0;
		self.__initializeSimpleTextRow(row);
		row += 1;
		self.__initializeTimedTextRow(row);
		row += 1;
		self.__initializeTheEndRow(row);

		self.__SetupGrid(hWeights, vWeights);
		self.__SetControlsPadding(self.childPaddingX, self.childPaddingY);



	def OnSimpleTextSubmitted(self, callback):
		self.__funcCheck(callback);
		self.__simpleTextSubmittedCallback = callback;


	def OnTimedTextSubmitted(self, callback):
		self.__funcCheck(callback);
		self.__timedTextSubmittedCallback = callback;


	def OnTheEndSubmitted(self, callback):
		self.__funcCheck(callback);
		self.__theEndSubmittedCallback = callback;



	def __SetupGrid(self, horizontalWeights, verticalWeights):
		i = 0;
		for hWeight in horizontalWeights:
			self.columnconfigure(i, weight = hWeight);
			i += 1;

		j = 0;
		for vWeight in verticalWeights:
			self.rowconfigure(j, weight = vWeight);
			j += 1;


	def __SetControlsPadding(self, padx, pady):
		for control in self.winfo_children():
			control.grid_configure(padx = padx, pady = pady);


	def __funcCheck(self, func):
		if not callable(func):
			raise ValueError('The input parameter is not a function');


	def __initializeSimpleTextRow(self, row):
		col = 0;

		self.simpleTextLabel = tk.Label(self, anchor = tk.E, text='Saisissez un texte à afficher :');
		self.simpleTextLabel.grid(row = row, column = col);
		col += 1;

		self.simpleTextEntry = tk.Text(self, width = 0);
		self.simpleTextEntry.grid(row = row, column = col, sticky = self.NSEW);
		col += 1;

		self.simpleTextBtn = tk.Button(self, text='Afficher', width = self.buttonWidth, height = self.buttonHeight, command = self.__onSimpleTextClick);
		self.simpleTextBtn.grid(row = row, column = col);


	def __initializeTimedTextRow(self, row):
		col = 0;

		self.timedTextLabel = tk.Label(self, anchor = tk.E, text='Saisissez un texte à faire défiler :');
		self.timedTextLabel.grid(row = row, column = col);
		col += 1;

		self.timedTextEntry = tk.Text(self, width = 0);
		self.timedTextEntry.grid(row = row, column = col, sticky = self.NSEW);
		col += 1;

		self.timedTextBtn = tk.Button(self, text = 'Faire défiler', width = self.buttonWidth, height = self.buttonHeight, command = self.__onTimedTextClick);
		self.timedTextBtn.grid(row = row, column = col);


	def __initializeTheEndRow(self, row):
		self.theEndBtn = tk.Button(self, text='The end!', width = self.buttonWidth, height = self.buttonHeight, command = self.__onTheEndButtonClick);
		self.theEndBtn.grid(row = row, column=1, sticky = self.NSEW)


	def __onSimpleTextClick(self, *args):
		# @TODO: get text value
		text = "OnSimpleTextClick";
		if self.__simpleTextSubmittedCallback is not None:
			self.__simpleTextSubmittedCallback(text);


	def __onTimedTextClick(self, *args):
		# @TODO: get text value
		text = "OnTimedTextClick";
		if self.__timedTextSubmittedCallback is not None:
			self.__timedTextSubmittedCallback(text);


	def __onTheEndButtonClick(self, *args):
		if self.__theEndSubmittedCallback is not None:
			self.__simpleTextSubmittedCallback();
