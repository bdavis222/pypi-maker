import os
import tkinter as tk
from tkinter import filedialog

SELECT_FOLDER_TEXT = "Select the top-level folder containing your Python project"

def getDirectory():
	filepath = ""
	tk.Tk().withdraw()
	chosenFolder = filedialog.askdirectory(initialdir=filepath, title=SELECT_FOLDER_TEXT)
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
