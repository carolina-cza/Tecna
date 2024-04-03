import string #allows access to the full range of string characters
import getpass 

def check_password_strength():
    password = getpass.getpass('Enter the password: ')
    strength = 0
    remarks = ' '
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        # elif char == ' ':
        #     wspace_count += 1
        else: 
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = ("That is a very bad password. Change it.") 
    elif strength == 2:
        remarks = ("That is a weak password.")
    elif strength == 3:
        remarks = ("Your password is okay, but it can be improved.")
    elif strength == 4:
        remarks = ("Your password is good.")
    elif strength == 5:
        remarks = ("Now that is a good one.")

    print("Your password has: -")
    print(f'{lower_count} lowercase letters')
    print(f"{upper_count} uppercase letters")
    print(f'{num_count} digits')
    print(f'{wspace_count} whitespaces')
    print(f"{special_count} special characters")
    print(f"Password Score: {strength /5}")
    print(f'Remarks: {remarks}')

def check_pwd(another_pw= False):
    valid = False
    if another_pw:
        choice = input("Do you want to check another password strenght (yes/no) :")
    else:
        choice = input("Do you want to check your password strenght (yes/no) :")
    
    while not valid:
        if choice.lower() == "yes":
            return True
        elif choice.lower() == "no":
            print("Exiting...")
            return False
        else:
            print("Invalid input... please try again. \n")
            break
    
if __name__ == '__main__':
    print("==== Welcome to Password Strenght Checker ====")
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)