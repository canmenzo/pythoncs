### pyperclip library for copypaste
import pyperclip
import re

### defang the url
def defang(userInput):
    new_url = userInput.replace("https", "hxxps")
    new_url = new_url.replace("http", "hxxp")
    new_url = new_url.replace("://", "[://]")
    new_url = new_url.replace(".", "[.]")
    return new_url

### main loop
print("Welcome to URL Defang Script!")
while True:
    
    # get input
    userInput = input("\nPlease enter your potentially malicious URL (or 'exit' to quit):")

    # exit validation
    if userInput.lower() == 'exit':
        print("Exiting...")
        break
    # regex validation for url
    elif re.match(r"(http|https):\/\/.*\..*",userInput):
        # call function defang
        final_url = defang(userInput)
        # print and copy to clipboard
        print(f"Defanged URL: {final_url} \n")
        print("Defanged URL has been copied to your clipboard.\n")
        pyperclip.copy(final_url)
    else:
        print("You have entered an incorrect URL.")