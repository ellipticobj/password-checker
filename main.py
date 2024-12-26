from utils import *

acceptedsymbols = "!@#$%^&*()-_=+|;:'\",.<>?"

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
charchecks[0] = checksymbols(password, acceptedsymbols)
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

if suggestions:
    print("\nSuggestions to improve your password:")
    for line in suggestions:
        print(line)