import datetime
import os
import subprocess
from pypimaker import strings
from pypimaker.ui.DialogWindow import DialogWindow

def generate(filepath, projectName, authorsArray, emailsArray, correspondingEmail, githubUsername,
	shortDescription, classifier, mainFunctionPath):
	checkForUnitTests(filepath)
	generateRequirementsFile(filepath)
	generateGitIgnoreFile(filepath)
	generateLicenseFile(filepath, authorsArray)
	generateReadmeFile(filepath, projectName, shortDescription, authorsArray, emailsArray, 
		githubUsername)
	generateInitFiles(filepath)
	generateSetupFile(filepath, authorsArray, correspondingEmail, githubUsername, projectName, 
		shortDescription, classifier, mainFunctionPath)

def checkForUnitTests(filepath):
	if "tests" not in os.listdir(filepath):
		dialogWindow = DialogWindow("No unit tests found", strings.UNIT_TEST_CREATION_PROMPT_TEXT, 
			positiveButtonText="Create", negativeButtonText="Don't", 
			positiveButtonAction=lambda: createUnitTestTemplates(filepath), 
			negativeButtonColor="red")

def createUnitTestTemplates(filepath):
	pythonFileFilepaths = []
	appendPythonFileFilepathsToList(filepath, pythonFileFilepaths)
	newPaths = createNewPaths(filepath, pythonFileFilepaths)
	importStrings = createImportStrings(filepath, pythonFileFilepaths)
	createTestFiles(filepath, newPaths, importStrings)

def appendPythonFileFilepathsToList(filepath, pythonFileFilepaths):
	contents = os.listdir(filepath)
	for item in contents:
		if item.startswith(".") or item.startswith("__") or item == "setup.py":
			continue
		
		extension = item.split(".")[-1]
		if extension == "py":
			pythonFileFilepaths.append(filepath + "/" + item)
		
		itemPath = filepath + "/" + item
		if os.path.isdir(itemPath):
			appendPythonFileFilepathsToList(itemPath, pythonFileFilepaths)

def createImportStrings(filepath, pythonFileFilepaths):
	startingIndex = len(filepath.split("/"))
	importStrings = []
	for path in pythonFileFilepaths:
		pathWithoutExtension = path.split(".")[0]
		importStringPath = ".".join(pathWithoutExtension.split("/")[startingIndex:])
		filename = importStringPath.split(".")[-1]
		importString = f"import {importStringPath} as {filename}"
		importStrings.append(importString)
	return importStrings

def createNewPaths(filepath, pythonFileFilepaths):
	startingIndex = len(filepath.split("/"))
	newPaths = []
	for path in pythonFileFilepaths:
		pathArray = path.split("/")
		pathArray[startingIndex] = "tests"
		newPaths.append("/".join(pathArray))
	return newPaths

def createTestFiles(filepath, newPaths, importStrings):
	startingIndex = len(filepath.split("/"))
	for path, importString in zip(newPaths, importStrings):
		directory = "/".join(path.split("/")[:-1])
		contents = strings.TEST_FILE_CONTENTS.format(
			importString=importString, 
			moduleName=path.split("/")[-1].split(".")[0].capitalize()
		)

		subprocess.call(["mkdir", "-p", directory])
		
		filename = path.split("/")[-1]
		newPathName = "".join([directory, "/", "test_", filename])
		with open(newPathName, "w") as file:
			file.write(contents)

def generateRequirementsFile(filepath):
	checkPipreqsInstallation()
	subprocess.run(["pipreqs", filepath], capture_output=True)

def checkPipreqsInstallation():
	try:
		import pipreqs 
	except:
		commandArray = ["pip", "install", "pipreqs"]
		commandArray2 = ["pip3", "install", "pipreqs"]
		try:
			subprocess.call(commandArray)
		except:
			subprocess.call(commandArray2)
		print()

def generateGitIgnoreFile(filepath):
	output = ".DS_Store\n__pycache__/\n*.py[cod]"
	with open(filepath + "/.gitignore", "w") as file:
		file.write(output)

def generateLicenseFile(filepath, authorsArray):
	currentYear = datetime.datetime.now().year
	if len(authorsArray):
		copyrightLine = f"\nCopyright (c) {currentYear} {getAuthorNamesInline(authorsArray)}\n"
	else:
		copyrightLine = ""
	
	output = strings.LICENSE_FILE_CONTENTS.format(copyrightLine=copyrightLine)
	
	with open(filepath + "/LICENSE", "w") as file:
		file.write(output)

def getAuthorNamesInline(authorsArray):
	if not len(authorsArray):
		return ""
	
	elif len(authorsArray) == 1:
		return authorsArray[0]
	
	elif len(authorsArray) == 2:
		return f"{authorsArray[0]} and {authorsArray[1]}"
	
	else:
		allButLast = authorsArray[:-1]
		last = authorsArray[-1]
		return ", ".join(allButLast) + ", and " + last

