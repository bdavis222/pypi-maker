import os
import tkinter as tk
from tkinter import filedialog
import src.ui.navigation as navigation
from src.ui.AuthorInfoSelector import AuthorInfoSelector
from src.ui.DialogWindow import ActionDialogWindow, InfoDialogWindow

MISMATCHED_SELECTION_TEXT = "Mismatched folder name and project name.\nAre you sure you selected correctly?"
NO_PYTHON_FILES_IN_PROJECT_FOLDER_TEXT = "No Python files found in folder.\nSelect a different folder."
PROJECT_DESCRIPTION_TEXT = 'One-sentence Project Description (e.g., "Software designed for..."):'
PROJECT_FOLDER_NOT_CHOSEN_TEXT = "You must select your project \nusing the Browse button."
PROJECT_NAME_NOT_CHOSEN_TEXT = "Project Name is a required field.\nUse folder name as project name?"
SELECT_FOLDER_TEXT = "Select the top-level folder containing your Python project"

class OptionSelector:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("PyPI Maker")
		centerX = (self.window.winfo_screenwidth() - 650) // 2
		centerY = (self.window.winfo_screenheight() - 250) // 2
		self.window.geometry(f"650x250+{centerX}+{centerY}")

		self.filepath = ""
		self.projectName = ""
		self.authorsArray = []
		self.emailsArray = []
		self.correspondingEmail = ""
		self.githubUsername = ""
		self.shortDescription = ""
		self.intendedAudience = ""
		self.intendedAudiences = [
			"N/A",
			"Customer Service",
			"Developers",
			"Education",
			"End Users/Desktop",
			"Financial and Insurance Industry",
			"Healthcare Industry",
			"Information Technology",
			"Legal Industry",
			"Manufacturing",
			"Other Audience",
			"Religion",
			"Science/Research",
			"System Administrators",
			"Telecommunications Industry"
		]
		self.classifiers = False
		
		filepathFrame = tk.Frame(self.window)
		self.labelSelectedPath = tk.Label(self.window, text=SELECT_FOLDER_TEXT, fg="red", 
			bg="white")
		buttonSelectFolder = tk.Button(self.window, text="Browse...", 
			command=self.browseFolders)
		self.showFilepath()
		self.labelSelectedPath.pack(in_=filepathFrame, side=tk.LEFT)
		buttonSelectFolder.pack(in_=filepathFrame, side=tk.LEFT)
		
		navigation = tk.Frame(self.window)
		labelIntendedAudienceSelect = tk.Label(self.window, text="Intended Audience:")
		self.menuIntendedAudienceSelectVar = tk.StringVar(self.window)
		self.menuIntendedAudienceSelectVar.set("Select...")
		menuIntendedAudienceSelect = tk.OptionMenu(self.window, self.menuIntendedAudienceSelectVar,
			*self.intendedAudiences)
		labelIntendedAudienceSelect.pack(in_=navigation, side=tk.LEFT)
		menuIntendedAudienceSelect.pack(in_=navigation, side=tk.LEFT)
		
		frameProjectName = tk.Frame(self.window)
		labelProjectName = tk.Label(self.window, text="Project Name:")
		self.entryProjectName = tk.Entry(self.window, width=25)
		labelProjectName.pack(in_=frameProjectName, side=tk.LEFT)
		self.entryProjectName.pack(in_=frameProjectName, side=tk.LEFT)
		
		frameGithubUsername = tk.Frame(self.window)
		labelGithubUsername = tk.Label(self.window, text="Project GitHub Username:")
		self.entryGithubUsername = tk.Entry(self.window, width=25)
		labelGithubUsername.pack(in_=frameGithubUsername, side=tk.LEFT)
		self.entryGithubUsername.pack(in_=frameGithubUsername, side=tk.LEFT)
		
		labelProjectDescription = tk.Label(self.window, text=PROJECT_DESCRIPTION_TEXT)
		self.entryProjectDescription = tk.Entry(self.window, width=50)
		
		self.includeAuthorNames = tk.BooleanVar(value=True)
		checkboxIncludeAuthorNames = tk.Checkbutton(self.window, text="Include author name(s)?", 
			variable=self.includeAuthorNames, onvalue=True, offvalue=False)
				
		buttonDone = tk.Button(self.window, text="Done", command=self.checkDone, fg="blue")
				
		filepathFrame.pack()
		navigation.pack()
		frameProjectName.pack()
		frameGithubUsername.pack()
		labelProjectDescription.pack()
		self.entryProjectDescription.pack()
		checkboxIncludeAuthorNames.pack()
		buttonDone.pack()
		
		self.window.protocol("WM_DELETE_WINDOW", quit)
		self.window.bind("<Return>", self.checkDoneWithReturnKey)
		
		self.window.mainloop()

	def browseFolders(self):
		chosenFolder = filedialog.askdirectory(initialdir=self.filepath, title=SELECT_FOLDER_TEXT)
		if chosenFolder not in ["", " ", "/"]:
			if not navigation.hasPyFiles(chosenFolder):
				InfoDialogWindow("No Python files found", NO_PYTHON_FILES_IN_PROJECT_FOLDER_TEXT)
				return
			self.filepath = chosenFolder
		else:
			self.filepath = ""
		self.showFilepath()
		self.window.focus_force()
	
	def checkDone(self):
		if self.filepath in ["", " ", "/"]:
			InfoDialogWindow("Missing info", PROJECT_FOLDER_NOT_CHOSEN_TEXT)
			return
		
		self.projectName = self.entryProjectName.get()
		if self.projectName == "":
			ActionDialogWindow("Missing info", PROJECT_NAME_NOT_CHOSEN_TEXT, 
				positiveAction=self.finishWithFolderNameAsProjectName)
			return
		
		chosenFolder = self.filepath.split("/")[-1]
		if chosenFolder != self.projectName:
			ActionDialogWindow("Check your selection", MISMATCHED_SELECTION_TEXT, 
				positiveAction=self.done)
			return
		
		self.done()
	
	def checkDoneWithReturnKey(self, event):        
		self.checkDone()
	
	def closeWindow(self):
		self.window.destroy()
		self.window.quit()
	
	def done(self):
		self.githubUsername = self.entryGithubUsername.get()
		self.shortDescription = self.entryProjectDescription.get()
		self.classifier = self.menuIntendedAudienceSelectVar.get()
		self.classifiers = self.classifier not in ["N/A", "Select..."]
		
		if self.includeAuthorNames.get():
			self.getNamesAndEmails()
		else:
			self.closeWindow()
	
	def finishWithFolderNameAsProjectName(self):
		chosenFolder = self.filepath.split("/")[-1]
		self.projectName = chosenFolder
		self.done()
	
	def getNamesAndEmails(self):
		self.closeWindow()
		authorInfoSelector = AuthorInfoSelector()
		self.authorsArray = authorInfoSelector.names
		self.emailsArray = authorInfoSelector.emails
		self.correspondingEmail = authorInfoSelector.correspondingEmail
	
	def showFilepath(self):
		if self.filepath in ["", " ", "/"]:
			self.labelSelectedPath.configure(text=SELECT_FOLDER_TEXT, fg="red", bg="white")
		else:
			displayedFilepath = self.filepath
			if len(displayedFilepath) > 50:
				displayedFilepath = "..." + displayedFilepath[-50:]
			self.labelSelectedPath.configure(text=displayedFilepath, bg="white", fg="black")
