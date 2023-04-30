import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import IntVar

class PubBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.title('Add Book')
        self.geometry("700x300")

        option = IntVar()

        tk.Radiobutton(self, text="Current Publisher", variable=option, value=1, command=self.cur_fr).grid(column=0, row=0)
        tk.Radiobutton(self, text="New Publisher", variable=option, value=2, command=self.new_fr).grid(column=1, row=0)

        new_bk_label = ttk.Label(self, text = 'New Book Title: ')
        new_bk_label.grid(row = 1, column = 0)

        self.new_bk = ttk.Entry(self, width = 30)
        self.new_bk.grid(row = 1, column = 1)

        auth_label = ttk.Label(self, text = 'Author: ')
        auth_label.grid(row = 2, column = 0)

        self.auth = ttk.Entry(self, width = 30)
        self.auth.grid(row = 2, column = 1)

        self.new_frame = tk.Frame(self)
        self.cur_frame = tk.Frame(self)

        cur_pub_label = ttk.Label(self.cur_frame, text = 'Publisher Name: ')
        cur_pub_label.grid(row = 5, column = 0)

        self.cur_pub = ttk.Entry(self.cur_frame, width = 30)
        self.cur_pub.grid(row = 5, column = 1)

        new_pub_label = ttk.Label(self.new_frame, text = 'New Publisher Name: ')
        new_pub_label.grid(row = 5, column = 0)

        self.new_pub = ttk.Entry(self.new_frame, width = 30)
        self.new_pub.grid(row = 5, column = 1)

        pub_phone_label = ttk.Label(self.new_frame, text = 'Publisher Phone: ')
        pub_phone_label.grid(row = 6, column = 0)

        self.pub_phone = ttk.Entry(self.new_frame, width = 30)
        self.pub_phone.grid(row = 6, column = 1)

        pub_address_label = ttk.Label(self.new_frame, text = 'Publisher Address: ')
        pub_address_label.grid(row = 7, column = 0)

        self.pub_address = ttk.Entry(self.new_frame, width = 30)
        self.pub_address.grid(row = 7, column = 1)

        pub_button = ttk.Button(self, text = "Add Publisher", command = self.pub_submit)
        pub_button.grid(row = 8, column = 1)

        bwr_submit_button = ttk.Button(self, text = 'Add Book', command = self.bk_submit)
        bwr_submit_button.grid(row = 9, column = 1)

        pub_bk_close = ttk.Button(self, text = "Close", command = self.destroy)
        pub_bk_close.grid(row = 10, column = 1)


    def new_fr(self):
        self.cur_frame.grid_forget()
        self.new_frame.grid(row=4, column=0)

    def cur_fr(self):
        self.new_frame.grid_forget()
        self.cur_frame.grid(row=4, column=0)

    def pub_submit(self):
        pub_submit_conn = sqlite3.connect('lms.db')
        pub_cur = pub_submit_conn.cursor()
        pub_cur.execute("INSERT INTO Publisher VALUES (:name, :phone, :address)",
                        {
                            'name': self.new_pub.get(),
                            'phone': self.pub_phone.get(),
                            'address': self.pub_address.get()
                        })
        pub_submit_conn.commit()
        pub_submit_conn.close()

    def add_auth(self):
        add_auth_conn = sqlite3.connect('lms.db')
        auth_cur = add_auth_conn.cursor()
        auth_cur.execute("INSERT INTO Book_Authors VALUES ((SELECT Book_id FROM Book WHERE Title = :book_title), :auth)",
                        {
                            'name': self.new_pub.get(),
                            'auth': self.auth.get()
                        })
        add_auth_conn.commit()
        add_auth_conn.close()
    
    def bk_submit(self):
        bk_submit_conn = sqlite3.connect('lms.db')
        bk_cur = bk_submit_conn.cursor()
        if self.new_pub.get() != '':
            bk_cur.execute("INSERT INTO Book(Title, Book_publisher) VALUES (:book_title, :pub_name)",
                            {
                                'book_title': self.new_bk.get(),
                                'pub_name': self.new_pub.get()
                            })
        elif self.cur_pub.get() != '':
            bk_cur.execute("INSERT INTO Book(Title, Book_publisher) VALUES (:book_title, :pub_name)",
                            {
                                'book_title': self.new_bk.get(),
                                'pub_name': self.cur_pub.get()
                            })
        bk_submit_conn.commit()
        bk_submit_conn.close()