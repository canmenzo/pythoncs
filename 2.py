
import re
from IPy import IP


def check(x):
    if checkHash(x) == True:
        return print(f"https://www.virustotal.com/gui/file/{x}")
    if checkIP(x) == True:
        return print(f"https://www.virustotal.com/gui/ip-address/{x}")
    if checkDomain(x) == True:
         return print(f"https://www.virustotal.com/gui/domain/{x}")
    else:
        print("You have not entered an IP Address or a Hash value or a Domain.")

def checkIP(x):
    try:
        if IP(x) == True:
            return True
    except ValueError as e:
        return False

def checkHash(x):
    MD5 = "^[a-fA-F0-9]{32}$" ### md5 test: 098f6bcd4621d373cade4e832627b4f6
    SHA1 = "^[a-fA-F0-9]{40}$" ### sha1 test: a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
    SHA256 = "^[a-fA-F0-9]{64}$" ### sha256 test: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

    if re.search(MD5, x):
        return True
    elif re.search(SHA1, x):
        return True
    elif re.search(SHA256, x):
        return True
    else:
        return False

print("Welcome to the OSINT generator!")
value = input("\nPlease enter your malicious entity (i.e. IP Address, Hash Value (SHA1, SHA256, MD5), Domain):")

check(value)