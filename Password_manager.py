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
root.iconbitmap(r'lock.ico')
root.geometry("300x350")
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


# deletes sql entry
# need to add message box in next update.
def delete ():
    conn = sqlite3.connect('sqlight3_Storage.db')
    c = conn.cursor()
    
    c.execute(f"DELETE from {name} WHERE oid=" + id_box.get())

    conn.commit()
    conn.close()
    Destroy1()


# saves updated entry 
def save (id):
           print(id)
           print(str(nameofuser.get()))
           conn = sqlite3.connect('sqlight3_Storage.db')#create curser
           c = conn.cursor()
           record_id = id
           sqlupdate = c.execute(f"""UPDATE {name} SET 
                name_of_user = :name,
                Website = :website,
                email = :email,
                user_name = :user_name,
                Password = :Password
             
                
                WHERE oid = :oid""",
                {'name': nameofuser.get(),
                 'website': Website.get(),
                 'email': email.get(),
                 'user_name': user_name.get(),
                 'Password': password_A.get(),
                 'oid': record_id }
                )
          
           conn.commit()
           conn.close()
           root1.destroy()   


# this large function allows you to select an id and update or delete it...
def SELECT():
  
  global id_box
  global id_box_label
  global lable
  global button_update
  global Button_Back
  global button_delete

  root.geometry("350x450")
  button_view.destroy()
  button_store.destroy()
  button_edit.destroy()
# this is to pull out the information on the delete box this is how i deied to do it 
  def get():
    JC = id_box.get()
    update(JC)
# this function takes the id number and displays that entry on your new screen for you to edit.
# you may have to reopen the program to see the changes 
# foe some reson I had to put ths function into the select function.
  def update (id):

      def edit():
        GET = id_box.get()
        save(GET)
      
      global nameofuser
      global Website
      global email
      global user_name
      global password_A

# new window 
      root1 = Tk()
      root1.title('Update')
      root1.geometry("350x300")
      root1.configure()  

      nameofuser = Entry(root1, width=30)
      nameofuser.grid(row = 1, column=1, padx=20, pady=(10, 0))
      Website = Entry(root1, width=30)
      Website.grid(row = 2, column= 1, padx = 20)
      email= Entry(root1, width=30)
      email.grid(row = 3, column=1, padx=20)
      user_name = Entry(root1, width=30)
      user_name.grid(row =4 , column= 1, padx = 20)
      password_A = Entry(root1, width=30)
      password_A.grid(row = 5, column= 1, padx = 20)
     
      namel_new = Label(root1, text = 'Name:')
      namel_new.grid(row = 1, column=0, padx=20, pady=(10, 0))
      Websitel_new = Label(root1, text = 'Website:')
      Websitel_new.grid(row =2 , column=0, padx=20)
      emaill_new = Label(root1, text = 'Email:')
      emaill_new.grid(row =3, column=0, padx=20)
      user_namel_new = Label(root1, text = 'Username:')
      user_namel_new.grid(row =4 , column=0, padx=20)
      passwordl_new = Label(root1, text = 'Password:')
      passwordl_new.grid(row = 5, column=0, padx=20)
     
      upd= Button(root1, text= 'Save Record', command= edit)
      upd.grid(row = 6, column= 0, columnspan= 2, pady= 10, padx=10, ipadx=140)

      # connects to database
      conn = sqlite3.connect('sqlight3_Storage.db')
      c = conn.cursor()
      c.execute(f"SELECT * FROM {name} WHERE oid = " + id)
      
      # inserts entry into the new window
      RECORD = c.fetchall()
      for records in RECORD:
         nameofuser.insert(0, records[0])
         Website.insert(0, records[1])
         email.insert(0, records[2])
         user_name.insert(0, records[3])
         password_A.insert(0, records[4])

         conn.commit()
         conn.close()
      
      
# pulls all entrys with there id number for editing
  conn = sqlite3.connect('sqlight3_Storage.db')
  c = conn.cursor()
  Je = 'SELECT *, oid FROM {}'.format(name)
  c.execute(Je)
  x = c.fetchall()
  print(x)
    
  Print_record = ''
  for y in x:
          Print_record += str(y) + "\n"
  # window display       
  lable = Label(root, text = Print_record)
  lable.grid(row = 6, column=1, padx=20)
  conn.commit()

  id_box = Entry(root, width=30)
  id_box.grid(row =2, column = 1)  
  id_box_label = Label(root, text='SELECT ID')
  id_box_label.grid(row=2, column= 0) 

  button_update = Button(root, text='Update', padx =5, pady =10, bg = 'floral white', fg = 'black',
      activebackground = "gray63",font=fontStyle, command= get)
  button_update.grid( row=3, column = 0, columnspan = 2, ipadx=78, pady =(15,0), padx=42 )
  button_delete = Button(root, text='Delete', padx =5, pady =10, bg = 'floral white', fg = 'black',
      activebackground = "gray63",font=fontStyle, command= delete) # meaningless value tricks function to run
  button_delete.grid( row=4, column = 0, columnspan = 2, ipadx=80, pady =(15,0), padx=42 )
  Button_Back = Button(root, text='Back', padx =5, pady =10, bg = 'floral white', fg = 'black',
      activebackground = "gray63",font=fontStyle, command= Destroy1)
  Button_Back.grid( row=5, column = 0, columnspan = 2, ipadx=85, pady =(15,0), padx=42 )


