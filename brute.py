from itertools import chain, product
import string
def getCharset(mode):
    charset = ""
    if '1' in mode:
        charset += string.digits
    if '2' in mode:
        charset += string.ascii_lowercase
    if '3' in mode:
        charset += string.ascii_uppercase
    if '4' in mode:
        charset += "!@#$%^&*()-_+=~`[]\{\}|\\:;\"'<>,.?/ "
    return charset

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
