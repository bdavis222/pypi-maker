import os
import subprocess
import sys
from src.ui.DialogWindow import ActionDialogWindow

FIX_SELECTION_TEXT = "This will fix imports in Python files.\nAre you sure you want to proceed?"
UNFIX_SELECTION_TEXT = "This will reset imports in Python files.\nAre you sure you want to proceed?"
SKIPPED_FILES = ["__pycache__", "__init__.py", "LICENSE", "README.md", "requirements.txt", "setup.py"]

def fix(filepath):
    ActionDialogWindow("Are you sure?", FIX_SELECTION_TEXT, negativeAction=exit, mainWindow=True)
    filesToParentPackagesMap = getFilesToParentPackagesMap(filepath)
    traverseFoldersAndFixPyImports(filepath, filesToParentPackagesMap)

def getFilesToParentPackagesMap(topLevelFilepath):
    filesToParentPackagesMap = {}
    traverseFoldersAndPopulatePathsMap(topLevelFilepath, filesToParentPackagesMap)
    return filesToParentPackagesMap

def traverseFoldersAndPopulatePathsMap(filepath, filesToParentPackagesMap):
    folderName = os.path.basename(filepath)
    contents = os.listdir(filepath)
    
    for item in contents:
        if item.startswith(".") or item in SKIPPED_FILES:
            continue
        
        newPath = filepath + "/" + item
        if os.path.isdir(newPath):
            traverseFoldersAndPopulatePathsMap(newPath, filesToParentPackagesMap)
        
        else:
            filenameAndExtension = item.split(".")
            if len(filenameAndExtension) != 2:
                continue
            
            filename, extension = filenameAndExtension
            if extension == "py":
                filesToParentPackagesMap[filename] = getFormattedPackageName(filepath)

def getFormattedPackageName(filepath):
    topLevelDirectory = os.path.basename(os.path.dirname(__file__))
    fullPackageArray = filepath.split("/")
    startingIndex = 0
    for index, directory in enumerate(fullPackageArray):
        if directory == topLevelDirectory:
            startingIndex = index
            break
    return ".".join(fullPackageArray[startingIndex:])

def traverseFoldersAndFixPyImports(filepath, filesToParentPackagesMap):
    contents = os.listdir(filepath)
    for item in contents:
        if item.startswith(".") or item in SKIPPED_FILES:
            continue
        
        newPath = filepath + "/" + item
        if os.path.isdir(newPath):
            traverseFoldersAndFixPyImports(newPath, filesToParentPackagesMap)
        
        else:
            filenameAndExtension = item.split(".")
            if len(filenameAndExtension) != 2:
                continue
            
            filename, extension = filenameAndExtension
            if extension == "py":
                fixPyImports(filepath, item, filesToParentPackagesMap)

def fixPyImports(filepath, item, filesToParentPackagesMap):
    currentFolder = os.path.basename(filepath)
    filename = filepath + "/" + item
    with open(filename, "r") as file:
        data = file.readlines()
    
    for index, rawLine in enumerate(data):
        line = rawLine.split()
        if not len(line) or line[0] not in ["import", "from"]:
            continue
        
        if line[0] == "import": 
            # import file 
            # OR import file as name
            importedFile = line[1]
            if importedFile not in filesToParentPackagesMap:
                continue
            
            if filesToParentPackagesMap[importedFile] == currentFolder:
                continue
                
            relativePackage = getRelativePackage(currentFolder, importedFile, 
                filesToParentPackagesMap)
            
            if relativePackage == "":
                continue
            
            if len(line) == 2: 
                # import file
                data[index] = f"from {relativePackage} import {importedFile}\n"
        
            elif len(line) == 4: 
                # import file as name
                restOfImportLine = " ".join(line[2:])
                data[index] = f"from {relativePackage} import {importedFile} {restOfImportLine}\n"
        
        elif line[0] == "from":
            if line[1] not in filesToParentPackagesMap: 
                # from file import function
                continue
            
            importedFile = line[1]
            restOfImportLine = " ".join(line[3:])
            relativePackage = getRelativePackage(currentFolder, importedFile, 
                filesToParentPackagesMap)
            
            if relativePackage == "":
                continue
            
            newFilename = relativePackage + "." + importedFile
            data[index] = f"from {newFilename} import {restOfImportLine}\n"
        
    with open(filename, "w") as file:
        file.writelines(data)

