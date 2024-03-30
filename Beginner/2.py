### IMPORTS FUNCTIONS FOR REGEX (FOR HASH), IPADDRESS VALIDATION, AND WHOIS (DOMAIN) VALIDATION
import re
import ipaddress
import whois

### CHECK FUNCTION FOR ALL 3 INSTANCES
def check(x):
    if checkHash(x) == True:
        return print(f"https://www.virustotal.com/gui/file/{x}")
    elif checkIP(x) == True:
        return print(f"https://www.virustotal.com/gui/ip-address/{x}")
    elif checkDomain(x) == True:
        return print(f"https://www.virustotal.com/gui/domain/{x}")
    else:
        print("You have entered not a correct value.")

### CHECK FUNCTION FOR HASH, REGEX AND RETURNS THE CORRECT OUTPUT
def checkHash(x):
    MD5 = "^[a-fA-F0-9]{32}$" ### md5 test: 098f6bcd4621d373cade4e832627b4f6
    SHA1 = "^[a-fA-F0-9]{40}$" ### sha1 test: a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
    SHA256 = "^[a-fA-F0-9]{64}$" ### sha256 test: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
    
    if re.search(MD5, x):
        print("The value you have entered is MD5.")
        return True
    elif re.search(SHA1, x):
        print("The value you have entered is SHA1.")
        return True
    elif re.search(SHA256, x):
        print("The value you have entered is SHA256.")
        return True
    else:
        return False

### CHECKS THE IP ADDRESS FUNCTION
def checkIP(x):
    ### ip test: 163.116.145.30
    try:
        ip_obj = ipaddress.ip_address(x)
        print("The value you have entered is an IP Address.")
        return True
    except ValueError:
        return False

### CHECK THE DOMAIN FUNCTION BY WHOIS IF ITS REGISTERED
def checkDomain(x):
    ### domain test: google.com
    try:
      domain_info = whois.whois(x)
      print("The value you have entered is a domain.")
      return True
    except: 
      print("The value you have entered is not a registered domain.")
      return False

### PRINTS main lines
print("Welcome to the OSINT generator!")
value = input("\nPlease enter your malicious entity (i.e. IP Address, Hash Value (SHA1, SHA256, MD5), Domain):")
### starts the main functions
check(value)
