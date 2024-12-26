def checklength(password):
    if len(password) < 8:
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
        suggestion += ["make your password at least 8 characters long"]
        
    if not charchecks[0]:
        suggestion += ["add at least one symbol to your password"]
        
    if not charchecks[1]:
        suggestion += ["add at least one uppercase letter to your password"]
        
    if not charchecks[2]:
        suggestion += ["add at least one lowercase letter to your password"]
        
    if not charchecks[3]:
        suggestion += ["add at least one number to your password"]
    
    if not rockyoucheck:
        suggestion += ["do not use a common or easy to guess password"]
        
    return suggestion