def getRelativePackage(currentFolder, importedFile, filesToParentPackagesMap):
    packageArray = filesToParentPackagesMap[importedFile].split(".")
    startingIndex = 0
    for index, directory in enumerate(packageArray):
        if directory == currentFolder:
            startingIndex = index + 1
    return ".".join(packageArray[startingIndex:])

###################################################################################################
########################################   Unfix   ################################################
###################################################################################################

def unfix(filepath):
    ActionDialogWindow("Are you sure?", UNFIX_SELECTION_TEXT, negativeAction=exit, mainWindow=True)
    filesSet = getFilesSet(filepath)
    traverseFoldersAndUnfixPyImports(filepath, filesSet)

def getFilesSet(topLevelFilepath):
    filesSet = set()
    traverseFoldersAndPopulateFilesSet(topLevelFilepath, filesSet)
    return filesSet

def traverseFoldersAndPopulateFilesSet(filepath, filesSet):
    folderName = os.path.basename(filepath)
    contents = os.listdir(filepath)
    
    for item in contents:
        if item.startswith(".") or item in SKIPPED_FILES:
            continue
        
        newPath = filepath + "/" + item
        if os.path.isdir(newPath):
            traverseFoldersAndPopulateFilesSet(newPath, filesSet)
        
        else:
            filenameAndExtension = item.split(".")
            if len(filenameAndExtension) != 2:
                continue
            
            filename, extension = filenameAndExtension
            if extension == "py":
                filesSet.add(filename)

def traverseFoldersAndUnfixPyImports(filepath, filesSet):
    contents = os.listdir(filepath)
    for item in contents:
        if item.startswith(".") or item in SKIPPED_FILES:
            continue
        
        newPath = filepath + "/" + item
        if os.path.isdir(newPath):
            traverseFoldersAndUnfixPyImports(newPath, filesSet)
        
        else:
            filenameAndExtension = item.split(".")
            if len(filenameAndExtension) != 2:
                continue
            
            filename, extension = filenameAndExtension
            if extension == "py":
                unfixPyImports(filepath, item, filesSet)

def unfixPyImports(filepath, item, filesSet):
    currentFolder = os.path.basename(filepath)
    filename = filepath + "/" + item
    with open(filename, "r") as file:
        data = file.readlines()
    
    for index, rawLine in enumerate(data):
        line = rawLine.split()
        if not len(line) or line[0] not in ["import", "from"]:
            continue
        
        if line[0] == "import": 
            # import file OR import folder.file 
            # OR import file as name 
            # OR import folder.file as name
            if line[1] in filesSet:
                continue
            
            importedFile = line[1].split(".")[-1]
            restOfImportLine = "" if len(line) == 2 else line[2:]
            
            data[index] = f"import {importedFile} {' '.join(restOfImportLine)}\n"
        
        elif line[0] == "from": 
            # from file import function 
            # OR from folder.file import function 
            # OR from folder.folder import file 
            # OR from folder.folder import file as name
            if line[1] in filesSet: 
                # from file import function
                continue
            
            importedFile = line[1]
            importedFile = importedFile.split(".")[-1]
            restOfImportLine = "" if len(line) == 2 else line[2:]
            
            if importedFile in filesSet: 
                # from folder.file import function as name
                data[index] = f"from {importedFile} {' '.join(restOfImportLine)}\n"
            
            elif importedFile not in filesSet: 
                # from folder.folder import file as name
                data[index] = f"{' '.join(restOfImportLine)}\n"
    
    with open(filename, "w") as file:
        file.writelines(data)
