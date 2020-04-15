#! /usr/bin/env python3
''' 
This  is my take on a password signin 
I used  sqlight to store the password and username of people.
this program will store the infromation of your accounts in a sqlite db.
this program also fetures a random password genorator this genorator
only creates 4 charecters perclick. Expect this program to be updated by 
next mouth.

!!!functing not compleat!!! 

@author: Chris Thummel
'''
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont
from random import choice
import sqlite3
import threading
import string
import random


root = Tk()
root.title('Password manager')
root.geometry("300x250")
fontStyle = tkFont.Font(family="times", size=11,)


#creates a table for sqlight users
conn = sqlite3.connect('sqlight3_Signin.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users(
            user_name text, 
            password text)""")

conn.commit()


# pulls user name and password from DB
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
#___________________________________________________________________________________


# loads the account infromation in the form of tupels
def load():
    
    global print_record
    global button_Back
    global label
    
    button_Store.destroy()
    button_Gen.destroy()
    
    root.geometry("600x600")
    
    conn = sqlite3.connect('sqlight3_Storage.db')
    c = conn.cursor()
    query = 'SELECT * FROM {}'.format(name)
    c.execute(query)
    x = c.fetchall()
    
    print_record = ''
    for i in x:
            print_record += str(i) + "\n"
    
    button_Back = Button(root, text='Back', padx =200, pady =10, bg = 'floral white', fg = 'black',activebackground = "gray63",font=fontStyle,cursor = "pencil", command= destroy1)
    button_Back.pack()
            
    label = Label(root, text = print_record, font=fontStyle)
    label.pack()
    conn.commit()
    conn.close()
    return

    
# This function is what generates 4 random charecters for the Create_Password function 
def Generate ():
    def pw_gen(size = 12, chars=string.ascii_letters + string.digits + string.punctuation):

            return ''.join(random.choice(chars) for _ in range(size))
    password_A.insert(0,pw_gen(int(4)))
    

# this function saves the account infromation
def Save (): 
 # Use the name variabul as tabel name_____________________________
    def store (name):
          conn = sqlite3.connect('sqlight3_Storage.db')
          c = conn.cursor()
          c.execute('''INSERT INTO {tab} VALUES (:name_of_user, :website, :user_name, :email, :Password);'''.format(tab=name),

			{   'name_of_user': nameofuser.get(),

				'website': Website.get(),

				'user_name': user_name.get(),

				'email': email.get(),

				'Password': password_A.get(),})
          
    #commit changes
         
          conn.commit()
          conn.close()
#___________________________________ end of second function         
    store(name)
    destroy()


# This is where you store your infromation into the db  
def Create_Password ():
    global button_Back
    global nameofuser
    global Website
    global email
    global user_name
    global password_A
    global namel_new 
    global Websitel_new
    global emaill_new
    global user_namel_new
    global passwordl_new
    global button_generate
    global button_Save
    
    root.geometry("350x350")
    button_Store.destroy()
    button_Gen.destroy()
    
    root.geometry("350x350")
    
    nameofuser = Entry(root, width=30)
    nameofuser.grid(row = 0, column=1, padx=20, pady=(10, 0))
    Website = Entry(root, width=30)
    Website.grid(row = 1, column= 1, padx = 20)
    email= Entry(root, width=30)
    email.grid(row = 2, column=1, padx=20)
    user_name = Entry(root, width=30)
    user_name.grid(row = 3, column= 1, padx = 20)
    password_A = Entry(root, width=30)
    password_A.grid(row = 4, column= 1, padx = 20)

    namel_new = Label(root, text = 'Name')
    namel_new.grid(row = 0, column=0, padx=20, pady=(10, 0))
    Websitel_new = Label(root, text = 'Website')
    Websitel_new.grid(row = 1, column=0, padx=20)
    emaill_new = Label(root, text = 'Email')
    emaill_new.grid(row = 2, column=0, padx=20)
    user_namel_new = Label(root, text = 'Username')
    user_namel_new.grid(row = 3, column=0, padx=20)
    passwordl_new = Label(root, text = 'Password')
    passwordl_new.grid(row = 4, column=0, padx=20)
    
    button_generate = Button(root, text='Generate', padx =5, pady =10, bg = 'floral white', fg = 'black',activebackground = "gray63",font=fontStyle,cursor = "pencil", command= Generate)
    button_generate.grid( row=5, column = 0, columnspan = 2, ipadx=76, pady =(15,0), padx=42 )
    button_Save = Button(root, text='Save', padx =5, pady =10, bg = 'floral white', fg = 'black',activebackground = "gray63",font=fontStyle,cursor = "pencil", command= Save)
    button_Save.grid( row=6, column = 0, columnspan = 2, ipadx=90, pady =(15,0), padx=42 )
    button_Back = Button(root, text='Back', padx =5, pady =10, bg = 'floral white', fg = 'black',activebackground = "gray63",font=fontStyle,cursor = "pencil", command= destroy)
    button_Back.grid( row=7, column = 0, columnspan = 2, ipadx=90, pady =(15,0), padx=42 )


# Reset to main menu this function destroys the last screen
def destroy ():
   button_Back.destroy()
   user_name.destroy()
   Website.destroy()
   email.destroy()
   password_A.destroy()
   nameofuser.destroy()
   button_generate.destroy()
   namel_new.destroy()
   Websitel_new.destroy()
   emaill_new.destroy()
   user_namel_new.destroy()
   passwordl_new.destroy()
   button_Save.destroy()
   label.destroy()
   in_main()

def destroy1 ():
    label.destroy()
    button_Back.destroy()
    in_main()
    

# this is the main menu
def in_main():
   root.geometry("250x250")
   global button_Gen
   global button_Store

   button_check.destroy()
   button_set.destroy() 
   label.destroy()
   label_1.destroy()
   label_2.destroy()
   e.destroy()
   e2.destroy() 
   # these are the selection buttons 
   button_Gen = Button(root, text='Create Entry', padx =45, pady =10, bg = 'floral white', fg = 'black',activebackground = "gray63",font=fontStyle,cursor = "pencil", command= Create_Password) 
   button_Gen.grid( row=2, column=1, ipadx=40, pady = (60, 0), padx=5 )
   button_Store = Button(root, text='Your Accounts', padx =55, pady =10, bg = 'floral white', fg = 'black',activebackground = "gray63",font=fontStyle,cursor = "arrow", command= load )
   button_Store.grid( row=4, column = 1, ipadx=20, pady =(15,0), padx=5 )


# this function is what checks the password and username to see if it is in the dictinary
def check():
    global name
   
    user = e.get()# Gets entry text.
    Password = e2.get()
    # Password and User are correct
    if stored_users.get(user) == Password:
        
#___________# Use the name variabul as tabel name ___________________
        def create_table (name):
            # creates a tabel for user to store there accounts
            conn = sqlite3.connect('sqlight3_Storage.db')
    
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS {tab}
                        (
                         name_of_user    TEXT    NOT NULL,
                         website        TEXT     NOT NULL,
                         user_name      TEXT,
                         email          TEXT,
                         Password        TEXT);'''.format(tab=name))
           
            conn.commit()
            conn.close()
 #_____________________________________________________end of second function       
       
        name = e.get()# sql var
        create_table(name)
        
        
        e.delete(0, END)
        e2.delete(0, END)
        label.config(text ='Signing in...', font=fontStyle)
        timer = threading.Timer(1.0, in_main) 
        timer.start() 
        # wrong user or password
    else:
        e.delete(0, END)
        e2.delete(0, END)
        label.config(text ='\nWrong password or username.', font=fontStyle)
 # this function adds an user name and password to  the dictinary 
def ok():    
    user = e.get()# Gets entry text.
    Password = e2.get()
    if stored_users.get(user):
       label.config(text ='\n Username already exists.',font=fontStyle)
       #checks to see if there are anyspaces in the  password
    elif ' ' in user or ' ' in Password:
        label.config(text ='\nNo spaces in your password\n or username.',font=fontStyle)
        timer = threading.Timer(2.0, new_user) 
        timer.start() 
        button_ok.destroy()
        return
    # checks to see if there is nothing 
    elif Password == '' or user == '':
        label.config(text ='\n Please enter a password and username.',font=fontStyle)
        timer = threading.Timer(2.0, new_user) 
        timer.start()
        button_ok.destroy()
        return
    # checkes password length 
    elif len(Password) < 3:
        label.config(text ='\n Password needs to be at least 3 \n charecters long.',font=fontStyle)
        timer = threading.Timer(2.0, new_user) 
        timer.start() 
        button_ok.destroy()
        return 
        # stores password
    else:
        stored_users[user] = Password
        label.config(text='Account Added. ',font=fontStyle)
        timer = threading.Timer(1.5, Restart) 
        timer.start()
        # sql to store password
        conn = sqlite3.connect('sqlight3_Signin.db')
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (:USER, :PASSWORD)",{'USER': user, 'PASSWORD': Password})
        conn.commit()          
        conn.close()
 
    
 # this function adds new user whole point of this function is to go to def ok       
def new_user():
    global button_ok
    
    e.delete(0, END)
    e2.delete(0, END)
    
    button_check.destroy()
    button_set.destroy() 
   
    label.config(text='\nPlease create a username and password.',font=fontStyle)
    button_ok = Button(root, text = 'OK', bg = 'floral white', fg = 'black', padx=12, pady=2, activebackground = "gray63", font=fontStyle, command =lambda:ok()) 
    button_ok.pack()
    
    
  # this resets the signin process  
def Restart():
   button_ok.destroy()
   label.destroy()
   label_1.destroy()
   label_2.destroy()
   e.destroy()
   e2.destroy() 
   login() 
   
   
# login after you create an account
def login():
    
    global label
    global label_1
    global label_2
    global e2
    global e
    global button_check

    label = Label(root,  text ='\nPlease Sign in.', fg= 'black', font=fontStyle )
    label.pack()
    label_1 = Label(root,  text ='Username.',  fg= 'black', font=fontStyle )
    label_1.pack()

    e = Entry(root, width=25, borderwidth=2, bg = "floral white")
    e.pack()

    label_2 = Label(root,  text =' Password.', fg= 'floral white',padx = 20, font=fontStyle )
    label_2.pack()

    e2 = Entry(root, width=25, borderwidth=2, bg = "floral white", show = '*')
    e2.pack()

    button_check = Button(root, text = 'Login', bg = 'floral white', fg= 'black',activebackground = "gray63", padx=12, pady=2,font=fontStyle, command = check)
    button_check.pack()


# Starting screen
label = Label(root,  text ='\nPlease Sign in.', fg= 'black', font=fontStyle )
label.pack()
label_1 = Label(root,  text ='\nUsername.', fg= 'black', font=fontStyle )
label_1.pack()

e = Entry(root, width=25, borderwidth=2, bg = "floral white")
e.pack()

label_2 = Label(root,  text ='\n Password.', fg= 'black', font=fontStyle )
label_2.pack()

e2 = Entry(root, width=25, borderwidth=2, bg = "floral white", show = '*')
e2.pack()

button_set = Button(root, text = 'New user', bg = 'floral white', fg = 'black',activebackground = "gray63", padx=12, pady=4, font=fontStyle, command = new_user)
button_set.pack(side='right')
button_check = Button(root, text = 'Login', bg = 'floral white', activebackground = "gray63", fg= 'black',padx=18, pady=4,font=fontStyle, command = check)
button_check.pack(side = 'left')


root.mainloop()