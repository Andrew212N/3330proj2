import sqlite3

import tkinter as tk
from tkinter import ttk
import checkout as co
import borrower as bo
import pub_book as bp

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Library Management System')
        self.geometry("400x300")

        label = ttk.Label(self, text ="Startpage", font = ("Verdana", 35))
        label.pack()

        chkout_button = ttk.Button(self, text = "Checkout Window", command = self.chkout_open)
        chkout_button.pack()

        add_bwr_button = ttk.Button(self, text = "Add Borrower", command = self.bwr_open)
        add_bwr_button.pack()

        add_book_button = ttk.Button(self, text = "Add Book with Publisher", command = self.pub_bk_open)
        add_book_button.pack()

        root_close = ttk.Button(self, text = "Close System", command = self.destroy)
        root_close.pack()

    def chkout_open(self):
        checkout = co.Checkout(self)
        checkout.grab_set()

    def bwr_open(self):
        bwr = bo.Borrower(self)
        bwr.grab_set()

    def pub_bk_open(self):
        pub_bk = bp.PubBook(self)
        pub_bk.grab_set()


if __name__ == "__main__":
    app = Root()
    app.mainloop()
