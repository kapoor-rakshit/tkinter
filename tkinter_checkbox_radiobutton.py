from tkinter import *

top=Tk()
top.geometry("400x400")

def rst():
	chkbx1.set(0)
	chkbx2.set(0)
	rbvr1.set(0)
	rbvr2.set(0)

def chk():
	print("Your Interests are :")
	if chkbx1.get()==1:
		print("Data Strcut and Algo")
	if chkbx2.get()==1:
		print("Distributed Systems")
	print("\n")
	result="Gender is : "+rbvr1.get()+"\n"+"Grade is : "+str(rbvr2.get())
	print(result)

chkbx1=IntVar()
chkbx2=IntVar()
# if the variable changes for any reason, the widget it's connected to will be updated to reflect the new value. 
# These Tkinter control variables are used like regular Python variables to keep certain values.
# It's not possible to hand over a regular Python variable to a widget through a variable or textvariable option. 
# The only kinds of variables for which this works are variables that are subclassed from a class called Variable, defined in the Tkinter module

cbx1=Checkbutton(top,text="Data Structures and Algorithms",variable=chkbx1,onvalue=1,offvalue=0,command=chk).grid(row=1,sticky=E)
cbx2=Checkbutton(top,text="Distributed Systems",variable=chkbx2,onvalue=1,offvalue=0,command=chk,cursor="dot").grid(row=3,sticky=W)

# command - A procedure to be called every time the user changes the state of this checkbutton.
# cursor - (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.
# offvalue - control variable will be set to 0 when it is cleared (off). You can supply an alternate value for the off state by setting offvalue to that value.
# onvalue - control variable will be set to 1 when it is set (on). You can supply an alternate value for the on state by setting onvalue to that value.
# variable - The control variable that tracks the current state of the checkbutton. Normally this variable is an IntVar, and 0 means cleared and 1 means set.

qbt=Button(top,text="Quit",command=top.quit).grid(row=5,sticky=W)           # Quit Button
sbt=Button(top,text="SUBMIT",command=chk).grid(row=7,sticky=W)           # Check state of checkboxes
rbt=Button(top,text="Reset",command=rst).grid(row=9)
# the widgets are centered in their cells. 
# You can use the STICKY option to change this; this option takes one or more values from the set N, S, E, W.

rbvr1=StringVar()
rbvr2=IntVar()

rb11=Radiobutton(top,text="Male",variable=rbvr1,value="Male").grid(row=13)
rb12=Radiobutton(top,text="Female",variable=rbvr1,value="Female").grid(row=14)
rb13=Radiobutton(top,text="Other",variable=rbvr1,value="Other").grid(row=15)

rb21=Radiobutton(top,text="S",variable=rbvr2,value=10).grid(row=17)
rb22=Radiobutton(top,text="A",variable=rbvr2,value=9).grid(row=19)
rb23=Radiobutton(top,text="B",variable=rbvr2,value=8).grid(row=21)
rb24=Radiobutton(top,text="C",variable=rbvr2,value=7).grid(row=23)

# value - When a radiobutton is turned on by the user, its control variable is set to its current value option. 
#If the control variable is an IntVar, give each radiobutton in the group a different integer value option. 
#If the control variable is a StringVar, give each radiobutton a different string value option.

# variable - The control variable that this radiobutton shares with the other radiobuttons in the group. 
#This can be either an IntVar or a StringVar.

#cbx1.place(x=100,y=150)
#cbx2.place(x=200,y=250)
#cbx1.pack()
#cbx2.pack()

top.mainloop()
