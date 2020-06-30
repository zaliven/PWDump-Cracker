import argparse
import os.path
import sys

class Parser:
    def __init__(self):
        parser = argparse.ArgumentParser(description="PWDump Cracker")
        parser.add_argument("-f", dest="filename", required=True, help="Enter the pwdump file you want to use", metavar="FILE", type=lambda x: self.is_valid_file(parser, x))
        parser.add_argument("-method", dest="method", required=True, help="Enter desired method (bruteforce/wordlist)", metavar="METHOD", choices=["bruteforce", "wordlist"])

        if (0 <= 4 <= len(sys.argv) and sys.argv[4] == "wordlist"):
            parser.add_argument("-wordlist", dest="wordlist", required=True, help="Enter the wordlist file you want to use", metavar="WORDLIST", type=lambda x: self.is_valid_file(parser, x))

        self.args = parser.parse_args()

    def is_valid_file(self, parser, arg):
        if not os.path.exists(arg):
            parser.error("The file %s does not exist" % arg)
        else:
            return open(arg, 'r')


    
#args.filename.name - file name
#args.method - method
#args.wordlist.name - wordlist var