# displays all the entrys
def display ():
    
    global print_record
    global button_Back
    global label
    global my_lable
    
    button_store.destroy()
    button_view.destroy()
    button_edit.destroy()

    root.geometry("600x600")
    
    conn = sqlite3.connect('sqlight3_Storage.db')
    c = conn.cursor()
    query = 'SELECT * FROM {}'.format(name)
    c.execute(query)
    x = c.fetchall()
    
    print_record = ''
    for i in x:
            print_record += str(i) + "\n"

    
    button_Back = Button(root, text='Back', padx =200, pady =10, bg = 'floral white', fg = 'black',
      activebackground = "gray63",font=fontStyle, command= Destroy)
    button_Back.grid(row = 2, column = 0,columnspan =2)
            
    label = Label(root, text = print_record, font=fontStyle)
    label.grid(row = 3, column = 0, columnspan = 2)
    conn.commit()
    conn.close()
    return

    
# This function is what generates 4 random charecters for the Create_Password function 
def Generate ():
    def pw_gen(size = 12, chars=string.ascii_letters + string.digits + string.punctuation):

            return ''.join(random.choice(chars) for _ in range(size))
    password_A.insert(0,pw_gen(int(4)))
    

# this function saves the account infromation
def Save (self): 
 # Use the name variabul as tabel name
    def store (name):
          conn = sqlite3.connect('sqlight3_Storage.db')
          c = conn.cursor()
          c.execute('''INSERT INTO {tab} VALUES (:name_of_user, :website, :user_name, :email, :Password);'''.format(tab=name),

			{'name_of_user': nameofuser.get(),

				'website': Website.get(),
        
        			'email': email.get(),

        			'user_name': user_name.get(),

				'Password': password_A.get(),})
          
    #commit changes
         
          conn.commit()
          conn.close()

    store(name)
    destroy()


# This is where you store your infromation into the db  
def Create_Entry ():
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
    
    root.geometry("350x450")
    button_store.destroy()
    button_view.destroy()
    button_edit.destroy()
    
    nameofuser = Entry(root, width=30)
    nameofuser.grid(row = 1, column=1, padx=20, pady=(10, 0))
    Website = Entry(root, width=30)
    Website.grid(row = 2, column= 1, padx = 20)
    email= Entry(root, width=30)
    email.grid(row = 3, column=1, padx=20)
    user_name = Entry(root, width=30)
    user_name.grid(row =4 , column= 1, padx = 20)
    password_A = Entry(root, width=30)
    password_A.bind('<Return>', Save)
    password_A.grid(row = 5, column= 1, padx = 20)

    namel_new = Label(root, text = 'Name:')
    namel_new.grid(row = 1, column=0, padx=20, pady=(10, 0))
    Websitel_new = Label(root, text = 'Website:')
    Websitel_new.grid(row =2 , column=0, padx=20)
    emaill_new = Label(root, text = 'Email:')
    emaill_new.grid(row =3, column=0, padx=20)
    user_namel_new = Label(root, text = 'Username:')
    user_namel_new.grid(row =4 , column=0, padx=20)
    passwordl_new = Label(root, text = 'Password:')
    passwordl_new.grid(row = 5, column=0, padx=20)
    
    button_generate = Button(root, text='Generate', padx =5, pady =10, bg = 'floral white', fg = 'black',
      activebackground = "gray63",font=fontStyle, command= Generate)
    button_generate.grid( row=6, column = 0, columnspan = 2, ipadx=76, pady =(15,0), padx=42 )
    button_Save = Button(root, text='Save', padx =5, pady =10, bg = 'floral white', fg = 'black',
      activebackground = "gray63",font=fontStyle, command= lambda:Save('N/A')) # meaningless value tricks function to run
    button_Save.grid( row=7, column = 0, columnspan = 2, ipadx=90, pady =(15,0), padx=42 )
    button_Back = Button(root, text='Back', padx =5, pady =10, bg = 'floral white', fg = 'black',
      activebackground = "gray63",font=fontStyle, command= destroy)
    button_Back.grid( row=8, column = 0, columnspan = 2, ipadx=90, pady =(15,0), padx=42 )


