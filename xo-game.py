from tkinter import *
from turtle import width

wind = Tk()
wind.geometry("325x300")

B1Top=Button(text='',width='10',height="5").grid(column=1,row=1)
B2Top=Button(text='',width='10',height="5").grid(column=2,row=1)
B3Top=Button(text='',width='10',height="5").grid(column=3,row=1)

B1Center=Button(text='',width='10',height="5").grid(column=1,row=2)
B2Center=Button(text='',width='10',height="5").grid(column=2,row=2)
B3Center=Button(text='',width='10',height="5").grid(column=3,row=2)

B1Bottom=Button(text='',width='10',height="5").grid(column=1,row=3)
B2Bottom=Button(text='',width='10',height="5").grid(column=2,row=3)
B3Bottom=Button(text='',width='10',height="5").grid(column=3,row=3)

wind.mainloop()