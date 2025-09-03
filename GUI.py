from tkinter import*  #for GUI
from tkinter import messagebox  #for message box
from tkinter import filedialog  #for file dialog
from tkinter import colorchooser  #for color chooser
from tkinter import simpledialog  #for simple dialog
from tkinter import ttk  #for tree view
from tkinter import scrolledtext  #for scrolled text
from tkinter import Menu  #for menu
from tkinter import Canvas  #for canvas  
from tkinter import Frame  #for frame 
from tkinter import Label  #for label  
from tkinter import Entry  #for entry 
from tkinter import Button  #for button
from tkinter import Checkbutton  #for check button
from tkinter import Radiobutton  #for radio button
from tkinter import Scale  #for scale
from tkinter import Listbox  #for list box 
from tkinter import Spinbox  #for spin box 
window=Tk()  #for window 

#for title
window.title("My first GUI application") 
window.configure(background='red') 
window.geometry('400x200') 

# window.resizable(False,False) 
# window.iconbitmap('logo.ico') 
#For text on the window
Label(window, text="Hello welcome to my page" , 
      fg='yellow',
      bg='dark green', 
      font='Halvetica 16 bold').pack() 
Label(window, text="This is GUI made by me",
      fg='yellow', 
      bg='dark green',
      font='Halvetica 16 bold').pack() 
#For image on the window  
img=PhotoImage(file='giyuu-tomioka-klinok-rassekaiushchii-demonov-dozhd-paren-pti.webp')
Label(window, image=img).pack()  
Label(window, text='Image label').pack() 
#For taking username 
window.geometry('300x100')  
Label(text="Enter usename").pack()
e=Entry(window).pack()


#For making a buttons
Button(text='Enter', bg='green', height='2',width='5').pack()
Checkbutton(text='General knowledge').pack()
Checkbutton(text='Maths').pack()
Radiobutton(text='male' , value='male').pack()
Radiobutton(text='female' , value='female').pack()
window.mainloop() 