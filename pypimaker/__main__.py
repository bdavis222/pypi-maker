import argparse
import sys

from src import strings
import src.files as files
import src.reset as reset
import src.upload as upload
from src.ui import navigation
from src.ui.OptionSelector import OptionSelector


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(
        description="Example input: pypimaker generate")
    parser.add_argument(
        "command",
        type=str,
        help=strings.ARGS_DESCRIPTION_TEXT,
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
            options.classifier,
            options.mainFunctionPath
        )

    elif userOption in ["upload", "-u"]:
        filepath = navigation.getDirectory()
        upload.upload(filepath)

    elif userOption in ["reset", "-r"]:
        filepath = navigation.getDirectory()
        reset.reset(filepath)

    elif userOption in ["help", "-h"]:
        print(strings.HELP_TEXT)

    else:
        print(strings.HELP_TEXT)


if __name__ == '__main__':
    main()
