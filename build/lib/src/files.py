import datetime
import os 
import subprocess 

DEFAULT_INITIAL_VERSION = "0.1.0"

def generate(filepath, projectName, authorsArray, emailsArray, correspondingEmail, githubUsername,
	shortDescription, classifier):
	generateRequirementsFile(filepath)
	generateGitIgnoreFile(filepath)
	generateLicenseFile(filepath, authorsArray)
	generateReadmeFile(filepath, projectName, shortDescription, authorsArray, emailsArray, 
		githubUsername)
	generateInitFiles(filepath)
	generateSetupFile(filepath, authorsArray, correspondingEmail, githubUsername, projectName, 
		shortDescription, classifier)

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
	
	output = f'\
MIT License\n{copyrightLine}\
\n\
Permission is hereby granted, free of charge, to any person obtaining a copy \
of this software and associated documentation files (the "Software"), to deal \
in the Software without restriction, including without limitation the rights \
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell \
copies of the Software, and to permit persons to whom the Software is \
furnished to do so, subject to the following conditions:\n\
\n\
The above copyright notice and this permission notice shall be included in all \
copies or substantial portions of the Software.\n\
\n\
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, \
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER \
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, \
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE \
SOFTWARE.'
	
	with open(filepath + "/LICENSE", "w") as file:
		file.write(output)

def getAuthorNamesInline(authorsArray):
	if len(authorsArray) == 1:
		return authorsArray[0]
	
	elif len(authorsArray) == 2:
		return f"{authorsArray[0]} and {authorsArray[1]}"
	
	else:
		allButLast = authorsArray[:-1]
		last = authorsArray[-1]
		return ", ".join(allButLast) + ", and " + last

def generateReadmeFile(filepath, projectName, blurb, authorsArray, emailsArray, githubUsername):
	blurbLine = "" if blurb == "" else f"> {blurb}\n"
	if len(authorsArray):
		namesAndEmails = getNamesAndEmailsVerticallySpaced(authorsArray, emailsArray)
		authorSection = f"## Authors\n\n{namesAndEmails}\n\n"
	else:
		authorSection = ""
	
	if githubUsername == "":
		licenseDetails = ""
		bugReports = ""
	else:
		licenseDetails = f"\
See the [LICENSE](https://github.com/{githubUsername}/{projectName}/blob/main/LICENSE) file for details."
		bugReports = f"\n\
### Bug Reports and Feature Requests\n\
\n\
To report a bug, visit the [issues page](https://github.com/{githubUsername}/{projectName}/issues). \
New feature requests are also welcome!"
	
	output = f"\
# {projectName}\n\
{blurbLine}\
\n\
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](PAYPAL_DONATE_LINK_GOES_HERE)\n\
\n\
OPTIONAL: ENTER A 2-3 SENTENCE DESCRIPTION ABOUT THE SOFTWARE HERE\n\
\n\
## Getting Started\n\
\n\
### Dependencies\n\
\n\
[Python 3](https://www.python.org/downloads/) must be installed before {projectName} can be installed.\n\
\n\
### Installation\n\
\n\
To install {projectName}, open a terminal window and run the following command:\n\
\n\
```\n\
pip install {projectName}\n\
```\n\
\n\
*(Note that the* `pip3` *command may be required instead of* `pip` *for some Python installations.)*\n\
\n\
### Running the Software\n\
\n\
To launch the main program, run the following command:\n\
\n\
```\n\
{projectName}\n\
```\n\
\n\
## SOME_OTHER_HEADER\n\
\n\
IMAGES INCLUDED BY LINKING TO THEIR LOCATION IN THE PROJECT, E.G.:\n\
![](https://github.com/bdavis222/dotscanner/blob/main/images/3.png)\n\
\n{authorSection}\
## Release History\n\
\n\
* {DEFAULT_INITIAL_VERSION}\n\
	 * Initial Release\n\
\n\
## License\n\
\n\
This project is licensed under the MIT License. {licenseDetails}\n\
\n\
## Development\n\
\n\
To contribute, download or clone the project. From the top level of the project's folder structure, \
one can use the following command to run a local version of the software (e.g., for UI testing):\n\
\n\
```\n\
python -m src\n\
```\n\
\n\
*(Note that the* `python3` *command may be required instead of* `python` *for some Python installations.)*\n\
\n\
### Testing\n\
\n\
Unit tests for this software were written for use with [Python's built-in unittest \
framework](https://docs.python.org/3/library/unittest.html), and are stored in the `tests` folder. \
To run tests, download the project, navigate to the top level of the project's folder structure and \
run the following command:\n\
\n\
```\n\
python -m unittest\n\
```\n\
{bugReports}"
	
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
	shortDescription, classifier):
	pyModules = getPyModules(filepath)
	
	authorNameLine = getAuthorsNameLine(authorsArray)
	authorEmailLine = getAuthorEmailLine(correspondingEmail)
	descriptionLine = getDescriptionLine(shortDescription)
	githubInfo = getGithubInfo(githubUsername, projectName)
	classifiers = getClassifiers(classifier)
	
	output = f"from setuptools import setup, find_packages\n\
import pathlib\n\
\n\
here = pathlib.Path(__file__).parent.resolve()\n\
\n\
long_description = (here / 'README.md').read_text(encoding='utf-8')\n\
\n\
setup(\n\
	name='{projectName}', # Required\n\
	version='{DEFAULT_INITIAL_VERSION}', # Required {descriptionLine}\n\
	long_description=long_description,\n\
	long_description_content_type='text/markdown',\
{githubInfo[0]}{authorNameLine}{authorEmailLine}{classifiers}\n\
	packages=find_packages(), # Required\n\
	py_modules={pyModules}, # Generated\n\
	python_requires='>=3.7, <4', {githubInfo[1]}\n\
	entry_points={{\n\
		'console_scripts': [\n\
			'{projectName} = src.__main__:main'\n\
		]\n\
	}}\n\
)"
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
		urlLine = f"\n    url='https://github.com/{username}/{projectName}',"
		projectUrlsLine = f"\n\
	project_urls={{\n\
		'Bug Reports': 'https://github.com/{username}/{projectName}/issues',\n\
		# 'Funding': 'PAYPAL_DONATE_LINK_GOES_HERE',\n\
		'Source': 'https://github.com/{username}/',\n\
	}},"
		return [urlLine, projectUrlsLine]

def getClassifiers(classifier):
	if classifier in ["N/A", "Select..."]:
		return ""
	else:
		return f"\n\
	classifiers=[ # Defined at https://pypi.org/classifiers/\n\
		'Intended Audience :: {classifier}',\n\
		'License :: OSI Approved :: MIT License',\n\
		'Programming Language :: Python :: 3',\n\
		'Operating System :: Unix',\n\
		'Operating System :: MacOS :: MacOS X',\n\
		'Operating System :: Microsoft :: Windows'\n\
	],"
