from tkinter import *

top=Tk()
top.geometry("400x400")

def rst():
	user.set("")
	passw.set("")
	repassw.set("")

def chk():
	if passw.get()!=repassw.get():
		print("Password mismatch !")
	else:
		print("Username is :",user.get())
		print(passw.get())

user=StringVar()
passw=StringVar()
repassw=StringVar()
var=StringVar()

lb1=Label(top,text="Username").grid(row=4)
t1=Entry(top,textvariable=user).grid(row=5)

lb2=Label(top,text="Password").grid(row=7)
t2=Entry(top,show="*",exportselection=0,textvariable=passw).grid(row=8)

lb3=Label(top,text="Re-enter Password").grid(row=12)
t3=Entry(top,show="*",exportselection=0,textvariable=repassw).grid(row=13)

# exportselection - text within an Entry widget, it is exported to the clipboard.To avoid this exportation, use exportselection = 0.
# show - To make a password entry show = "*".
# textvariable - to retrieve the current text from your entry widget,set this option to an instance of the StringVar class.

label = Message(top, textvariable = var, relief = RAISED )
var.set("Hey!? How are you doing?")
label.grid(row=15)
# Message()
#Its functionality is very similar to the one provided by the Label widget, 
#except that it can also automatically wrap the text, maintaining a given width or aspect ratio.

sbt=Button(top,text="SUBMIT",command=chk).grid(row=17)
qbt=Button(top,text="QUIT",command=top.quit).grid(row=19)
rbt=Button(top,text="RESET",command=rst).grid(row=23)

top.mainloop()
