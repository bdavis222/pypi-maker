import os
import tkinter as tk
from tkinter import filedialog
from pypimaker import strings

def getDirectory():
	filepath = ""
	tk.Tk().withdraw()
	chosenFolder = filedialog.askdirectory(initialdir=filepath, title=strings.SELECT_FOLDER_TEXT)
	if chosenFolder not in ["", " ", "/"] and hasPyFiles(chosenFolder):
		filepath = chosenFolder
		return filepath
	else:
		quit()

def hasPyFiles(filepath):
	for _, _, files in os.walk(filepath):
		for file in files:
			if file.endswith(".py"):
				 return True
	return False

def hasMainFunctionInSrc(filepath):
	for item in os.listdir(filepath):
		newPath = filepath + "/" + item
		if os.path.isdir(newPath) and os.path.basename(newPath) == "src":
			srcContents = os.listdir(newPath)
			for filename in srcContents:
				if filename == "__main__.py":
					finalPath = newPath + "/" + filename
					return mainFileHasMainFunction(finalPath)
	return False

def mainFileHasMainFunction(filepath):
	with open(filepath, "r") as file:
		for line in file:
			if line.startswith("def main("):
				return True
	return False
