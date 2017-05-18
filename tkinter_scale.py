from tkinter import *

top=Tk()
top.geometry("100x100")

def chk():
	select = "Value = " + str(scvar.get())
	label.config(text=select)

def stk():
	scvar.set(35.56)

scvar=DoubleVar()

scale = Scale(top, variable = scvar , from_=20.0,to=63.5,tickinterval=0.5,resolution=0.85,sliderlength=50,length=200,
	showvalue=1,troughcolor="red")
scale.pack(anchor = CENTER)

# from_
# to
# resolution (same as increment)
# length - The length of the scale widget. This is x dimension if the scale is horizontal,or y dimension if vertical.
# sliderlength - length of slider on scale.
# showvalue - Normally, the current value of the scale is displayed in text form by the slider.Set this option to 0 to suppress that label.
# tickinterval - To display periodic scale values as labels on side of scale.
# troughcolor - Bgcolor of scale 

button = Button(top, text = "Get Value", command = chk)
button.pack(anchor = CENTER)

button = Button(top, text = "Set Value", command = stk)
button.pack(anchor = CENTER)

button=Button(top,text="Quit",command=top.quit)
button.pack(anchor=CENTER)

label = Label(top)
label.pack()

top.mainloop()
