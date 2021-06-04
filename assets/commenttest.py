import glob
import os
import sys
from pathlib import Path



class ErrorMessage:
	
	def __init__(self, filename, failedLines):
		self.filename  = filename
		self.failedLines = failedLines
	
	def printErrors(self):
		paddingOne = "    Incorrect name line 1 = "
		paddingtwo = "    Incorrect ID line 2 = "
		correctLineOne = "    line 1 should = \"//Greg Quinn\""
		correctLineTwo = "    line 2 should = \"//1125128\""
		print(self.filename)
		file = open(self.filename, "r")
		line1 = file.readline()
		line2 = file.readline()
		if 1 in self.failedLines:
			print(paddingOne+ line1.strip())
			print(correctLineOne)
		if 2 in self.failedLines:
			print(paddingtwo+ line2.strip())
			print(correctLineTwo)

result = list(Path().glob('**/*.tsx'))
incorrectfiles = []

for filename in result:
	if(os.path.isfile(filename)):
		file = open(filename, "r")
		line1 = file.readline()
		line2 = file.readline()
		lineOneFail = line1.strip() != "//Greg Quinn"
		lineTwoFail = line2.strip() != "//1125128"
		if lineOneFail or lineTwoFail:
			
			failedLines = []
			if lineOneFail:
				failedLines.append(1)
			if lineTwoFail:
				failedLines.append(2)
			errorMessage = ErrorMessage(filename, failedLines)
			incorrectfiles.append(errorMessage)
		file.close()

if len(incorrectfiles) == 0:
	print("Number of incorrect files = " + str(len(incorrectfiles)))
	sys.exit(0)
else:
	for errorMessage in incorrectfiles:
		errorMessage.printErrors()
	print("Number of incorrect files = " + str(len(incorrectfiles)))
	sys.exit(1)
