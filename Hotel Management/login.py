from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import HotelManagementSystem

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\login.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\log.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lb1=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lb1=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=255)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        #=================Icon Images============
        img2 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\user.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=610, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\password.jpg")
        img3 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=610, y=395, width=25, height=25)

        # log in button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        # register button
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=120)

        #forgetpassbtn
        registerbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=10, y=370, width=160)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("success","Welcome to Hotel")
        else:
            conn=mysql.connector.connect()
            messagebox.showerror("Invaild","Invalid user name and password")

if __name__=="main":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()