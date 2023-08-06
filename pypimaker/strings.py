ARGS_DESCRIPTION_TEXT = "Enter command 'generate', 'upload', 'reset', or 'help'"

HELP_TEXT = """
PyPI Maker
----------

To run PyPI Maker, enter 'pypimaker' followed by a valid command.
Some examples:

   pypimaker generate
   pypimaker upload
   pypimaker -r

The possible commands (or their aliases) are the following:

   generate  (-g)
   upload    (-u)
   reset     (-r)
   help      (-h)

See the documentation on GitHub for more information:
https://github.com/bdavis222/pypimaker
"""

DEFAULT_INITIAL_VERSION = "0.1.0"

PROJECT_DESCRIPTION_TEXT = 'One-sentence Project Description (e.g., "Software designed for..."):'
SELECT_FOLDER_TEXT = "Select the top-level folder containing your Python project"
PROJECT_NAME_DESCRIPTION_TEXT = '(Your package will be installed with the "pip install \
project_name" command using the project name given above.)'

MISMATCHED_SELECTION_TEXT = "Mismatched folder name and project name.\nAre you sure you selected correctly?"
NO_PYTHON_FILES_IN_PROJECT_FOLDER_TEXT = "No Python files found in folder.\nSelect a different folder."
PROJECT_FOLDER_NOT_CHOSEN_TEXT = "You must select your project \nusing the Browse button."
PROJECT_NAME_NOT_CHOSEN_TEXT = "Project Name is a required field.\nUse folder name as project name?"

NO_MAIN_FUNCTION_TITLE = "Main function not found"
MUST_SELECT_MAIN_FILE = 'No "main" function found.\nChoose a file containing\nthe main entry point function?'
NO_MAIN_FOUND_AFTER_SELECTION_TEXT = 'The selected file does not contain\na function named "main" for your project.'

MISSING_AUTHOR_NAMES_TEXT = "Some emails have missing author names.\nPlease fix and resubmit."
MISSING_FIRST_NAME_TEXT = "Corresponding author name not given.\nSubmit with no authors?"
MISSING_FIRST_AUTHOR_EMAIL_TEXT = "Email given for other(s), but not first author.\n\
Use next email in list for correspondence?"

RESET_SELECTION_TEXT = "This will remove generated files.\nAre you sure you want to reset?"

UNIT_TEST_CREATION_PROMPT_TEXT = '''Create template unit test files?
These will be placed in a "tests" folder
within your main project folder.'''

TEST_FILE_CONTENTS = '''import unittest
{importString}

# This unit test uses Python's built-in unit testing framework
# See https://docs.python.org/3/library/unittest.html for more information

class {camelName}Test(unittest.TestCase):
    def test_condition_doesThis_whenThis(self):
        pass

if __name__ == "__main__":
    unittest.main()
'''

LICENSE_FILE_CONTENTS = '''MIT License
{copyrightLine}
Permission is hereby granted, free of charge, to any person obtaining a copy \
of this software and associated documentation files (the "Software"), to deal \
in the Software without restriction, including without limitation the rights \
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell \
copies of the Software, and to permit persons to whom the Software is \
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all \
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, \
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER \
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, \
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE \
SOFTWARE.'''

README_CONTENTS = """# {projectName}
{blurbLine}
This Python package was created and uploaded to PyPI using [PyPI Maker](https://github.com/bdavis222/pypimaker). \
This is a template README generated by PyPI Maker.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](PAYPAL_DONATE_LINK_GOES_HERE)

OPTIONAL: ENTER A 2-3 SENTENCE DESCRIPTION ABOUT THE SOFTWARE HERE

## Getting Started

### Dependencies

[Python 3](https://www.python.org/downloads/) must be installed before {projectName} can be installed.

### Installation

To install {projectName}, open a terminal window and run the following command:

```
pip install {projectName}
```

*(Note that the* `pip3` *command may be required instead of* `pip` *for some Python installations.)*

### Running the Software

To launch the main program, run the following command:

```
{projectName}
```

## SOME_OTHER_HEADER

IMAGES INCLUDED BY LINKING TO THEIR LOCATION IN THE PROJECT, E.G.:
![](https://github.com/bdavis222/dotscanner/blob/main/images/3.png)
{authorSection}
## Release History

* {version}
     * Initial Release

## License

This project is licensed under the MIT License. {licenseDetails}

## Development

To contribute, download or clone the project. From the top level of the project's folder structure, \
one can use the following command to run a local version of the software (e.g., for UI testing):

```
python -m pypimaker
```

*(Note that the* `python3` *command may be required instead of* `python` *for some Python installations.)*

### Testing

Unit tests for this software were written for use with [Python's built-in unittest \
framework](https://docs.python.org/3/library/unittest.html), and are stored in the `tests` folder. \
To run tests, download the project, navigate to the top level of the project's folder structure and \
run the following command:

```
python -m unittest
```
{bugReports}
"""

AUTHOR_SECTION_CONTENTS = "\n## Authors\n\n{namesAndEmails}\n"

LICENSE_DETAILS_CONTENTS = "See the [LICENSE](https://github.com/{githubUsername}/{projectName}/blob/main/LICENSE) file for details."

BUG_REPORTS_CONTENTS = """
### Bug Reports and Feature Requests\n\

To report a bug, visit the [issues page](https://github.com/{githubUsername}/{projectName}/issues). \
New feature requests are also welcome!"""

SETUP_FILE_CONTENTS = """from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='{projectName}',  # Required
    version='{version}',  # Required {descriptionLine}
    long_description=long_description,
    long_description_content_type='text/markdown',\
{githubUrlLine}{authorNameLine}{authorEmailLine}{classifiers}
    packages=find_packages(),  # Required
    py_modules={pyModules},  # Generated
    python_requires='>=3.7, <4', {githubProjectUrlsLine}
    entry_points={{
        'console_scripts': [
            '{projectName} = {mainFunctionPath}:main'
        ]
    }}
)
"""

DEFAULT_MAIN_FUNCTION_PATH = "src.__main__"

GITHUB_URL_LINE_CONTENT = "\n    url='https://github.com/{username}/{projectName}',"

GITHUB_PROJECT_URLS_LINE_CONTENT = """
    project_urls={{
        'Bug Reports': 'https://github.com/{username}/{projectName}/issues',
        # 'Funding': 'PAYPAL_DONATE_LINK_GOES_HERE',
        'Source': 'https://github.com/{username}/',
    }},"""

CLASSIFIERS_CONTENT = """
    classifiers=[ # Defined at https://pypi.org/classifiers/
        'Intended Audience :: {classifier}',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows'
    ],"""

INTENDED_AUDIENCES_LIST = [
    "N/A",
    "Customer Service",
    "Developers",
    "Education",
    "End Users/Desktop",
    "Financial and Insurance Industry",
    "Healthcare Industry",
    "Information Technology",
    "Legal Industry",
    "Manufacturing",
    "Other Audience",
    "Religion",
    "Science/Research",
    "System Administrators",
    "Telecommunications Industry"
]
