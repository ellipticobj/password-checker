from ttkbootstrap import StringVar
import ttkbootstrap as ttk
from utils import *
from ttkbootstrap.constants import *

root = ttk.Window(themename="minty")
root.title("converter")
root.geometry("400x400")
root.minsize(400, 400)

default_font = ("Arial", 12)
style = ttk.Style()
style.configure(".", font=default_font)

def showpage(page):
    for frame in frames.values():
        frame.pack_forget()
    frames[page].pack(fill="both", expand=True)
    if page == "main page":
        inputfield.delete(0, ttk.END)

frames = {}
selectedfunc = ""

def checkpassword(usrpass):
    if not checklength(usrpass):
        lengthchecklabel.config(text="your password should be at least 8 characters", bootstyle="danger")
    
    if not checksymbols(usrpass):
        symbolchecklabel.config(text="your password should have symbols", bootstyle="danger")
    
    if not checkupper(usrpass):
        upperchecklabel.config(text="your password should have uppercase characters", bootstyle="danger")
    
    if not checklower(usrpass):
        lowerchecklabel.config(text="your password should have lowercase characters", bootstyle="danger")
    
    if not checknumbers(usrpass):
        numberchecklabel.config(text="your password should have numbers", bootstyle="danger")
    
    if not checkrockyou(usrpass):
        rockyouchecklabel.config(text="your password should not be easy to guess", bootstyle="danger")

def genpassword():
    generatedpassword = generatepass()
    genpasslabel.config(text=f"{generatedpassword}")

def resetlabels():
    lengthchecklabel.config(text="your password's length is okay!", bootstyle="success")
    symbolchecklabel.config(text="your password has symbols", bootstyle="success")
    upperchecklabel.config(text="your password has uppercase characters", bootstyle="success")
    lowerchecklabel.config(text="your password has lowercase characters", bootstyle="success")
    numberchecklabel.config(text="your password has numbers", bootstyle="success")
    rockyouchecklabel.config(text="your password is not in the list of common passwords", bootstyle="success")


frame1 = ttk.Frame(root)
frames["main page"] = frame1

titlelabel = ttk.Label(frame1, text="input your password or press generate password to generate a password")

inputfield = ttk.Entry(frame1)
inputfield.pack(pady=5)

checkpassbutton = ttk.Button(frame1, text="check password", command=lambda: (checkpassword(inputfield.get().strip()), showpage("check password")))
checkpassbutton.pack(pady=5)

genpassbutton = ttk.Button(frame1, text="generate password", command=lambda: (genpassword(), showpage("generate password")))
genpassbutton.pack(pady=5)


frame2 = ttk.Frame(root)
frames["check password"] = frame2

lengthchecklabel = ttk.Label(frame2, text="your password's length is okay!", bootstyle="success")
lengthchecklabel.pack(pady=5)

symbolchecklabel = ttk.Label(frame2, text="your password has symbols", bootstyle="success")
symbolchecklabel.pack(pady=5)

upperchecklabel = ttk.Label(frame2, text="your password has uppercase characters", bootstyle="success")
upperchecklabel.pack(pady=5)

lowerchecklabel = ttk.Label(frame2, text="your password has lowercase characters", bootstyle="success")
lowerchecklabel.pack(pady=5)

numberchecklabel = ttk.Label(frame2, text="your password has numbers", bootstyle="success")
numberchecklabel.pack(pady=5)

rockyouchecklabel = ttk.Label(frame2, text="your password is not in the list of common passwords", bootstyle="success")
rockyouchecklabel.pack(pady=5)

checkbackbutton = ttk.Button(frame2, text="back", command=lambda: (resetlabels(), showpage("main page")), bootstyle="outline")
checkbackbutton.pack(pady=5)


frame3 = ttk.Frame(root)
frames["generate password"] = frame3

genpasstitle = ttk.Label(frame3, text="generated password: ")
genpasstitle.pack(pady=5)

genpasslabel = ttk.Label(frame3, text="", bootstyle="success")
genpasslabel.pack(pady=5)

genbackbutton = ttk.Button(frame3, text="back", command=lambda: (showpage("main page")), bootstyle="outline")
genbackbutton.pack(pady=5)

showpage("main page")
root.mainloop()