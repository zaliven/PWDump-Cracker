import hashlib
from argparser import get_cli_args
from brute import bruteforce, getCharset
'''
python dump.py -f 127.0.0.1.pwdump -method bruteforce -range 3 -mode 124
python dump.py -f 127.0.0.1.pwdump -method wordlist -wordlist=pass.txt
'''
def testAttempt(attempt):
    for hashTuple in hashes:
        if(hashlib.new('md4', attempt.encode('utf-16le')).hexdigest().upper() == hashTuple[1]):
            print(hashTuple[0] + " : " + attempt)

args = get_cli_args()
#collect hashes from pwdump
hashes = []
with open(args.filename.name) as f:
    for line in f:
        separated = line.split(":")
        if("NO PASSWORD" not in separated[3]):
            hashes.append((separated[0], separated[3]))

if(args.method == "wordlist"):
    with open(args.wordlist.name) as passes:
        for line in passes:
            testAttempt(line.strip("\n"))
else:
    charset = getCharset(args.mode)
    for attempt in bruteforce(charset, int(args.range)):
        if (args.verbose):
            print(attempt)
        testAttempt(attempt)

