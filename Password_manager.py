#! /usr/bin/env python3

from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont

import threading
import os 
import random 
import onetimepad
import json

# as requested in comment
 # use `json.loads` to do the reverse
# root setup
root = Tk()
root.title('Password manager')
root.geometry("225x175")
root.configure(bg='black')
fontStyle = tkFont.Font(family="times", size=10,)


stored_users = {'Christian': 'Thummel'}

# this is the main apllictation
def in_sys():
   
   button_check.destroy()
   button_set.destroy() 
   label.destroy()
   label_1.destroy()
   label_2.destroy()
   e.destroy()
   e2.destroy() 
   label3 = Label(root,  text ='Work in progress.', bg = 'black', fg= 'yellow', font=fontStyle )
   label3.pack() 

# this is what checks the password and  username  to see if it  is in the dic
def check():
   
    user = e.get()# Gets entry text.
    Password = e2.get()
    
    if stored_users.get(user) == Password:
        e.delete(0, END)
        e2.delete(0, END)
        label.config(text ='Singing in')
        timer = threading.Timer(1.0, in_sys) 
        timer.start() 
    else:
        e.delete(0, END)
        e2.delete(0, END)
        label.config(text ='\nWrong password or username')

# this function adds the user name and password to  the dictinary 
def ok():    
    user = e.get()# Gets entry text.
    Password = e2.get()
    if stored_users.get(user):
       label.config(text ='\n Username already exist')
    elif ' ' in user or ' ' in Password:
        label.config(text ='\n No spaces in your password\n or username')
        timer = threading.Timer(2.0, new_user) 
        timer.start() 
        button_ok.destroy()
        return
    elif Password == '' or user == '':
        label.config(text ='\n Please enter/n a password and username')
        timer = threading.Timer(2.0, new_user) 
        timer.start()
        button_ok.destroy()
        return
    elif len(Password) < 3:
        label.config(text ='\n Password needs to be at least 3 \n charecters long')
        timer = threading.Timer(2.0, new_user) 
        timer.start() 
        button_ok.destroy()
        return 
        
    else:
        stored_users[user] = Password
        label.config(text='Account Added ')
        timer = threading.Timer(1.0, Restart) 
        timer.start() 
 # this function adds new user       
def new_user():
    global button_ok
    
    e.delete(0, END)
    e2.delete(0, END)
    
    button_check.destroy()
    button_set.destroy() 
   
    label.config(text='Please create a user name and password.')
    button_ok = Button(root, text = 'OK', bg = 'blue', fg = 'yellow', padx=12, pady=2, font=fontStyle, command =lambda:ok()) 
    button_ok.pack()
  # this resets the sgin in process  
def Restart():
   button_ok.destroy()
   label.destroy()
   label_1.destroy()
   label_2.destroy()
   e.destroy()
   e2.destroy() 
   main() 
 # main sign in as function
def main():
    
    global label
    global label_1
    global label_2
    global e2
    global e
    global button_check
    global button_set
    
    
    label = Label(root,  text ='\nPlease Sing in.', bg = 'black', fg= 'yellow', font=fontStyle )
    label.pack()
    label_1 = Label(root,  text ='Username.', bg = 'black', fg= 'yellow', font=fontStyle )
    label_1.pack()

    e = Entry(root, width=25, borderwidth=2, bg = "gray")
    e.pack()

    label_2 = Label(root,  text =' Password.', bg = 'black', fg= 'yellow', font=fontStyle )
    label_2.pack()

    e2 = Entry(root, width=25, borderwidth=2, bg = "gray")
    e2.pack()

    button_set = Button(root, text = 'New user', bg = 'blue', fg = 'yellow', padx=12, pady=2, font=fontStyle, command =lambda: new_user)
    button_set.pack(side='right')
    button_check = Button(root, text = 'Continue', bg = 'yellow', fg= 'blue',font=fontStyle, command = check)
    button_check.pack(side = 'left')



label = Label(root,  text ='\nPlease Sing in.', bg = 'black', fg= 'yellow', font=fontStyle )
label.pack()
label_1 = Label(root,  text ='Username.', bg = 'black', fg= 'yellow', font=fontStyle )
label_1.pack()

e = Entry(root, width=25, borderwidth=2, bg = "gray")
e.pack()

label_2 = Label(root,  text =' Password.', bg = 'black', fg= 'yellow', font=fontStyle )
label_2.pack()

e2 = Entry(root, width=25, borderwidth=2, bg = "gray")
e2.pack()

button_set = Button(root, text = 'New user', bg = 'blue', fg = 'yellow', padx=12, pady=2, font=fontStyle, command = new_user)
button_set.pack(side='right')
button_check = Button(root, text = 'Continue', bg = 'yellow', fg= 'blue',font=fontStyle, command = check)
button_check.pack(side = 'left')

root.mainloop()