import hashlib, binascii
import subprocess
import sys
import os

cmd = "powershell.exe \"Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -NoProfile -File getHashes.ps1' -Verb RunAs\""
os.system(cmd)

path = "getHashes.ps1"
#runas /user:Administrator powershell.exe -ExecutionPolicy Bypass C:\\Users\\nikita\\Documents\\hash\\getHashes.ps1
#p = subprocess.Popen(["runas /user:Administrator",  "powershell.exe", "getHashes.ps1"], stdout=sys.stdout, shell=True)
#result = subprocess.run([r'powershell.exe',  r'-ExecutionPolicy',  r'ByPass' r'./getHashes.ps1', " > passest.txt"], stdout=subprocess.PIPE, universal_newlines=True, shell=True)
#print(result.stdout)

    
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
        if not passw:
            continue
        for hashDict in hashes:
            if(hashlib.new('md4', passw.encode('utf-16le')).hexdigest().upper() == hashDict[1]):
                print(hashDict[0] + " : " + passw)