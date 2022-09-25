import tkinter as t
from tkinter import messagebox
import quiz_module

#This is the funaction which is caled when user start the quiz when reaching through the signup menu
def mcqs_up():

    r.iconify()
    u.iconify()
    quiz_module.whole()
    m.iconify()
    
#This is the function which is called when user start the quiz by reaching through the signin menu directly
def mcqs_in():
    m.iconify()
    r.iconify()
    u.iconify()
    quiz_module.whole()

#Main window in which the user regiester him by filling the credentials   
def signup_win():
    global root
    global username
    global cms_id
    global password
    global gender
    m.destroy()
    root = t.Tk()
    root.geometry("1500x1000")
    root.title("SIGN UP")


    label_0 = t.Label(root, text = "SIGN UP",width = 20,fg = "cyan4",font = ("bold",20)).place(x=500,y=53)

    label_1 = t.Label(root, text = "USER NAME",width = 20,font = ("bold",10)).place(x=480,y=130)
    username = t.Entry(root)
    username.place(x=710,y=130)
   

    label_2 = t.Label(root, text = "CMS ID",width = 20,font = ("bold",10)).place(x=480,y=200)
    cms_id = t.Entry(root)
    cms_id.place(x=710,y=200)

    label_3 = t.Label(root, text = "PASSWORD",width = 20,font = ("bold",10)).place(x=480,y=280)
    password = t.Entry(root, show = '*')
    password.place(x=710,y=280)

    label_4 = t.Label(root, text = "GENDER",width = 20,font = ("bold",10)).place(x=480,y=350)
    gender = t.Entry(root)
    gender.place(x=710,y=350)
   
    button = t.Button(root, text = "Submit",width = 20,bg = "cyan4",fg = "white",command = signup_file).place(x=600,y=420)

#Function which put some validation checks on the signup menu   
def signup_file():
    with open("user.txt","r") as f:
       
        if username.get()=='' or cms_id.get()=='' or password.get()=='' or gender.get()=='':
            messagebox.showerror("Error","Fill all the entries")
            return None
        elif len(cms_id.get()) != 6:
            messagebox.showerror("Error","CMS ID must contain 6 digits")
            return None
        elif not (cms_id.get()).isdigit():
            messagebox.showerror("Error","CMS ID only contain digits")
            return None
        elif cms_id.get() in f.read():
            messagebox.showerror("Error","CMS ID already exists")
            return None
        elif len(password.get())<8:
             messagebox.showerror("Error","Password must contain atleast 8 characters")
             return None
        elif gender.get()!="male" and gender.get()!="female":
            messagebox.showerror("Error","Enter either male or female")
            return None
        else:    
            with open ("user.txt","a") as f:
                f.write(username.get()+'\t')
                value=cms_id.get()
                f.write(value+'\t')
                value1=password.get()
                f.write(value1+'\t')
                f.write(gender.get()+'\t')
                f.write('\n')
                root.destroy()
                signin_win_up()

#Sigin window is displayed when user submits the button on signup menu and after clicking the submit button on this window then after matching the information entered by the user the display_menu is shown
def signin_win_up():
    global r
    global cms_id
    global password
    r = t.Tk()
    r.geometry("1500x1000")
    r.title("SIGN IN")


    label_0 = t.Label(r, text="SIGN IN",width=20,fg="cyan4",font=("bold",20)).place(x=500,y=53)

    label_1 = t.Label(r, text="CMS ID",width=20,font=("bold",10)).place(x=480,y=130)

    cms_id = t.Entry(r)
    cms_id.place(x=710,y=130)

    label_2 =t.Label(r, text="PASSWORD",width=20,font=("bold",10)).place(x=480,y=200)

    password = t.Entry(r,show="*")
    password.place(x=710,y=200)

    t.Button(r, text="Submit",width=20,bg="cyan4",fg="white",command=signin_file_up).place(x=600,y=260)

               
