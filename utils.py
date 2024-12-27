from random import choice, shuffle
# vars to tweak

symbols = "!@#$%^&*()-_=+|;:'\",.<>?"
numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"

# generator
genlength = 12
minsymb = 3
minupper = 3
minlower = 3
minnum = 3



# checker
securepasslen = 8
securesymb = 1
secureupper = 1
securelower = 1
securenum = 1

def checklength(password):
    if len(password) < securepasslen:
        return False
    return True

def checksymbols(password, symbols):
    return sum(char in symbols for char in password) >= securesymb

def checkupper(password):
    return sum(char.isupper() for char in password) >= secureupper

def checklower(password):
    return sum(char.islower() for char in password) >= securelower

def checknumbers(password):
    return sum(char.isdigit() for char in password) >= securenum

def checkrockyou(password):
    with open('rockyou.txt', 'r') as file:
        for line in file:
            if password == line.strip():
                return False
    return True

def suggestimprovements(lengthcheck, charchecks, rockyoucheck):
    suggestion = []

    if not lengthcheck:
        suggestion.append("make your password at least 8 characters long")
        
    if not charchecks[0]:
        suggestion.append("add at least one symbol to your password")
        
    if not charchecks[1]:
        suggestion.append("add at least one uppercase letter to your password")
        
    if not charchecks[2]:
        suggestion.append("add at least one lowercase letter to your password")
        
    if not charchecks[3]:
        suggestion.append("add at least one number to your password")
    
    if not rockyoucheck:
        suggestion.append("do not use a common or easy to guess password")
        
    return suggestion

def generatepass():
    password = ''
    
    for i in range(securesymb):
        password += choice(symbols)
    for i in range(secureupper):
        password += choice(letters).upper()
    for i in range(securelower):
        password += choice(letters).lower()
    for i in range(securenum):
        password += choice(numbers)
    
    if len(password) < securepasslen:
        for i in range(securepasslen - len(password)):
            password += choice(symbols+letters.lower()+numbers+letters.upper())
    
    return ''.join(shuffle(list(password)))