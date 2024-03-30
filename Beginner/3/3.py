




import pyperclip


print("Welcome to URL Defang Script!")
old_url = input("\nPlease enter your potentially malicious URL:")

if old_url.find("https") == 0:
    new_url = old_url.replace("https://", "hxxps[://]")
elif old_url.find("http") == 0:
    new_url = old_url.replace("http://", "hxxp[://]")
else:
    print("You have entered an incorrect URL.")

print(f"Defanged URL: {new_url} \n")
print("Defanged URL has been copied to your clipboard.")
pyperclip.copy(new_url)