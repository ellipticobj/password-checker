import sys
import tty
import termios

def getpassword(prompt="Input password: ",showasterisk=False):
    
    password = ""
    
    sys.stdout.write(prompt)
    sys.stdout.flush()
    
    # get file descriptor (identifier thingy) for stdin
    stdinfd = sys.stdin.fileno()
    
    # save settings of terminal before i set it to raw input
    oldsettings = termios.tcgetattr(stdinfd)
    
    tty.setraw(stdinfd)
    
    while True:
        char = sys.stdin.read(1)
        # break if user presses enter
        if char == "\n" or char == "\r":
            break
        # remove one character from the password if backspace is pressed
        elif char == "\x7f": 
            if password:
                password = password[:-1]
                if showasterisk:
                    # removes last character
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
        else:
            password += char
            if showasterisk:
                sys.stdout.write("*")
                sys.stdout.flush()
    
    termios.tcsetattr(stdinfd, termios.TCSADRAIN, oldsettings)

    return password