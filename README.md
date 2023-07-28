# PyPI Maker
> Software designed for simplifying PyPI Python package setups

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?business=UA5NL9MJSFMVY)

## Getting Started

### Dependencies

[Python 3](https://www.python.org/downloads/) must be installed before pypimaker can be installed.

### Installation

To install pypimaker, open a terminal window and run the following command:

```
pip install pypimaker
```

*(Note that the* `pip3` *command may be required instead of* `pip` *for some Python installations.)*

## Generating Your PyPI Files

To generate the files needed for your PyPI package, run the following command:

```
pypimaker generate
```

This will launch a graphical user interface that looks like the following:
![](https://github.com/bdavis222/pypimaker/blob/main/images/0.png)

Inputting the information for your project will generate all of the files needed for uploading it to PyPI (`LICENSE`, `README.me`, `requirements.txt`, and `setup.py`). This can be re-run at any time to re-generate these files.

## Uploading Your Finished Project to PyPI

If you don't yet have an account on PyPI, [register for one](https://pypi.org/account/register/). Once you've set up your account and you're ready to upload your package to PyPI (e.g., after you have updated the generated template `README.md` file to your liking), run the following command:

```
pypimaker upload
```

You will be asked to enter your PyPI username and password (which you've registered previously) in the terminal. Your project will then be uploaded to PyPI, and others can download it using the following command:

```
pip install <PROJECT_NAME>
```

*(Here, <PROJECT_NAME> is the name you selected when running `pypimaker generate`)*

## Resetting Your Project

At any time, all of the files generated by PyPI Maker can be removed with the following command:

```
pypimaker reset
```

## Making changes to your PyPI project

To make changes and update your project, simply re-run `pypimaker upload`. Follow the steps in the terminal to incremement your version number and your update will be pushed to PyPI.

*Note: the extraneous `+[CATransaction synchronize]` output in the terminal window is a known bug in macOS 13 that will not affect your project.*

## Authors

Brian Davis

## Release History

* 0.1.11
     * Bug fixes
* 0.1.0
     * Initial Release

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/bdavis222/pypimaker/blob/main/LICENSE) file for details.

## Development

### Testing

Tests for PyPI Maker use [Python's built-in unittest framework](https://docs.python.org/3/library/unittest.html), and are stored in the `tests` folder. To run tests, navigate to the top level of PyPI Maker's folder structure and run the following command:

```
python -m unittest
```

The same test framework can optionally be added to your own project: If there is not yet a folder named `tests` in the top level of your project's directory structure, then a dialog window will pop up asking if you would like to include template unit tests in your project when running `pypimaker generate`. Confirming this selection will create a `tests` folder with individual unit tests inside, corresponding to each of the Python files in your project. Of course, until writing test cases within each of these test files, they won't actually test anything.

### Bug Reports and Feature Requests

To report a bug, visit the [issues page](https://github.com/bdavis222/pypimaker/issues). New feature requests are also welcome!