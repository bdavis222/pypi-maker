import os
import subprocess
from src.ui.DialogWindow import ActionDialogWindow

RESET_SELECTION_TEXT = "This will remove generated files.\nAre you sure you want to reset?"

def reset(topLevelDirectory):
    ActionDialogWindow("Are you sure?", RESET_SELECTION_TEXT, negativeAction=exit, mainWindow=True)
    
    filesToRemove = ["LICENSE", "README.md", "requirements.txt", "setup.py", ".gitignore"]
    foldersToRemove = ["build", "dist"]
    for item in os.listdir(topLevelDirectory):
        if item.endswith("egg-info"):
            foldersToRemove.append(item)
    
    for file in filesToRemove:
        commandArray = ["rm", topLevelDirectory + "/" + file]
        subprocess.run(commandArray, capture_output=True)
    
    for folder in foldersToRemove:
        commandArray = ["rm", "-r", topLevelDirectory + "/" + folder]
        subprocess.run(commandArray, capture_output=True)
