from tkinter import *

top=Tk()
top.geometry("400x400")

def chk():
	print(spinval.get())
	print(spin2val.get())
	print(Lb1.curselection())
	if mayoVar.get()==1:
		print("mayo selected")
	if ketchVar.get()==1:
		print("ketchup selected")

spinval=StringVar()
spin2val=StringVar()

yr=Spinbox(top,from_=1,to=10,increment=2,textvariable=spinval,state=DISABLED).pack()
w = Spinbox(values=("sdkjf","vvnd","vnd","vdv"),textvariable=spin2val,state="readonly").pack()

# from_
# to
# increment
# textvariable
# state
# values
scrollbar = Scrollbar(top,orient=VERTICAL,width=20)
scrollbar.pack(side=RIGHT)

Lb1 = Listbox(top,height=3,width=30,selectmode=MULTIPLE,yscrollcommand = scrollbar.set)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.insert(END,"C#")
Lb1.pack(side=LEFT)
scrollbar.config(command = Lb1.yview)

# selectmode - Determines how many items can be selected, and how mouse drags affect the selection −
#BROWSE − (default) you can only select one line out of a listbox. If you click on an item and then drag to a different line, the selection will follow the mouse.
#SINGLE − You can only select one line, and you can't drag the mouse.
#MULTIPLE − You can select any number of lines at once.
#EXTENDED − You can select any adjacent group of lines at once by clicking on the first line and dragging to the last line.

# height - Number of lines (not pixels!) shown in the listbox. Default is 10.
# width - The width of the widget in characters. The default is 20.

# curselection() - Returns a tuple containing the line numbers of the selected element or elements, 
#counting from 0. If nothing is selected, returns an empty tuple.

# insert ( index, *elements ) - Insert one or more new lines into the listbox before the line specified by index. 
#Use END as the first argument if you want to add new lines to the end of the listbox.

# set() - To connect a scrollbar to another widget w, set w's xscrollcommand or yscrollcommand to the scrollbar's set() method. 
#The arguments have the same meaning as the values returned by the get() method.

# orient - Set orient = HORIZONTAL for a horizontal scrollbar, orient = VERTICAL for a vertical one.

mb=Menubutton( top, text = "condiments",relief=RAISED,direction=LEFT)
mb.pack()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label = "mayo",variable = mayoVar )
mb.menu.add_checkbutton ( label = "ketchup",variable = ketchVar )
mb.pack()

# menu - To associate the menubutton with a set of choices, set this option to the Menu object containing those choices. 
#That menu object must have been created by passing the associated menubutton to the constructor as its first argument.

# tearoff - Normally, a menu can be torn off, the first position (position 0) in the list of choices is occupied by the tear-off element, 
#and the additional choices are added starting at position 1. 
#If you set tearoff = 0, the menu will not have a tear-off feature, and choices will be added starting at position 0.

# direction - Set direction = LEFT to display the menu to the left of the button; 
#use direction = RIGHT to display the menu to the right of the button; 
#or use direction = 'above' to place the menu above the button.

#add_radiobutton( options ) - Creates a radio button menu item. and similarly many more....

bt=Button(top,text="SUBMIT",command=chk).pack()

top.mainloop()
