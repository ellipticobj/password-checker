from utils import *

acceptedsymbols = "!@#$%^&*()-_=+|;:'\",.<>?"

while True:
    password = input("input your password: ")
    print("checking password...")
    
    
    print("    checking password length...", end='')
    lengthcheck = checklength(password)
    if not lengthcheck:
        print("fail")
    else:
        print("pass")
    
    
    print("    checking character types...")
    
    print("        checking symbols...", end='')
    symbolcheck = checksymbols(password, acceptedsymbols)
    print("pass" if symbolcheck else "fail")
    
    print('        checking uppercase...', end='')
    uppercheck = checkupper(password)
    print("pass" if uppercheck else "fail")
    
    print('        checking lowercase...', end='')
    lowercheck = checklower(password)
    print("pass" if lowercheck else "fail")
    
    print("        checking numbers...", end='')
    numcheck = checknumbers(password)
    print("pass" if numcheck else "fail")
    
    print("    done")
    
    print("  checking against common passwords...", end='')
    rockyoucheck = checkrockyou(password)
    if not rockyoucheck:
        print("fail")
    else:
        print("pass")
    
    print(suggestimprovements())
    