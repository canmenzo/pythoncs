### import defang library
from defang import defang

### welcome msg / get input
print("Welcome to URL Defang Script!")
old_url = input("\nPlease enter your potentially malicious URL:")


print(defang(old_url))