def signin_win_in():
    global r
    global cms_id
    global password
    r = t.Tk()
    r.geometry("1500x1000")
    r.title("SIGN IN")


    label_0 = t.Label(r, text="SIGN IN",width=20,fg="cyan4",font=("bold",20)).place(x=500,y=53)

    label_1 = t.Label(r, text="CMS ID",width=20,font=("bold",10)).place(x=480,y=130)

    cms_id = t.Entry(r)
    cms_id.place(x=710,y=130)

    label_2 = t.Label(r, text="PASSWORD",width=20,font=("bold",10)).place(x=480,y=200)

    password = t.Entry(r,show="*")
    password.place(x=710,y=200)

    t.Button(r, text="Submit",width=20,bg="cyan4",fg="white",command=signin_file_in).place(x=600,y=260)              

#This is the function which checks 
def signin_file_in():
    value=cms_id.get()
    with open("user.txt","r") as my_file:
        info=my_file.read()
        x=info.find(value)
        word=info[x:x+6]
        if word == value :
            value1 = password.get()
            y = len(value1)
            x = info.find(value1)
            word1 = info[x:x+y]
            if word1 == value1 :
                display_menu_in()
            else:
                messagebox.showerror("Error","Enter correct Password")
        else:
            messagebox.showerror("Error","Enter correct CMS ID")

#This is the sigin window where the user enters his cms_id and password which is checked against the data stored in the file
def signin_file_up():
    value = cms_id.get()
    with open("user.txt","r") as my_file:
        info = my_file.read()
        x = info.find(value)
        word = info[x:x+6]
        if word == value :
            value1 = password.get()
            y = len(value1)
            x=info.find(value1)
            word1 = info[x:x+y]
            if word1 == value1 :
                display_menu_up()
            else:
                messagebox.showerror("Error","Enter correct Password")
        else:
            messagebox.showerror("Error","Enter correct CMS ID")

def exit():
    u.destroy()
    r.destroy()
    m.destroy()
               
# This is display_menu when users reaches through the signup menu   
def display_menu_up():
    global u
    u = t.Toplevel()
    u.geometry("1500x1000")
    u.title("MENU")
    u.configure(background="white")
    canvas=t.Canvas(u,width=1500,height=1000,background="white")
    canvas.pack()
    photo=t.PhotoImage(file="quiz2.png")
    canvas.image=photo
    canvas.create_image(670,370,image=photo)

    button1=t.Button(u,text="START QUIZ",background="cyan4",fg="white",font="none 12 bold ",width=15,height=2,command= mcqs_up)
    button1.place(x=900,y=200)

    button3=t.Button(u,text="EXIT",background="cyan4",fg="white",font="none 12 bold ",width=15,height=2,command=exit)
    button3.place(x=900,y=300)

#This is the display menu when user reaches directly through the signin menu
def display_menu_in():
    global u
    u=t.Toplevel()
    u.geometry("1500x1000")
    u.title("MENU")
    u.configure(background="white")
    canvas=t.Canvas(u,width=1500,height=1000,background="white")
    canvas.pack()
    photo=t.PhotoImage(file="quiz2.png")
    canvas.image=photo
    canvas.create_image(670,370,image=photo)

    button1=t.Button(u,text="START QUIZ",background="cyan4",fg="white",font="none 12 bold ",width=15,height=2,command= mcqs_in)
    button1.place(x=900,y=200)

    button3=t.Button(u,text="EXIT",background="cyan4",fg="white",font="none 12 bold ",width=15,height=2,command=exit)
    button3.place(x=900,y=300)

#Main window where the signup and signin button are displayed    
global m
m = t.Tk()
m.geometry("1500x1000")
m.configure(background="white")
canvas=t.Canvas(m,width = 1500,height = 1000,background = "black")
canvas.pack()
photo = t.PhotoImage(file ="quiz2.png")
canvas.image=photo
canvas.create_image(670,370,image=photo)



button1 = t.Button(m,text="SIGN UP",background = "cyan4",font = "none 12 bold ",fg = "white",width = 17,height = 3,command = signup_win)
button1.place(x=900,y=225)
button2 = t.Button(m,text="SIGN IN",background = "cyan4",font = "none 12 bold ",fg= "white",width = 17,height = 3,command = signin_win_in)
button2.place(x=900,y=385)
m.mainloop()