def generateReadmeFile(filepath, projectName, blurb, authorsArray, emailsArray, githubUsername):
	if len(authorsArray):
		namesAndEmails = getNamesAndEmailsVerticallySpaced(authorsArray, emailsArray)
		authorSection = strings.AUTHOR_SECTION_CONTENTS.format(namesAndEmails=namesAndEmails)
	else:
		authorSection = ""
	
	if githubUsername == "":
		licenseDetails = ""
		bugReports = ""
	else:
		licenseDetails = strings.LICENSE_DETAILS_CONTENTS.format(
			githubUsername=githubUsername,
			projectName=projectName
		)
		bugReports = strings.BUG_REPORTS_CONTENTS.format(
			githubUsername=githubUsername,
			projectName=projectName
		)
	
	output = strings.README_CONTENTS.format(
		projectName=projectName,
		blurbLine="" if blurb == "" else f"> {blurb}\n",
		authorSection=authorSection,
		version=strings.DEFAULT_INITIAL_VERSION,
		licenseDetails=licenseDetails,
		bugReports=bugReports
	)
	
	with open(filepath + "/README.md", "w") as file:
		file.write(output)

def getNamesAndEmailsVerticallySpaced(authorsArray, emailsArray):
	namesAndEmails = []
	for name, email in zip(authorsArray, emailsArray):
		if email == "":
			namesAndEmails.append(name)
		else:
			namesAndEmails.append(f"{name} ({email})")
	return "\n\n".join(namesAndEmails)

def generateInitFiles(filepath):
	searchForPyFiles(filepath, includeThisDirectory=False)

def searchForPyFiles(filepath, includeThisDirectory=True):
	pyFileFound = False
	contents = os.listdir(filepath)
	for item in contents:
		if item.startswith("."):
			continue
		extension = item.split(".")[-1]
		if includeThisDirectory and extension == "py" and not pyFileFound:
			createInitFileAt(filepath)
			pyFileFound = True
		
		itemPath = filepath + "/" + item
		if os.path.isdir(itemPath):
			searchForPyFiles(itemPath)

def createInitFileAt(filepath):
	with open(filepath + "/__init__.py", "w") as openFile:
		openFile.write("")

def generateSetupFile(filepath, authorsArray, correspondingEmail, githubUsername, projectName, 
	shortDescription, classifier, mainFunctionPath):
	githubInfo = getGithubInfo(githubUsername, projectName)
	
	output = strings.SETUP_FILE_CONTENTS.format(
		projectName=projectName,
		version=strings.DEFAULT_INITIAL_VERSION,
		descriptionLine=getDescriptionLine(shortDescription),
		githubUrlLine=githubInfo[0],
		authorNameLine=getAuthorsNameLine(authorsArray),
		authorEmailLine=getAuthorEmailLine(correspondingEmail),
		classifiers=getClassifiers(classifier),
		pyModules=getPyModules(filepath),
		githubProjectUrlsLine=githubInfo[1],
		mainFunctionPath=mainFunctionPath
	)
	
	with open(filepath + "/setup.py", "w") as file:
		file.write(output)

def getPyModules(filepath):
	pyModules = []
	searchForModules(filepath, filepath, pyModules)
	return pyModules

def searchForModules(absoluteFilepath, filepath, pyModules):
	contents = os.listdir(filepath)
	for item in contents:
		if item.startswith(".") or item.endswith("egg-info") or item in ["build", "dist"]:
			continue
		elif item == "__init__.py":
			pyModules.append(getFormattedPath(absoluteFilepath, filepath))
		
		itemPath = filepath + "/" + item
		if os.path.isdir(itemPath):
			searchForModules(absoluteFilepath, itemPath, pyModules)

def getFormattedPath(absoluteFilepath, filepath):
	topLevelFolderName = absoluteFilepath.split("/")[-1]
	filepathArray = filepath.split("/")
	index = 0
	folderName = filepathArray[index]
	while folderName != topLevelFolderName:
		folderName = filepathArray[index]
		index += 1
	return ".".join(filepathArray[index:])

def getAuthorsNameLine(authorsArray):
	if not len(authorsArray):
		return ""
	else:
		return f"\n    author='{getAuthorNamesInline(authorsArray)}',"

def getAuthorEmailLine(correspondingEmail):
	return f"\n    author_email='{correspondingEmail}'," if correspondingEmail != "" else ""

def getDescriptionLine(description):
	return f"\n    description='{description}'," if description != "" else ""

def getGithubInfo(username, projectName):
	if username == "":
		return ["", ""]
	else:
		urlLine = strings.GITHUB_URL_LINE_CONTENT.format(username=username, projectName=projectName)
		projectUrlsLine = strings.GITHUB_PROJECT_URLS_LINE_CONTENT.format(
			username=username,
			projectName=projectName
		)
		return [urlLine, projectUrlsLine]

def getClassifiers(classifier):
	if classifier in ["N/A", "Select..."]:
		return ""
	else:
		return strings.CLASSIFIERS_CONTENT.format(classifier=classifier)
