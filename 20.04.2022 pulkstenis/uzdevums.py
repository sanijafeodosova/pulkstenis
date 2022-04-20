# Python strftime()
from tkinter import *
from datetime import datetime
from time import strftime
from turtle import bgcolor


plkst=Tk()
plkst.title("Pulkstenis")
plkst.geometry('750x150')

def time():
    paka=strftime("%H:%M:%S %p")
    vieta.config(text=paka)
    vieta.after(1000,time)
    return 0
vieta=Label(plkst,font="ds-digital 100", bg="gray", fg="white")
vieta.pack(anchor ="sw")
time()





plkst.mainloop() 