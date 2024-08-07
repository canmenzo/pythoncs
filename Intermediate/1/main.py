



# import library
import requests

### API functions
def callAPI(hashID):
    url = f"https://www.virustotal.com/api/v3/files/{hashID}"

    headers = {
        "accept": "application/json",
        "x-apikey": "{{ INSERT YOUR VT API KEY HERE}}"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

def menuOptions(menuChoice):
    match menuChoice:
    case "engineNo":
        print("")
    case "engineName":
        print("")
    case "verdict":
        print("")
    case "hits":
        print("")
    case "ransom":
        print("")
    case "keywords":
        print("")
    case _:
        print("Exiting the program...")
        exit()

### input for hash
hashID = input("Please enter the hash you'd like to investigate: \n")
# call function to grab api
callAPI(hashID)

menuChoice = input("Please choose one of the following: \n")
menuOptions(menuChoice)


