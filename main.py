from utils import *

# TODO: make a password generator
# TODO: make a way for the user to type in the password without it being displaye?
# TODO: gui?

while True:
    choice = input("1. Check your password strength\n2. Generate a secure password\nInput your choice[1/2]: ")
    while choice not in ['1','2']:
        choice = input("1. Check your password strength\n2. Generate a secure password\nInput your choice[1/2]: ")
    
    if choice == "1":
        password = input("input your password: ")
        print("checking password...")


        print("    checking password length...", end='')
        lengthcheck = checklength(password)
        if not lengthcheck:
            print("fail")
        else:
            print("pass")


        print("    checking character types...")
        #             symbol, upper, lower, num
        charchecks = [False, False, False, False]

        print("        checking symbols...", end='')
        charchecks[0] = checksymbols(password, symbols)
        print("pass" if charchecks[0] else "fail")

        print('        checking uppercase...', end='')
        charchecks[1] = checkupper(password)
        print("pass" if charchecks[1] else "fail")

        print('        checking lowercase...', end='')
        charchecks[2] = checklower(password)
        print("pass" if charchecks[2] else "fail")

        print("        checking numbers...", end='')
        charchecks[3] = checknumbers(password)
        print("pass" if charchecks[3] else "fail")

        print("    fail" if False in charchecks else "    pass")

        print("  checking against common passwords...", end='')
        rockyoucheck = checkrockyou(password)
        if not rockyoucheck:
            print("fail")
        else:
            print("pass")

        print("fail" if lengthcheck == False or rockyoucheck == False or False in charchecks else "pass")

        suggestions = suggestimprovements(lengthcheck,charchecks,rockyoucheck)

        print("\nfeedback:")
        if suggestions:
            for line in suggestions:
                print(line)
        else:

            print("looking good!")
    
    elif choice == "2":
        print(f"This is your secure password: {generatepass()}")