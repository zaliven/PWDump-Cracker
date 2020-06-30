import argparse
import os.path
import sys

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist" % arg)
    else:
        return open(arg, 'r')

def get_cli_args():
    parser = argparse.ArgumentParser(description="PWDump Cracker")
    parser.add_argument("-f", dest="filename", required=True, help="Enter pwdump file to crack", type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-method", dest="method", required=True, help="Enter desired method", choices=["bruteforce", "wordlist"])
    if(0 <= 4 <= len(sys.argv)):
        if (sys.argv[4] == "wordlist"):
            parser.add_argument("-wordlist", dest="wordlist", required=True, help="Enter the wordlist file you want to use", type=lambda x: is_valid_file(parser, x))
        else:
            parser.add_argument("-range", dest="range", required=True, help="Enter the bruteforce pass length")
            parser.add_argument("-mode", dest="mode", required=True, help="Enter bruteforce mode (you may concatenate modes): 1 - numeric | 2 - lower alpha | 3 - upper alpha | 4 - symbols", metavar="MODE")
            parser.add_argument('-v', '--verbose', action="store_true", help="View bruteforce output")            
    return parser.parse_args()



