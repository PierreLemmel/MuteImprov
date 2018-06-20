import os;
from sys import platform;
from selenium import webdriver;
from selenium.webdriver.common.by import By;

class Controller:

	def __init__(self):
		pathToDriver = self.__getPathToDriver();

		print(pathToDriver);
		self.driver = webdriver.Chrome(pathToDriver);
		self.urlForIndex = self.__getUrlForIndex();
		self.urlForTheEnd = self.__getUrlForTheEnd();


	def OpenBrowser(self):
		self.driver.get(self.urlForIndex);


	def SetSimpleText(self, text):
		self.__navigateToIndexIfNeeded();

		escapedText = self.__escapeText(text);
		script = 'MuteImprov.setTextImmediate("{0}");'.format(escapedText);
		
		self.__execScript(script);


	def SetTimedText(self, text, minDelay = 100, maxDelay = 150):
		self.__navigateToIndexIfNeeded();

		escapedText = self.__escapeText(text);
		script = 'MuteImprov.setTextTimed("{0}", {1}, {2})'.format(escapedText, minDelay, maxDelay);

		self.__execScript(script);


	def StartTheEnd(self):
		self.__navigateToTheEndIfNeeded();


	def __escapeText(self, text):
		escapedText = text.replace('"', '\\"');
		escapedText = escapedText.replace('\n', '\\n');
		return escapedText;


	def __execScript(self, script):
		print('Executing script: {0}'.format(script));
		self.driver.execute_script(script);


	def __navigateToIndexIfNeeded(self):
		self.__checkForUrl(self.urlForIndex);


	def __navigateToTheEndIfNeeded(self):
		self.__checkForUrl(self.urlForTheEnd);


	def __checkForUrl(self, url):
		currentFileName = self.driver.current_url.split('/')[-1];
		requiredFileName = url.split('\\')[-1];
		if (currentFileName != requiredFileName):
			self.driver.get(url);


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