from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1910x1000+0+0")
        #=====title=======
        lbl_title = Label(self.root, text="New Room Add", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1910, height=60)

        # ========logo========
        img2 = Image.open(r"C:\Users\Avi Chaudhary\Desktop\Hotel management(GUI)\logo.jpg")
        img2 = img2.resize((100, 55), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=55)
        # =========labelFrame=====
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM BOOKING DETAILS",font=("arial", 12, "bold"), padx=2, )
        labelframeleft.place(x=20, y=90, width=600, height=450)

        #floor
        lbl_floor = Label(labelframeleft, text="floor ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        entry_floor = ttk.Entry(labelframeleft, width=29, font=("arial", 10))
        entry_floor.grid(row=0, column=1)
        #Room No
        lbl_RoomNo = Label(labelframeleft, text="Room No ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        entry_RoomNo = ttk.Entry(labelframeleft, width=29, font=("arial", 10))
        entry_RoomNo.grid(row=1, column=1)

        #Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        entry_RoomType = ttk.Entry(labelframeleft, width=29, font=("arial", 10))
        entry_RoomType.grid(row=2, column=1)

        # ======btns=====
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=10, y=200, width=500, height=45)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold",width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        #=======================tabel frame search==================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="SHOW ROOM DETAILS",font=("arial", 12, "bold"), padx=2, )
        Table_Frame.place(x=750, y=90, width=700, height=450)


        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, column=("floor", "roomno", "roomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomType", text="Room Type")


        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomType", width=100)

        self.room_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()