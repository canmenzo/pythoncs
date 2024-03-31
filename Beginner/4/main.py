
### all comments can be found in the [failedInputValidation.py](./Beginner/4/failedInputValidation.py)
import random
import string

### thank you chatgpt for the inputvalidation, took 7 prompts.
def get_valid_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'exit':
            exit()
        elif valid_options:
            input_list = [option.strip() for option in user_input.split(',')]
            if any(option in valid_options for option in input_list):
                return input_list
            else:
                print("Invalid input. Please include at least one of the required character types.")
        elif user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer or type 'exit' to quit.")

def genPw(reqLength, reqChar):
    allChars = ''
    if 'uppercase' in reqChar:
        allChars += string.ascii_uppercase
    if 'lowercase' in reqChar:
        allChars += string.ascii_lowercase
    if 'digits' in reqChar:
        allChars += string.digits
    if 'special' in reqChar:
        allChars += string.punctuation

    password = ''.join(random.choice(allChars) for _ in range(reqLength))
    return password

print("Welcome to password generator!")

while True:
    reqLength = get_valid_input("Please enter the required length for the password (type 'exit' to quit): ")
    reqChar = get_valid_input("Enter required characters (uppercase, lowercase, digits, special), separated by commas (type 'exit' to quit): ", {'uppercase', 'lowercase', 'digits', 'special'})
    
    password = genPw(reqLength, reqChar)
    print("Generated Password:", password)
