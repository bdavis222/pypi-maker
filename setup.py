from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
	name='pypimaker', # Required
    version='0.1.3', # Required 
    description='Software designed for simplifying PyPI Python package setups',
	long_description=long_description,
	long_description_content_type='text/markdown',
    url='https://github.com/bdavis222/pypimaker',
    author='Brian Davis',
	classifiers=[ # Defined at https://pypi.org/classifiers/
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Operating System :: Unix',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows'
	],
	packages=find_packages(), # Required
	py_modules=['tests', 'src.ui', 'src'], # Generated
	python_requires='>=3.7, <4', 
	project_urls={
		'Bug Reports': 'https://github.com/bdavis222/pypimaker/issues',
		'Funding': 'https://www.paypal.com/donate/?business=UA5NL9MJSFMVY',
		'Source': 'https://github.com/bdavis222/',
	},
	entry_points={
		'console_scripts': [
			'pypimaker = src.__main__:main'
		]
	}
)