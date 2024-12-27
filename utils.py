# vars to tweak

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

def checksymbols(password, acceptedsymbols):
    return any(char in acceptedsymbols for char in password)

def checkupper(password):
    return any(char.isupper() for char in password)

def checklower(password):
    return any(char.islower() for char in password)

def checknumbers(password):
    return any(char.isdigit() for char in password)

def checkrockyou(password):
    # TODO: check the passwords against rockyou.txt
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
    
    return 0