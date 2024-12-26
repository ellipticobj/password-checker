def checklength(password):
    if len(password) < 8:
        return False
    return True

def checksymbols(password, acceptedsymbols):
    return any(char in acceptedsymbols for char in password)

def checkupper(password):
    return any(char.isuppr() for char in password)

def checklower(password):
    return any(char.islower() for char in password)

def checknumbers(password):
    return any(char.isdigit() for char in password)

def checkrockyou(passwords):
    # TODO: check the passwords against rockyou.txt
    return 0

def suggestimprovements():
    # TODO: figure out how to suggest improvements for the passwords
    suggestion = '''suggestions to improve your password:'''
    return suggestion

