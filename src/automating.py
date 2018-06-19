import os;
from sys import platform;
from selenium import webdriver;


class Controller:

	def __init__(self):
		pathToDriver = self.__getPathToDriver();

		print(pathToDriver);
		self.driver = webdriver.Chrome(pathToDriver);


	def OpenBrowser(self):
		self.driver.get("http://www.google.com");


	def __getPathToDriver(self):
		osFolder = None;
		driver = None;
		if platform == "linux" or platform == "linux2":
			osFolder = "linux";
			driver = "chromedriver";
		elif platform == "win32":
			osFolder = "windows";
			driver = "chromedriver.exe";

		if osFolder is None:
			raise ValueError('Unexpected platform: %s' % platform);

		basePath = os.getcwd();
		path = os.path.join(basePath, '..\drivers', osFolder, driver);

		return path;


	def SetSimpleText(self, text):
		print('SetSimpleText: %s' % text);


	def SetTimedText(self, text):
		print('SetTimedText: %s' % text);


	def StartTheEnd(self):
		print('The End!');