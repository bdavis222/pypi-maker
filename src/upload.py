import os
import subprocess
import time

def upload(filepath):
    checkForRequiredFiles(filepath)

    checkWheelInstallation()
    checkTwineInstallation()
    
    versionNumber = getValidVersionNumberForSetupFile(filepath)
    setNewSetupFileVersion(filepath, versionNumber)

    createDistributionFiles(filepath)
    uploadDistributionFiles(filepath)
    removeDistributionFiles(filepath)

def checkForRequiredFiles(filepath):
    requiredFiles = ["LICENSE", "README.md", "requirements.txt", "setup.py"]
    topLevelDirectoryFiles = set(os.listdir(filepath))
    for file in requiredFiles:
        if file not in topLevelDirectoryFiles:
            print(f"{file} not yet created. Run generatefiles.py first!")
            quit()
    
    if "build" in topLevelDirectoryFiles or "dist" in topLevelDirectoryFiles:
        print("Top-level folders cannot be named 'build' or 'dist'. Please change folder names.")
        quit()

def checkWheelInstallation():
    try:
        import wheel 
    except:
        commandArray = ["pip", "install", "wheel"]
        commandArray2 = ["pip3", "install", "wheel"]
        try:
            subprocess.call(commandArray)
        except:
            subprocess.call(commandArray2)
        print()

def checkTwineInstallation():
    try:
        import twine 
    except:
        commandArray = ["pip", "install", "twine"]
        commandArray2 = ["pip3", "install", "twine"]
        try:
            subprocess.call(commandArray)
        except:
            subprocess.call(commandArray2)
        print()

def getValidVersionNumberForSetupFile(filepath):
    currentSetupFileVersion = getSetupFileVersion(filepath)
    currentPackageVersion = getCurrentPackageVersion(getPackageNameFromSetupFile(filepath))
    if not versionNumberGreater(currentSetupFileVersion, currentPackageVersion):
        currentSetupFileVersion = getNewSetupFileVersion(currentPackageVersion)
    return currentSetupFileVersion

def getSetupFileVersion(filepath):
    with open(filepath + "/setup.py", "r") as file:
        data = file.readlines()
    
    for rawLine in data:
        line = rawLine.split()
        if not len(line):
            continue
        
        if line[0].startswith("version"):
            fullLine = "".join(line)
            currentVersion = fullLine.split("'")[1]
            return currentVersion
    
    return DEFAULT_INITIAL_VERSION

def getCurrentPackageVersion(packageName):
    commandArray = ['pip', 'install', f'{packageName}==nonVersionString']
    result = subprocess.run(commandArray, capture_output=True)
    errorMessage = str(result.stderr)
    if "versions:" not in errorMessage:
        return "0.0.0"
    versions = errorMessage.split("versions:")[-1].split(")")[0].split()
    versions = [version[:-1] if version.endswith(",") else version for version in versions]
    return "0.0.0" if versions == ["none"] else getLargestVersionNumber(versions)

def getPackageNameFromSetupFile(filepath):
    with open(filepath + "/setup.py", "r") as file:
        data = file.readlines()
    
    for rawLine in data:
        line = rawLine.split()
        if not len(line):
            continue
        
        if line[0].startswith("name"):
            fullLine = "".join(line)
            packageName = fullLine.split("'")[1]
            return packageName
    
    raise Exception("No package name found in setup.py")

def versionNumberGreater(largerVersion, smallerVersion):
    largerVersionArray = [int(version) for version in largerVersion.split(".")]
    smallerVersionArray = [int(version) for version in smallerVersion.split(".")]
    largerVersionFirst, largerVersionSecond, largerVersionThird = largerVersionArray
    smallerVersionFirst, smallerVersionSecond, smallerVersionThird = smallerVersionArray
    
    if largerVersionFirst > smallerVersionFirst:
        return True
    elif largerVersionFirst < smallerVersionFirst:
        return False
    
    if largerVersionSecond > smallerVersionSecond:
        return True
    elif largerVersionSecond < smallerVersionSecond:
        return False
    
    return largerVersionThird > smallerVersionThird

def getNewSetupFileVersion(currentPackageVersion):
    newVersion = ""
    while newVersion == "":
        newVersion = input(f"The current version number ({currentPackageVersion}) must be \
incremented. Enter new version number: ")
        
        if not isValidVersionNumber(newVersion):
            newVersion = ""
            continue
        
        if not versionNumberGreater(newVersion, currentPackageVersion):
            newVersion = ""
            continue
        
    print()
    return newVersion

def getLargestVersionNumber(versions):
    maxVersion = "0.0.0"
    for version in versions:
        if versionNumberGreater(version, maxVersion):
            maxVersion = version
    return maxVersion

def isValidVersionNumber(versionNumber):
    numberArray = versionNumber.split(".")
    if len(numberArray) != 3:
        return False
    try:
        int(numberArray[0])
        int(numberArray[1])
        int(numberArray[2])
        return True
    except:
        return False

def setNewSetupFileVersion(filepath, newVersionNumber):
    versionNumberFound = False
    with open(filepath + "/setup.py", "r") as file:
        data = file.readlines()
    
    for index, rawLine in enumerate(data):
        line = rawLine.split()
        if not len(line):
            continue
        
        if line[0].startswith("version"):
            versionIndex = index
            versionNumberFound = True
            break
    
    if not versionNumberFound:
        raise Exception("No version number found in setup.py")
    
    data[versionIndex] = f"    version='{newVersionNumber}', # Required \n"
    
    with open(filepath + "/setup.py", "w") as file:
        file.writelines(data)

def createDistributionFiles(filepath):
    setupFilePath = filepath + "/setup.py"
    
    commandArray = ["python", "setup.py", "sdist", "bdist_wheel"]
    commandArray2 = ["python3", "setup.py", "sdist", "bdist_wheel"]
    try:
        subprocess.call(commandArray, cwd=filepath)
    except:
        subprocess.call(commandArray2, cwd=filepath)

    print()

    count = 0
    while "dist" not in os.listdir(filepath):
        time.sleep(0.1)
        count += 1
        if count > 50:
            raise Exception("'dist' directory not created successfully")

def uploadDistributionFiles(filepath):
    distPath = filepath + "/dist"

    count = 0
    while len(os.listdir(distPath)) < 2:
        time.sleep(0.1)
        count += 1
        if count > 50:
            raise Exception("Files in 'dist' directory not created successfully")

    commandArray = ["twine", "upload", distPath + "/*"]
    subprocess.call(commandArray)

def removeDistributionFiles(filepath):
    foldersToRemove = ["build", "dist"]
    for item in os.listdir(filepath):
        if item.endswith("egg-info"):
            foldersToRemove.append(item)
    
    for folder in foldersToRemove:
        commandArray = ["rm", "-r", filepath + "/" + folder]
        subprocess.run(commandArray, capture_output=True)
