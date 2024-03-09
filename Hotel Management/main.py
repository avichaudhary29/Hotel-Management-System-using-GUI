from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1910x1000+0+0")
# ======== 1st image==========
        img1=Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\hotel.jpg")
        img1=img1.resize((1910,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1910,height=140)

# ========logo========
        img2=Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\logo.jpg")
        img2=img2.resize((210,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=200,height=140)
 #-------title----
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1910,height=50)

#=====main frame====
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1910,height=790)
#========menu==========
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=240)
#=====button frame====
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=43,width=235,height=250)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=19,font=("times new roman",16,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=19, font=("times new roman", 16, "bold"), bg="black",fg="white", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS",width=19,command=self.details_room, font=("times new roman", 16, "bold"), bg="black",fg="white", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=19, font=("times new roman", 16, "bold"), bg="black",fg="white", bd=0, cursor="hand1")
        logout_btn.grid(row=3, column=0, pady=1)

 #==============right side image===========
        img3 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\hotel lobbey.jpg")
        img3 = img3.resize((1317, 790), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=232, y=0, width=1320, height=790)
#==================down image===============
        img4 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\game.jpg")
        img4 = img4.resize((235, 260), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=207, width=235, height=260)




        img5 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\dining.jpg")
        img5 = img5.resize((235, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=450, width=235, height=180)

        img6 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\room.jpg")
        img6 = img6.resize((360, 500), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg1 = Label(main_frame, image=self.photoimg6, bd=4, relief=RIDGE)
        lblimg1.place(x=1549, y=385, width=360, height=500)

        img7 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\food.jpg")
        img7 = img7.resize((383, 390), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        lblimg1 = Label(main_frame, image=self.photoimg7, bd=4, relief=RIDGE)
        lblimg1.place(x=1549, y=0, width=383, height=390)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)



    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
