
# import libraries
import random
import string
# import re

# # exit validation/sanitization
# def exitValidation(x):
#     try:
#         if x.lower() == 'exit':
#             print("Exiting...")
#             exit()
#         # elif x.isnumeric():
#         #     return
#         # elif re.match(r"(uppercase|lowercase|digits|special)",x):
#         #     return
#         # else:
#         #     print("Please enter a valid input.")
#     except ValueError:
#         print("Please enter a valid input.")

# # input validation
# def validate(x):
#     try:
#         if x.isnumeric():
#             return
#     except ValueError:
#         answer = input('Invalid input. Would like to try again? [y/n]: ')
#         if answer == 'y':
#             reqLength = int(input("Please enter the required length for the pw:\n"))

#         elif answer == 'n':
#             print('Thank you for using the password generator!')
#             exit()
#         else:
#             print("Invalid input.\n")
#             print("Exiting the program.")

# def checkChars(y):
#     if re.match(r"(uppercase|lowercase|digits|special)",x):
#         return
#     else:
#         print("Please enter a valid input.")

def genPw(reqLength, reqChar):
    # choosing characters
    allChars = ''
    if 'uppercase' in reqChar:
        allChars += string.ascii_uppercase
    if 'lowercase' in reqChar:
        allChars += string.ascii_lowercase
    if 'digits' in reqChar:
        allChars += string.digits
    if 'special' in reqChar:
        allChars += string.punctuation

    # generate random password based on chars and length
    password = ''.join(random.choice(allChars) for _ in range(reqLength))
    return password

# welcome msg
print("Welcome to password generator!")

# main loop
while True:

    ### input validation/sanitization
    # input for length
    reqLength = int(input("Please enter the required length for the pw:\n"))
     # input for chars
    reqChar = input("Enter required characters (uppercase, lowercase, digits, special), separated by commas:").strip().lower().split(',')

    # generate
    password = genPw(reqLength, reqChar)
    print("Generated Password:", password)