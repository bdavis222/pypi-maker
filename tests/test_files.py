import unittest
import pypimaker.files as files

# This unit test uses Python's built-in unit testing framework
# See https://docs.python.org/3/library/unittest.html for more information

class FilesTest(unittest.TestCase):
	def test_getNamesAndEmailsVerticallySpaced_spacesInfoProperly(self):
		authorsArray = ["John Doe", "Jane Toe"]
		emailsArray = ["john@gmail.com", "jane@hotmail.com"]
		expectedOutput = "John Doe (john@gmail.com)\n\nJane Toe (jane@hotmail.com)"
		
		output = files.getNamesAndEmailsVerticallySpaced(authorsArray, emailsArray)
		
		self.assertEqual(output, expectedOutput)
	
	def test_getAuthorsNameLine(self):
		emptyNameLine = files.getAuthorsNameLine([])
		singleNameLine = files.getAuthorsNameLine(["John Doe"])
		doubleNameLine = files.getAuthorsNameLine(["John Doe", "Jane Toe"])
		tripleNameLine = files.getAuthorsNameLine(["John Doe", "Jane Toe", "Bob Smith"])
		
		self.assertEqual(emptyNameLine, "")
		self.assertEqual(singleNameLine, "\n    author='John Doe',")
		self.assertEqual(doubleNameLine, "\n    author='John Doe and Jane Toe',")
		self.assertEqual(tripleNameLine, "\n    author='John Doe, Jane Toe, and Bob Smith',")
	
	def test_getAuthorNamesInline(self):
		noNamesLine = files.getAuthorNamesInline([])
		oneNameLine = files.getAuthorNamesInline(["John Doe"])
		twoNamesLine = files.getAuthorNamesInline(["John Doe", "Jane Toe"])
		threeNamesLine = files.getAuthorNamesInline(["John Doe", "Jane Toe", "Bob Smith"])
		
		self.assertEqual(noNamesLine, "")
		self.assertEqual(oneNameLine, "John Doe")
		self.assertEqual(twoNamesLine, "John Doe and Jane Toe")
		self.assertEqual(threeNamesLine, "John Doe, Jane Toe, and Bob Smith")
	
	def test_getAuthorEmailLine(self):
		noEmailOutput = files.getAuthorEmailLine("")
		emailOutput = files.getAuthorEmailLine("john@gmail.com")
		
		self.assertEqual(noEmailOutput, "")
		self.assertEqual(emailOutput, "\n    author_email='john@gmail.com',")
	
	def test_getDescriptionLine(self):
		noDescriptionOutput = files.getDescriptionLine("")
		descriptionOutput = files.getDescriptionLine("fake description")
		
		self.assertEqual(noDescriptionOutput, "")
		self.assertEqual(descriptionOutput, "\n    description='fake description',")
	
	def test_getGithubInfo_returnsListOfEmptyStrings_whenUsernameIsEmptyString(self):
		self.assertEqual(files.getGithubInfo("", "testProjectName"), ["", ""])
	
	def test_getClassifiers_returnsEmptyString_whenClassifierIsDefaultOrNotApplicable(self):
		self.assertEqual(files.getClassifiers("N/A"), "")
		self.assertEqual(files.getClassifiers("Select..."), "")

if __name__ == "__main__":
	unittest.main()
