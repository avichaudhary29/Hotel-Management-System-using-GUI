from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #==========variables========
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        #=====title=======
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1910, height=60)

        # ========logo========
        img2 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\logo.jpg")
        img2 = img2.resize((100, 55), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=55)
      #=========labelFrame=====
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING DETAILS",font=("arial", 12, "bold"),padx=2,)
        labelframeleft.place(x=20,y=90,width=600,height=700)
        # ========labels and entries======
        #customer contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("arial", 10))
        entry_contact.grid(row=0, column=1)
        # featch data button
        btnFetchData = Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data", font=("arial", 12, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=450, y=4)

        # check in date
        check_in_date = Label(labelframeleft, text="Check in Date ", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29, font=("arial", 10))
        txtcheck_in_date.grid(row=1, column=1)

        # Check out Date
        lbl_Check_out = Label(labelframeleft, text="Check out Date ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft,textvariable=self.var_checkout, width=29, font=("arial", 10))
        txt_Check_out.grid(row=2, column=1)
        # =========room type=========
        label_RoomType = Label(labelframeleft, text="Room Type  ", font=("arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, width=29, font=("arial", 10),state="readonly")
        combo_RoomType["value"] = ("Single", "Double", "Luxury")
        combo_RoomType.grid(row=3, column=1)
        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room  ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomAvailable = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, width=29, font=("arial", 10))
        txtRoomAvailable.grid(row=4, column=1)
        # Meal
        lblMeal = Label(labelframeleft, text="Meal  ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft,textvariable=self.var_meal, width=29, font=("arial", 10))
        txtMeal.grid(row=5, column=1)

        #No Of Days
        lblNoOfDays = Label(labelframeleft, text="No Of Days  ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=29, font=("arial", 10))
        txtNoOfDays.grid(row=6, column=1)

        #Paid Tax
        lblNoOfDays = Label(labelframeleft, text="Paid Tax  ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=29, font=("arial", 10))
        txtNoOfDays.grid(row=7, column=1)

        #Sub Total
        lblNoOfDays = Label(labelframeleft, text="Sub Total  ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=29, font=("arial", 10))
        txtNoOfDays.grid(row=8, column=1)

        #Total Cost
        lblNoOfDays = Label(labelframeleft, text="Total Cost  ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=9, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_total, width=29, font=("arial", 10))
        txtNoOfDays.grid(row=9, column=1)
      #====Bill Button====
        btnBill=Button(labelframeleft, text="Bill", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1,sticky=W)
      #======btns=====
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=480,width=500,height=45)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        #======Right side=====
        img3 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\bed room.jpg")
        img3 = img3.resize((600, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=2, relief=RIDGE)
        lblimg.place(x=1200, y=100, width=600, height=300)

        #======tabel frame search system===
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM",font=("arial", 12, "bold"), padx=2, )
        Table_Frame.place(x=650, y=450, width=1210, height=300)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        combo_Search = ttk.Combobox(Table_Frame,font=("arial", 12), width=24, state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, font=("arial", 13), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("arial", 12), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", font=("arial", 12), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        #============show data table==
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=5,y=50,width=1200,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No of Days")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)



      #=====================All Data Fetch==============
    def Fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please eneter Contact Number",parent=self.root)
      else:
         conn=mysql.connector.connect(host="localhost",username="root",password="ducat123",database="world")
         my_cursor=conn.cursor()
         query=("select Name from customer where Mobile=%s")
         value=(self.var_contact.get(),)
         my_cursor.execute(query,value)
         row=my_cursor.fetchone()

         if row==None:
          messagebox.showerror("Error","This number not found",parent=self.root)
         else:
           conn.commit()
           conn.close()

           showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
           showDataframe.place(x=450,y=55,width=300,height=180)

           lblName=Label(showDataframe,text="Name:",font=("arial",12))
           lblName.place(x=0,y=0)
           lbl=Label(showDataframe,text=row,font=("arial",12))
           lbl.place(x=90,y=0)
        #=============Gender============
           conn=mysql.connector.connect(host="localhost",username="root",password="ducat123",database="world")
           my_cursor=conn.cursor()
           query=("select Gender from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()

           lblGender = Label(showDataframe, text="Gender:", font=("arial", 12))
           lblGender.place(x=0, y=30)
           lbl2 = Label(showDataframe, text=row, font=("arial", 12))
           lbl2.place(x=90, y=30)

          #=====================email===============
           conn=mysql.connector.connect(host="localhost",username="root",password="ducat123",database="world")
           my_cursor = conn.cursor()
           query = ("select Email from customer where Mobile=%s")
           value = (self.var_contact.get(),)
           my_cursor.execute(query, value)
           row = my_cursor.fetchone()

           lblemail = Label(showDataframe, text="Email:", font=("arial", 12))
           lblemail.place(x=0, y=60)
           lbl3 = Label(showDataframe, text=row, font=("arial", 12))
           lbl3.place(x=90, y=60)
          #===================Nationality===============
           conn = mysql.connector.connect(host="localhost", username="root", password="ducat123", database="world")
           my_cursor = conn.cursor()
           query = ("select Nationality from customer where Mobile=%s")
           value = (self.var_contact.get(),)
           my_cursor.execute(query, value)
           row = my_cursor.fetchone()

           lblNationality = Label(showDataframe, text="Gender:", font=("arial", 12))
           lblNationality.place(x=0, y=90)
           lbl4 = Label(showDataframe, text=row, font=("arial", 12))
           lbl4.place(x=90, y=90)
          #===============Address========================
           conn = mysql.connector.connect(host="localhost", username="root", password="ducat123", database="world")
           my_cursor = conn.cursor()
           query = ("select Address from customer where Mobile=%s")
           value = (self.var_contact.get(),)
           my_cursor.execute(query, value)
           row = my_cursor.fetchone()

           lblAddress = Label(showDataframe, text="Gender:", font=("arial", 12))
           lblAddress.place(x=0, y=120)
           lbl5 = Label(showDataframe, text=row, font=("arial", 12))
           lbl5.place(x=90, y=120)

if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
