# PWDump Cracker

Attempts to crack a pwdump file with either a wordlist attack or brute force.
Before using this tool you need to have a pwdump file - it is possible to get one using the fgdump tool.


## Usage
```
python dump.py -f FILENAME -method wordlist -wordlist WORDLIST
;
python dump.py -f FILENAME -method bruteforce -range RANGE -mode MODE [-v]
```

FILENAME - pwdump file
method - desired method

wordlist - wordlist file

range - password length to bruteforce
mode - bruteforce mode. 1 - numeric | 2 - lower alpha | 3 - upper alpha | 4 - symbols. It is possible to combine modes (124 for example)
