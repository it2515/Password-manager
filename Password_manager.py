#! /usr/bin/env python3
''' 
This  is my take on a password signin 
I used  sqlight to store the password and username of people.
This is the  very start of my password manager project 
@author: Chris Thummel
# edits to make put back button.    


'''
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont
import sqlite3
import threading



root = Tk()
root.title('Password manager')
root.geometry("300x250")
fontStyle = tkFont.Font(family="times", size=12,)


#creates a table for sqlight this is commented out   
'''
conn = sqlite3.connect('sqlight3_Signin.db')
c = conn.cursor()

c.execute("""CREATE TABLE users(
            user_name text, 
            password text)""")

conn.commit()
'''

# pulls username and password from DB
conn = sqlite3.connect('sqlight3_Signin.db')
c = conn.cursor()
c.execute("SELECT * FROM users")
x = c.fetchall()
conn.commit()
conn.close()


# converts stored tupels into a dictinary
def Convert(tup, di): 
    di = dict(tup) 
    return di 

# singin dictinary
j = {} 

# assigns dictinary to stored users
stored_users = (Convert(x, j)) 

# this is the main apllictation 
def in_sys():
   
   button_check.destroy()
   button_set.destroy() 
   label.destroy()
   label_1.destroy()
   label_2.destroy()
   e.destroy()
   e2.destroy() 
   label3 = Label(root,  text ='Work in progress.', fg= 'black', font=fontStyle )
   label3.pack() 

# this function is what checks the password and username to see if it is in the dictionary
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

# this function adds an username and password to the dictionary
def ok():    
    user = e.get()# Gets entry text.
    Password = e2.get()
    if stored_users.get(user):
       label.config(text ='\n Username already exist',font=fontStyle)
       #checks to see if there are any spaces in the password or username 
    elif ' ' in user or ' ' in Password:
        label.config(text ='\n No spaces in your password\n or username',font=fontStyle)
        timer = threading.Timer(2.0, new_user) 
        timer.start() 
        button_ok.destroy()
        return
    # checks to see if there is nothing in username and password 
    elif Password == '' or user == '':
        label.config(text ='\n Please enter/n a password and username',font=fontStyle)
        timer = threading.Timer(2.0, new_user) 
        timer.start()
        button_ok.destroy()
        return
    # checkes password length 
    elif len(Password) < 3:
        label.config(text ='\n Password needs to be at least 3 \n charecters long',font=fontStyle)
        timer = threading.Timer(2.0, new_user) 
        timer.start() 
        button_ok.destroy()
        return 
        # stores password
    else:
        stored_users[user] = Password
        label.config(text='Account Added ',font=fontStyle)
        timer = threading.Timer(1.0, Restart) 
        timer.start()
        
# sqlight to store password
        conn = sqlite3.connect('sqlight3_Signin.db')
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (:USER, :PASSWORD)",{'USER': user, 'PASSWORD': Password})
        conn.commit()          
        conn.close()
            
            
 # this function gos to newuser screen     
def new_user():
    global button_ok
    
    e.delete(0, END)
    e2.delete(0, END)
    
    button_check.destroy()
    button_set.destroy() 
   
    label.config(text='Please create a username and password.',font=fontStyle)
    button_ok = Button(root, text = 'OK', bg = 'floral white', fg = 'black', padx=12, pady=2, font=fontStyle, command =lambda:ok()) 
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
   
   
# will be updated next week
def main():
    
    global label
    global label_1
    global label_2
    global e2
    global e
    global button_check
    global button_set
    
    
    label = Label(root,  text ='\nPlease Sing in.', fg= 'black', font=fontStyle )
    label.pack()
    label_1 = Label(root,  text ='Username.',  fg= 'black', font=fontStyle )
    label_1.pack()

    e = Entry(root, width=25, borderwidth=2, bg = "floral white")
    e.pack()

    label_2 = Label(root,  text =' Password.', fg= 'floral white', font=fontStyle )
    label_2.pack()

    e2 = Entry(root, width=25, borderwidth=2, bg = "floral white")
    e2.pack()

    
    button_check = Button(root, text = 'Login', bg = 'floral white', fg= 'black', padx=12, pady=2,font=fontStyle, command = check)
    button_check.pack()



label = Label(root,  text ='\nPlease Sing in.', fg= 'black', font=fontStyle )
label.pack()
label_1 = Label(root,  text ='Username.', fg= 'black', font=fontStyle )
label_1.pack()

e = Entry(root, width=25, borderwidth=2, bg = "floral white")
e.pack()

label_2 = Label(root,  text =' Password.', fg= 'black', font=fontStyle )
label_2.pack()

e2 = Entry(root, width=25, borderwidth=2, bg = "floral white")
e2.pack()

button_set = Button(root, text = 'New user', bg = 'floral white', fg = 'black', padx=12, pady=4, font=fontStyle, command = new_user)
button_set.pack(side='right')
button_check = Button(root, text = 'Login', bg = 'floral white', fg= 'black',padx=12, pady=4,font=fontStyle, command = check)
button_check.pack(side = 'left')

root.mainloop()
