

### ASSIGN GLOBAL VARIABLES
OLD_DOMAIN = ["https://www.olddomain.com", "http://www.olddomain.com", "www.olddomain.com", "olddomain.com"]
NEW_DOMAIN = "https://www.newdomain.com"

### CHECKURL FUNCTION 
def checkUrl(x):
    if "http://" in x or "https://" in x and "www." in x and ".io" in x or ".com" in x:
        return True
    else:
        return False

### MAIN FUNCTION:
### CHECKS IF INPUT IS OLD DOMAIN AND AN ACTUAL URL, RETURN NEW DOMAIN IF YES, IF NOT RETURNS PROPER ERROR MESSAGE
def main(OldDomain):
    if OldDomain in OLD_DOMAIN and checkUrl(OldDomain) == True:
        print("The New Domain is", NEW_DOMAIN)
    elif OldDomain in OLD_DOMAIN and checkUrl(OldDomain) == False:
        print("Old Domain you have entered is not a valid URL.")
    else:
        print("You have entered a wrong Old Domain.")

### CODE
if __name__ == "__main__":
    ### THIS ENSURES THAT CODE IS RAN OUTSIDE ONLY BY RUNNING THE SCRIPT TO ENSURE MODULE / FUNCTION RUNNING ONCE.
    OldDomain = input('Please enter the Old Domain:')
    main(OldDomain)
