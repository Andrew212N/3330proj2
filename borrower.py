import sqlite3
import tkinter as tk
from tkinter import ttk

class Borrower(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.title('Add Borrower')
        self.geometry("450x300")

        bwr_name_label = ttk.Label(self, text = 'Borrower Name: ')
        bwr_name_label.grid(row = 1, column = 0)

        self.bwr_name = ttk.Entry(self, width = 30)
        self.bwr_name.grid(row = 1, column = 1)

        bwr_address_label = ttk.Label(self, text = 'Borrower Address: ')
        bwr_address_label.grid(row = 2, column = 0)

        self.bwr_address = ttk.Entry(self, width = 30)
        self.bwr_address.grid(row = 2, column = 1)

        bwr_phone_label = ttk.Label(self, text = 'Borrower Phone: ')
        bwr_phone_label.grid(row = 3, column = 0)

        self.bwr_phone = ttk.Entry(self, width = 30)
        self.bwr_phone.grid(row = 3, column = 1)

        bwr_submit_button = ttk.Button(self, text = 'Add', command = self.bwr_submit)
        bwr_submit_button.grid(row = 4, column = 0, pady = 10, padx = 10)

        chkout_close = ttk.Button(self, text = "Close", command = self.destroy)
        chkout_close.grid(row = 4, column = 1)

    def bwr_submit(self):
        bwr_submit_conn = sqlite3.connect('lms.db')
        sub_cur = bwr_submit_conn.cursor()
        sub_cur.execute("INSERT INTO Borrower(Name, Address, Phone) VALUES (:name, :address, :phone)",
                        {
                            'name': self.bwr_name.get(),
                            'address': self.bwr_address.get(),
                            'phone': self.bwr_phone.get()
                        })
        bwr_submit_conn.commit()
        bwr_submit_conn.close()