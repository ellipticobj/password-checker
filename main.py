from utils import *

acceptedsymbols = "!@#$%^&*()-_=+|;:'\",.<>?"

while True:
    password = input("input your password: ")
    print("checking password...")
    print("checking password length...", end='')
    lengthcheck = checklength(password)
    if not lengthcheck:
        print("fail")
    else:
        print("pass")
    print("checking character types...", end='')
    charcheck = checkcharactertypes(password)
    if not charcheck:
        print('fail')
    else:
        print('pass')
    print("checking against common passwords...", end='')
    rockyoucheck = checkrockyou(password)
    if not rockyoucheck:
        print("fail")
    else:
        print("pass")
    print(suggestimprovements())
    