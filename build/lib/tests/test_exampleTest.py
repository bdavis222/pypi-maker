# import mock 
# import unittest 

# # Below is an example of a test class used for another program. This will not run, as many things 
# # are not actually imported here, and the files themselves are not contained in this template project

# class TestExample(unittest.TestCase):
#     # Test case 1 (just an example of how a test case should be named)
#     def test_condition_doesThis_whenThis(self):
#         pass
    
#     # Test case 2 (with function mocks)
#     @mock.patch("dotscanner.files.os.path.basename") # Mocking a function return value
#     @mock.patch("dotscanner.files.os.path.dirname") # Mocking a function return value
#     @mock.patch("dotscanner.files.os.path.isfile") # Mocking a function return value
#     # Note that the mocks are passed in as parameters IN REVERSE ORDER to the declarations above
#     def test_getDirectoryAndFilenames_getsSingleFile_whenSelectedPathIsFile(self, mock_isfile, mock_dirname, mock_basename):
#         # Convention is to have three code blocks in a test. The first is all of the setup:
#         # Mock return values defined here:
#         mock_isfile.return_value = True
#         mock_dirname.return_value = "test/directory/"
#         mock_basename.return_value = "testFile.png"
#         # Any fake objects needed defined here:
#         fakeUserSettings = FakeUserSettings()
        
#         # The second code block is all of the actions:
#         directory, filenames = files.getDirectoryAndFilenames(fakeUserSettings)
#         # os.path.basename, os.path.dirname, and os.path.isfile are all used somewhere within this 
#         # getDirectoryAndFilenames method, which is why their return values were mocked above
        
#         # The third code block is all of the assertions
#         self.assertEqual(directory, "test/directory/")
#         self.assertEqual(filenames, ["testFile.png"])
    
#     # Test case 3 (with a variable mock)
#     @mock.patch("settings.config.DENSITY_OUTPUT_FILENAME", "density.txt") # Mocking a variable
#     def test_outputString_signifiesSkip_whenFileWasAlreadyMeasured(self):
#         output = strings.alreadyMeasuredNotification(filename="test.png")
        
#         self.assertEqual(
#             output, 
#             f"\nFile test.png already measured in density.txt file. Skipping."
#         )

# if __name__ == "__main__":
#     unittest.main()
