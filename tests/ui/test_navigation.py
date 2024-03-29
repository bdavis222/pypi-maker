import unittest

from pypimaker import strings
import pypimaker.ui.navigation as navigation

# This unit test uses Python's built-in unit testing framework
# See https://docs.python.org/3/library/unittest.html for more information


class NavigationTest(unittest.TestCase):
    def test_getPathFromBase(self):
        self.assertEqual(
            navigation.getPathFromBase(
                base="path/to/base", target="path/to/base"),
            strings.DEFAULT_MAIN_FUNCTION_PATH
        )
        self.assertEqual(
            navigation.getPathFromBase(
                base="path/to/base", target="not/path/to/base"),
            strings.DEFAULT_MAIN_FUNCTION_PATH
        )
        self.assertEqual(
            navigation.getPathFromBase(
                base="path/to/base", target="path/not/to/base/to/target.py"),
            strings.DEFAULT_MAIN_FUNCTION_PATH
        )
        self.assertEqual(
            navigation.getPathFromBase(
                base="path/to/base", target="path/to/base/to/target.py"),
            "to.target"
        )
        self.assertEqual(
            navigation.getPathFromBase(
                base="path/to/base", target="path/to/base/to/deep/target.py"),
            "to.deep.target"
        )
        self.assertEqual(
            navigation.getPathFromBase(
                base="path/to/base", target="path/to/base/to/__target__.py"),
            "to.__target__"
        )


if __name__ == "__main__":
    unittest.main()
