import os
import tkinter as tk
from src.ui.DialogWindow import ActionDialogWindow, InfoDialogWindow

MISSING_AUTHOR_NAMES_TEXT = "Some emails have missing author names.\nPlease fix and resubmit."
MISSING_FIRST_NAME_TEXT = "Corresponding author name not given.\nSubmit with no authors?"
MISSING_FIRST_AUTHOR_EMAIL_TEXT = "Email given for other(s), but not first author.\n\
Use next email in list for correspondence?"

class AuthorInfoSelector:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("PyPI Maker")
		centerX = (self.window.winfo_screenwidth() - 650) // 2
		centerY = (self.window.winfo_screenheight() - 310) // 2
		self.window.geometry(f"650x310+{centerX}+{centerY}")
		
		self.names = []
		self.emails = []
		self.correspondingEmail = ""
		
		labelPrimary = tk.Label(self.window, text="Corresponding Author")
		
		authorFrame1 = tk.Frame(self.window)
		labelName1 = tk.Label(self.window, text="Name:")
		self.entryName1 = tk.Entry(self.window, width=25)
		labelEmail1 = tk.Label(self.window, text="Email:")
		self.entryEmail1 = tk.Entry(self.window, width=25)
		labelName1.pack(in_=authorFrame1, side=tk.LEFT)
		self.entryName1.pack(in_=authorFrame1, side=tk.LEFT)
		labelEmail1.pack(in_=authorFrame1, side=tk.LEFT)
		self.entryEmail1.pack(in_=authorFrame1, side=tk.LEFT)
		
		labelOthers = tk.Label(self.window, text="Other Authors")
		
		authorFrame2 = tk.Frame(self.window)
		labelName2 = tk.Label(self.window, text="Name:")
		self.entryName2 = tk.Entry(self.window, width=25)
		labelEmail2 = tk.Label(self.window, text="Email:")
		self.entryEmail2 = tk.Entry(self.window, width=25)
		labelName2.pack(in_=authorFrame2, side=tk.LEFT)
		self.entryName2.pack(in_=authorFrame2, side=tk.LEFT)
		labelEmail2.pack(in_=authorFrame2, side=tk.LEFT)
		self.entryEmail2.pack(in_=authorFrame2, side=tk.LEFT)
		
		authorFrame3 = tk.Frame(self.window)
		labelName3 = tk.Label(self.window, text="Name:")
		self.entryName3 = tk.Entry(self.window, width=25)
		labelEmail3 = tk.Label(self.window, text="Email:")
		self.entryEmail3 = tk.Entry(self.window, width=25)
		labelName3.pack(in_=authorFrame3, side=tk.LEFT)
		self.entryName3.pack(in_=authorFrame3, side=tk.LEFT)
		labelEmail3.pack(in_=authorFrame3, side=tk.LEFT)
		self.entryEmail3.pack(in_=authorFrame3, side=tk.LEFT)
		
		authorFrame4 = tk.Frame(self.window)
		labelName4 = tk.Label(self.window, text="Name:")
		self.entryName4 = tk.Entry(self.window, width=25)
		labelEmail4 = tk.Label(self.window, text="Email:")
		self.entryEmail4 = tk.Entry(self.window, width=25)
		labelName4.pack(in_=authorFrame4, side=tk.LEFT)
		self.entryName4.pack(in_=authorFrame4, side=tk.LEFT)
		labelEmail4.pack(in_=authorFrame4, side=tk.LEFT)
		self.entryEmail4.pack(in_=authorFrame4, side=tk.LEFT)
		
		authorFrame5 = tk.Frame(self.window)
		labelName5 = tk.Label(self.window, text="Name:")
		self.entryName5 = tk.Entry(self.window, width=25)
		labelEmail5 = tk.Label(self.window, text="Email:")
		self.entryEmail5 = tk.Entry(self.window, width=25)
		labelName5.pack(in_=authorFrame5, side=tk.LEFT)
		self.entryName5.pack(in_=authorFrame5, side=tk.LEFT)
		labelEmail5.pack(in_=authorFrame5, side=tk.LEFT)
		self.entryEmail5.pack(in_=authorFrame5, side=tk.LEFT)
		
		authorFrame6 = tk.Frame(self.window)
		labelName6 = tk.Label(self.window, text="Name:")
		self.entryName6 = tk.Entry(self.window, width=25)
		labelEmail6 = tk.Label(self.window, text="Email:")
		self.entryEmail6 = tk.Entry(self.window, width=25)
		labelName6.pack(in_=authorFrame6, side=tk.LEFT)
		self.entryName6.pack(in_=authorFrame6, side=tk.LEFT)
		labelEmail6.pack(in_=authorFrame6, side=tk.LEFT)
		self.entryEmail6.pack(in_=authorFrame6, side=tk.LEFT)
		
		authorFrame7 = tk.Frame(self.window)
		labelName7 = tk.Label(self.window, text="Name:")
		self.entryName7 = tk.Entry(self.window, width=25)
		labelEmail7 = tk.Label(self.window, text="Email:")
		self.entryEmail7 = tk.Entry(self.window, width=25)
		labelName7.pack(in_=authorFrame7, side=tk.LEFT)
		self.entryName7.pack(in_=authorFrame7, side=tk.LEFT)
		labelEmail7.pack(in_=authorFrame7, side=tk.LEFT)
		self.entryEmail7.pack(in_=authorFrame7, side=tk.LEFT)
		
		authorFrame8 = tk.Frame(self.window)
		labelName8 = tk.Label(self.window, text="Name:")
		self.entryName8 = tk.Entry(self.window, width=25)
		labelEmail8 = tk.Label(self.window, text="Email:")
		self.entryEmail8 = tk.Entry(self.window, width=25)
		labelName8.pack(in_=authorFrame8, side=tk.LEFT)
		self.entryName8.pack(in_=authorFrame8, side=tk.LEFT)
		labelEmail8.pack(in_=authorFrame8, side=tk.LEFT)
		self.entryEmail8.pack(in_=authorFrame8, side=tk.LEFT)
		
		self.buttonDone = tk.Button(self.window, text="Done", command=self.checkDone, fg="blue")
		
		labelPrimary.pack()
		authorFrame1.pack()
		labelOthers.pack()
		authorFrame2.pack()
		authorFrame3.pack()
		authorFrame4.pack()
		authorFrame5.pack()
		authorFrame6.pack()
		authorFrame7.pack()
		authorFrame8.pack()
		self.buttonDone.pack()
		
		self.window.protocol("WM_DELETE_WINDOW", quit)
		self.window.bind("<Return>", self.checkDoneWithReturnKey)
		
		self.window.mainloop()
	
	def checkDone(self):
		names = [self.entryName1.get(), self.entryName2.get(), self.entryName3.get(), 
			self.entryName4.get(), self.entryName5.get(), self.entryName6.get(), 
			self.entryName7.get(), self.entryName8.get()]
		emails = [self.entryEmail1.get(), self.entryEmail2.get(), self.entryEmail3.get(), 
			self.entryEmail4.get(), self.entryEmail5.get(), self.entryEmail6.get(), 
			self.entryEmail7.get(), self.entryEmail8.get()]
		
		noEmailsEntered = True
		for name, email in zip(names, emails):
			if email != "":
				noEmailsEntered = False
				if name == "":
					InfoDialogWindow("Invalid entry", MISSING_AUTHOR_NAMES_TEXT)
					return
		
		if names[0] == "":
			ActionDialogWindow("Invalid entry", MISSING_FIRST_NAME_TEXT, 
				positiveAction=self.doneWithNoAuthors)
			return
		
		if emails[0] == "" and not noEmailsEntered:
			ActionDialogWindow("Invalid entry", MISSING_FIRST_AUTHOR_EMAIL_TEXT)
		
		self.done(names, emails)
	
	def checkDoneWithReturnKey(self, event):        
		self.checkDone()
	
	def done(self, names, emails):
		self.names, self.emails = self.getFilteredNamesAndEmails(names, emails)
		self.correspondingEmail = self.getCorrespondingEmail()
		self.window.destroy()
		self.window.quit()
	
	def doneWithNoAuthors(self):
		self.names = []
		self.emails = []
		self.window.destroy()
		self.window.quit()
	
	def getCorrespondingEmail(self):
		for email in self.emails:
			if email != "":
				return email
	
	def getFilteredNamesAndEmails(self, names, emails):
		filteredNames = []
		filteredEmails = []
		for index, name in enumerate(names):
			if name != "":
				filteredNames.append(names[index])
				filteredEmails.append(emails[index])
		return filteredNames, filteredEmails
