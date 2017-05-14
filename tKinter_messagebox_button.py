#Pyhton3

from tkinter import *
from tkinter import messagebox
# note that module name has changed from Tkinter in Python 2 to tkinter in Python3

top=Tk()                                                 # window1
top.geometry("500x500")

#top2=Tk()                                               # window2

def func():
	messagebox.showinfo("hello","Clicked Text button")

def func2():
	res=messagebox.askquestion("hello","Clicked Image button")
	if res=="yes":
		print("Clicked Yes")
	else:
		print("Clicked No")

		#messagebox.showinfo()
		#messagebox.showerror()
		#messagebox.showwarning()
		#messagebox.askquestion()
                                                       #text button
bt=Button(top,text="hello",command=func,activebackground="#fff",activeforeground="#000",bg="#0ff",fg="#f00",bd="3",
	height="2",width="10",underline="2",font="bold")  

im=PhotoImage(file="forces.png")                      #image button
bt2=Button(top,image=im,command=func2)

        #activebackground - color of button when under cursor
        #activeforeground - color of text when under cursor
        #bg -               normal bgcolor
        #fg -               normal textcolor
        #bd -               border width
        #underline -        underline the particular character

bt.place(x=200,y=200) 
bt2.place(x=250,y=400)
        #Just one widget with PLACE, even when looped
        #The PLACE geometry manager organizes widgets by placing them in a specific position in the parent widget.
b=0
for r in range(6):
    for c in range(6):
        b = b + 1
        Button(top, text = str(b)).grid(row = r,column =c) 
        #A grid of buttons is obtained
        #The GRID geometry manager organizes widgets in a table-like structure in the parent widget.

top.mainloop()