# Reset to main menu these functions destroys the last screen
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
   my_label.destroy()
   in_menu()


def Destroy ():
    my_lable.destroy()
    label.destroy()
    button_Back.destroy()
    in_menu()


def Destroy1 ():
   
   button_update.destroy()
   button_delete.destroy()
   Button_Back.destroy()
   lable.destroy()
   id_box.destroy()
   id_box_label.destroy()
   in_menu()
  

# this is the main menu
def in_menu():
   root.geometry("263x400")

   global button_store
   global button_view
   global my_label
   global button_edit

   my_lable.destroy()
   button_check.destroy()
   button_set.destroy() 
   label.destroy()
   label_1.destroy()
   label_2.destroy()
   e.destroy()
   e2.destroy() 
   # these are the selection buttons 
   my_label = Label(image=my_img)
   my_label.grid(row = 0 , column = 0, columnspan = 2)

   button_store = Button(root, text='Create Entry', padx =45, pady =10, bg = 'floral white', fg = 'black',
    activebackground = "gray63",font=fontStyle,cursor = "arrow", command= Create_Entry) 
   button_store.grid( row=1, column=0, ipadx=38, pady = (60, 0), padx=5 )
   button_view = Button(root, text='Your Accounts', padx =55, pady =10, bg = 'floral white', fg = 'black',
    activebackground = "gray63",font=fontStyle,cursor = "arrow", command= display)
   button_view.grid( row=3, column = 0, ipadx=20, pady =(15,0), padx=5 )
   button_edit = Button(root, text='Update', padx =55, pady =10, bg = 'floral white', fg = 'black',
    activebackground = "gray63",font=fontStyle,cursor = "arrow", command= SELECT)
   button_edit.grid( row=4, column = 0, ipadx=43, pady =(15,0), padx=5 )

# this function is what checks the password and username to see if it is in the dictinary
def check(self):
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
                         email          TEXT,
                         user_name      TEXT,
                         Password        TEXT);'''.format(tab=name))
           
            conn.commit()
            conn.close()
 #_____________________________________________________end of second function       
       
        name = e.get()# sql var
        create_table(name)
        
        
        e.delete(0, END)
        e2.delete(0, END)
        label.config(text ='Signing in...', font=fontStyle)
        timer = threading.Timer(1.0, in_menu) 
        timer.start() 
        # wrong user or password
    else:
        e.delete(0, END)
        e2.delete(0, END)
        label.config(text ='\nWrong password or username.', font=fontStyle)
 

 # this function adds an user name and password to  the dictinary 
def ok(self):    
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
    e2.bind('<Return>', Clear)
    
    button_check.destroy()
    button_set.destroy() 
   
    label.config(text='\nPlease create a username and password.',font=fontStyle)
    button_ok = Button(root, text = 'OK', bg = 'floral white', fg = 'black', padx=12, pady=2, 
      activebackground = "gray63", font=fontStyle, command =lambda:ok('N/A'))  # meaningless value tricks function to run
    button_ok.pack()
    
    
  # this resets the signin process  
def Clear(self):
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
    e2.bind('<Return>', check)
    e2.pack()

    button_check = Button(root, text = 'Login', bg = 'floral white', fg= 'black',
      activebackground = "gray63", padx=12, pady=2,font=fontStyle, command = lambda:check('N/A')) # meaningless value tricks function to run
    button_check.pack()


# Starting screen

my_img = ImageTk.PhotoImage(Image.open(r'3-512.png'))
my_lable = Label(image=my_img)
my_lable.pack()
label = Label(root,  text ='\nPlease Sign in.', fg= 'black', font=fontStyle )
label.pack()
label_1 = Label(root,  text ='\nUsername:', fg= 'black', font=fontStyle )
label_1.pack()

e = Entry(root, width=25, borderwidth=2, bg = "floral white")
e.pack()

label_2 = Label(root,  text ='\n Password:', fg= 'black', font=fontStyle )
label_2.pack()

e2 = Entry(root, width=25, borderwidth=2, bg = "floral white", show = '*')
e2.bind('<Return>', check)
e2.pack()

button_set = Button(root, text = 'New user', bg = 'floral white', fg = 'black',
  activebackground = "gray63", padx=12, pady=4, font=fontStyle, command = new_user)
button_set.pack(side='right')
button_check = Button(root, text = 'Login', bg = 'floral white', 
  activebackground = "gray63", fg= 'black',padx=18, pady=4,font=fontStyle, command = lambda:check('N/A'))# meaningless value tricks function to run
button_check.pack(side = 'left')


root.mainloop()
