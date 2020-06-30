import hashlib, binascii
import sys
import argparser


myParser = argparser.Parser()
#collect hashes
hashes = []
with open("127.0.0.1.pwdump") as f:
    for line in f:
        separated = line.split(":")
        if("NO PASSWORD" not in separated[3]):
            hashes.append((separated[0], separated[3]))

#we will compare output of word list to hashes
with open('pass.txt') as passes:
    for line in passes:
        passw = line.strip("\n")
        for hashTuple in hashes:
            if(hashlib.new('md4', passw.encode('utf-16le')).hexdigest().upper() == hashTuple[1]):
                print(hashTuple[0] + " : " + passw)