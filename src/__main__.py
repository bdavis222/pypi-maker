import argparse
import sys
import src.files as files
import src.imports as imports
import src.reset as reset
import src.upload as upload
from src.ui import navigation
from src.ui.OptionSelector import OptionSelector

INVALID_ARGUMENT_TEXT = "Invalid argument given. Must be 'generate', 'upload', 'reset', \
'fiximports', 'unfiximports', or 'help'."

ARGS_DESCRIPTION_TEXT = "Enter command 'generate', 'upload', 'reset', 'fiximports', \
'unfiximports', or 'help'"

HELP_TEXT = "\nPyPI Maker\n----------\n\n\
To run, enter 'pypimaker' followed by a valid command.\n\
Some examples:\n\n\
   pypimaker generate\n\
   pypimaker upload\n\
   pypimaker -r\
\n\nThe possible commands (or their aliases) are the following:\n\n\
   generate  (-g)\n\
   upload    (-u)\n\
   reset     (-r)\n\
   fix       (-f)\n\
   unfix     (-z)\n\
   help      (-h)\n\n\
See the documentation on GitHub or PyPI for more information.\n"

def main(argv=sys.argv):
	parser = argparse.ArgumentParser(description="Example input: pypimaker generate")
	parser.add_argument(
		"command", 
		type=str, 
		help=ARGS_DESCRIPTION_TEXT, 
		nargs=1
	)
	userOption = "help" if len(sys.argv) == 1 else sys.argv[1]
	
	if userOption in ["generate", "-g"]:
		options = OptionSelector()
		files.generate(
			options.filepath,
			options.projectName,
			options.authorsArray,
			options.emailsArray,
			options.correspondingEmail,
			options.githubUsername,
			options.shortDescription,
			options.classifier
		)
	
	elif userOption in ["upload", "-u"]:
		filepath = navigation.getDirectory()
		upload.upload(filepath)
	
	elif userOption in ["reset", "-r"]:
		filepath = navigation.getDirectory()
		reset.reset(filepath)
	
	elif userOption in ["fix", "-f"]:
		filepath = navigation.getDirectory()
		imports.fix(filepath)
	
	elif userOption in ["unfix", "-z"]:
		filepath = navigation.getDirectory()
		imports.unfix(filepath)
	
	elif userOption in ["help", "-h"]:
		print(HELP_TEXT)
	
	else:
		raise Exception(INVALID_ARGUMENT_TEXT)

if __name__ == '__main__':
	main()
