import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk

class numOfCopies(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.title('Number of Copies')
        self.geometry('300x200')

        noc_title_label = ttk.Label(self, text = 'Enter Book Title: ')
        noc_title_label.grid(row = 2, column = 0, pady = 10, padx = 10)

        self.noc_entry = ttk.Entry(self, width = 30)
        self.noc_entry.grid(row = 3, column = 0, padx = 10)

        noc_search_button = ttk.Button(self, text = 'Submit', command = self.noc_search_function)
        noc_search_button.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)
    
    def noc_search_function(self):
        noc_con = sqlite3.connect('./lms.db')
        noc_cur = noc_con.cursor()
        noc_cur.execute("SELECT Library_Branch.Branch_name, SUM(Book_Loans.Book_id IS NOT NULL) as Loaned_copies FROM Book JOIN Book_Copies ON Book.Book_id = Book_Copies.Book_id JOIN Library_Branch ON Book_Copies.Branch_id = Library_Branch.Branch_id LEFT JOIN Book_Loans ON Book_Copies.Book_id = Book_Loans.Book_id AND Book_Copies.Branch_id = Book_Loans.Branch_id WHERE Book.Title = :book_title GROUP BY Library_Branch.Branch_name;",
                        {
                            'book_title' : self.book_title.get()
                        })
        records = noc_cur.fetchall()
        print_rec = 'Number of Copies per branch: ' + str(records[0][0])

        noc_label = ttk.Label(self, text = print_rec)
        noc_label.grid(row = 6, column = 0, columnspan = 2, padx = 10)

        noc_con.commit()
        noc_con.close()
