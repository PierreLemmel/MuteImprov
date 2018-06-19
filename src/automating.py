import os;
from sys import platform;
from selenium import webdriver;


class Controller:

	def __init__(self):
		pathToDriver = self.__getPathToDriver();

		print(pathToDriver);
		self.driver = webdriver.Chrome(pathToDriver);
		self.urlForIndex = self.__getUrlForIndex();
		self.urlForTheEnd = self.__getUrlForTheEnd();


	def OpenBrowser(self):
		self.driver.get("http://www.google.com");


	def SetSimpleText(self, text):
		print('SetSimpleText: %s' % text);


	def SetTimedText(self, text):
		print('SetTimedText: %s' % text);


	def StartTheEnd(self):
		print('The End!');


	def __navigateToIndexIfNeeded(self):
		


	def __getUrlForIndex(self):
		basePath = os.getcwd();
		path = os.path.join(basePath, '..\content', 'index.html');
		return path;


	def __getUrlForTheEnd(self):
		basePath = os.getcwd();
		path = os.path.join(basePath, '..\content', 'theend.html');
		return path;


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