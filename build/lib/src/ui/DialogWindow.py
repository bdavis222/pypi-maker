import tkinter as tk

class DialogWindow:
	def __init__(self, title, message, positiveButtonText, negativeButtonText, 
		positiveButtonAction=None, negativeButtonAction=None, windowWidth=300, windowHeight=140, 
		positiveButtonColor="blue", negativeButtonColor="black", 
		mainWindow=False):		
		self.window = tk.Tk()
		self.window.title(title)
		centerX = (self.window.winfo_screenwidth() - windowWidth) // 2
		centerY = (self.window.winfo_screenheight() - windowHeight) // 2
		self.window.geometry(f"{windowWidth}x{windowHeight}+{centerX}+{centerY}")
		
		self.positiveButtonAction = positiveButtonAction
		self.negativeButtonAction = negativeButtonAction
		
		spacer = tk.Label(self.window, text=" ")
		messageText = tk.Label(self.window, text=message)
		spacer2 = tk.Label(self.window, text=" ")
		
		buttonsFrame = tk.Frame(self.window)
		
		if positiveButtonAction is None:
			positiveButton = tk.Button(self.window, text=positiveButtonText,
				fg=positiveButtonColor, command=self.closeWindow)
			self.window.bind("<Return>", self.closeWindowWithReturnKey)
		else:
			positiveButton = tk.Button(self.window, text=positiveButtonText, 
				fg=positiveButtonColor, command=self.performPositiveAction)
			self.window.bind("<Return>", self.performPositiveActionWithReturnKey)
		
		if negativeButtonAction is None:
			negativeButton = tk.Button(self.window, text=negativeButtonText, 
				fg=negativeButtonColor, command=self.closeWindow)
			self.window.bind("<Escape>", self.closeWindowWithEscapeKey)
		else:
			negativeButton = tk.Button(self.window, text=negativeButtonText, 
				fg=negativeButtonColor, command=self.performNegativeAction)
			if negativeButtonAction == exit:
				self.window.bind("<Escape>", self.performNegativeActionWithEscapeKey)
		
		negativeButton.pack(in_=buttonsFrame, side=tk.LEFT)
		positiveButton.pack(in_=buttonsFrame, side=tk.LEFT)
		
		spacer.pack()
		messageText.pack()
		spacer2.pack()
		buttonsFrame.pack()
		
		if mainWindow:
			self.window.protocol("WM_DELETE_WINDOW", quit)
		
		self.window.mainloop()
	
	def closeWindow(self):
		self.window.destroy()
		self.window.quit()
	
	def closeWindowWithEscapeKey(self, event):
		self.closeWindow()
	
	def closeWindowWithReturnKey(self, event):
		self.closeWindow()
	
	def performPositiveAction(self):
		self.closeWindow()
		self.positiveButtonAction()
	
	def performPositiveActionWithReturnKey(self, event):
		self.closeWindow()
		self.positiveButtonAction()
	
	def performNegativeAction(self):
		self.closeWindow()
		self.negativeButtonAction()
	
	def performNegativeActionWithEscapeKey(self, event):
		self.closeWindow()
		self.negativeButtonAction()

class ActionDialogWindow(DialogWindow):
	def __init__(self, title, message, positiveAction=None, negativeAction=None, 
		negativeColor="red", mainWindow=False):
		super().__init__(title, message, positiveButtonText="Confirm", negativeButtonText="Cancel",
			positiveButtonAction=positiveAction, negativeButtonAction=negativeAction,
			negativeButtonColor=negativeColor, mainWindow=mainWindow)

class InfoDialogWindow(DialogWindow):
	def __init__(self, title, message, negativeColor="black"):
		super().__init__(title, message, positiveButtonText="Ok", negativeButtonText="Go back", 
			negativeButtonColor=negativeColor)
