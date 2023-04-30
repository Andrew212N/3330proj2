import sqlite3
import datetime
import tkinter as tk
from tkinter import ttk

#need to figure out how to insert card_no, returned date
class Checkout(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.title('Checkout Window')
        self.geometry("375x200")

        book_title_label = ttk.Label(self, text = 'Book Title: ')
        book_title_label.grid(row = 2, column = 0, pady = 10, padx = 5)

        self.book_title = ttk.Entry(self, width = 30)
        self.book_title.grid(row = 2, column = 1, padx = 5)


        chkout_func_button = ttk.Button(self, text = 'Checkout', command = self.chkout_func)
        chkout_func_button.grid(row = 4, column = 0, columnspan = 2)

        chkout_close = ttk.Button(self, text = "Close", command = self.destroy)
        chkout_close.grid(row = 4, column = 1, columnspan = 2)

    def chkout_func(self):
        chkout_con = sqlite3.connect('lms.db')
        chkout_cur = chkout_con.cursor()
        chkout_cur.execute("UPDATE Book_Copies SET No_of_copies = (bc.No_of_copies - 1) FROM Book_Copies bc WHERE bc.Book_id = (SELECT b.Book_id FROM Book b WHERE Title = :book_title)",
                        {
                                'book_title': self.book_title.get()
                        })
        chkout_cur.execute("INSERT INTO Book_Loans VALUES ((SELECT Book_id FROM Book WHERE Title = :book_title), (SELECT Branch_id FROM Book_Copies WHERE Book_id = (SELECT Book_id FROM Book WHERE Title = :book_title)), NULL, :date_out, :due_date, NULL)",
                        {
                                'book_title': self.book_title.get(),
                                'date_out': datetime.date.today(),
                                'due_date': datetime.date.today() + datetime.timedelta(days = 10)
                        })
        chkout_cur.execute("SELECT No_of_Copies FROM Book_Copies bc WHERE bc.Book_id = (SELECT b.Book_id FROM Book b WHERE Title = :book_title)", 
                        {
                            'book_title': self.book_title.get()
                        })
        
        records = chkout_cur.fetchall()

        print_rec = 'Number of Copies remaining: ' + str(records[0][0])

        chkout_label = ttk.Label(self, text = print_rec)
        chkout_label.grid(row = 6, column = 0, columnspan = 2)

        chkout_con.commit()
        chkout_con.close()