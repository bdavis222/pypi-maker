import unittest
import src.upload as upload

# This unit test uses Python's built-in unit testing framework
# See https://docs.python.org/3/library/unittest.html for more information

class UploadTest(unittest.TestCase):
    def test_correctlyDetectsLargerVersionNumber(self):
        self.assertTrue(upload.versionNumberGreater("1.0.12", "1.0.3"))
        self.assertTrue(upload.versionNumberGreater("1.1.2", "1.0.5"))
        self.assertTrue(upload.versionNumberGreater("0.1.2", "0.0.9"))
        self.assertFalse(upload.versionNumberGreater("0.0.2", "1.0.0"))
        self.assertFalse(upload.versionNumberGreater("5.4.3", "5.5.1"))
        self.assertFalse(upload.versionNumberGreater("1.0.2", "1.0.2"))
    
    def test_getLargestVersionNumber(self):
        versions = ["1.0.12", "1.0.3", "1.1.2", "1.0.5", "5.4.3", "5.5.1", "0.0.2", "1.0.0"]
        largest = upload.getLargestVersionNumber(versions)
        self.assertEqual(largest, "5.5.1")
    
    def test_isValidVersionNumber(self):
        self.assertTrue(upload.isValidVersionNumber("0.0.1"))
        self.assertTrue(upload.isValidVersionNumber("0.12.519"))
        self.assertTrue(upload.isValidVersionNumber("9.0.1"))
        self.assertFalse(upload.isValidVersionNumber("1.0"))
        self.assertFalse(upload.isValidVersionNumber("0.4.g"))
        self.assertFalse(upload.isValidVersionNumber("test"))

if __name__ == "__main__":
    unittest.main()
