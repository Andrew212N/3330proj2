import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import IntVar

class PubBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.title('Add Book')
        self.geometry("500x300")

        new_bk_label = ttk.Label(self, text = 'New Book Title: ')
        new_bk_label.grid(row = 1, column = 0)

        self.new_bk = ttk.Entry(self, width = 30)
        self.new_bk.grid(row = 1, column = 1)

        option = IntVar()

        tk.Radiobutton(self, text="Current Publisher", variable=option, value=1, command=self.cur_fr).grid(column=0, row=3)
        tk.Radiobutton(self, text="New Publisher", variable=option, value=2, command=self.new_fr).grid(column=1, row=3)

        self.new_frame = tk.Frame(self)
        self.cur_frame = tk.Frame(self)

        cur_pub_label = ttk.Label(self.cur_frame, text = 'Publisher Name: ')
        cur_pub_label.grid(row = 4, column = 0)

        self.cur_pub = ttk.Entry(self.cur_frame, width = 30)
        self.cur_pub.grid(row = 4, column = 1)

        # new_pub_label = ttk.Label(self.new_frame, text = 'Publisher Name: ')
        # new_pub_label.grid(row = 4, column = 0)

        # self.new_pub = ttk.Entry(self.new_frame, width = 30)
        # self.new_pub.grid(row = 4, column = 1)

        # pub_phone_label = ttk.Label(self.new_frame, text = 'Publisher Phone: ')
        # pub_phone_label.grid(row = 5, column = 0)

        # self.pub_phone = ttk.Entry(self.new_frame, width = 30)
        # self.pub_phone.grid(row = 5, column = 1)

        # pub_address_label = ttk.Label(self.new_frame, text = 'Publisher Address: ')
        # pub_address_label.grid(row = 6, column = 0)

        # self.pub_address = ttk.Entry(self.new_frame, width = 30)
        # self.pub_address.grid(row = 6, column = 1)

        # bwr_submit_button = ttk.Button(self, text = 'Add', command = self.bwr_submit)
        # bwr_submit_button.grid(row = 4, column = 0, pady = 10, padx = 10)

        pub_bk_close = ttk.Button(self, text = "Close", command = self.destroy)
        pub_bk_close.grid(row = 4, column = 1)


    def new_fr(self):
        self.cur_frame.grid_forget()
        self.new_frame.grid(row=1, column=0)

    def cur_fr(self):
        self.new_frame.grid_forget()
        self.cur_frame.grid(row=1, column=0)

    # def bwr_submit(self):
    #     bwr_submit_conn = sqlite3.connect('lms.db')
    #     sub_cur = bwr_submit_conn.cursor()
    #     sub_cur.execute("INSERT INTO Borrower VALUES (:name, :address, :phone)",
    #                     {
    #                         'name': self.bwr_name.get(),
    #                         'address': self.bwr_address.get(),
    #                         'phone': self.bwr_phone.get()
    #                     })
    #     bwr_submit_conn.commit()
    #     bwr_submit_conn.close()