CREATE TABLE Book_Authors(Book_id int not null, Author_name text, FOREIGN KEY (Book_id) REFERENCES Book (Book_id));

CREATE TABLE Book_Copies(Book_id int, Branch_id int, No_of_copies int, FOREIGN KEY (Book_id) REFERENCES Book (Book_id), FOREIGN KEY (Branch_id) REFERENCES Library_Branch (Branch_id));

CREATE TABLE Book_Loans(Book_id int, Branch_id int, Card_no INTEGER, Date_out date, Due_date date, Returned_date date, FOREIGN KEY (Book_id) REFERENCES Book (Book_id), FOREIGN KEY (Branch_id) REFERENCES Library_Branch (Branch_id), FOREIGN KEY (Card_no) REFERENCES Borrower (Card_no));

CREATE TABLE Book(Book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Title text, Book_publisher text);

CREATE TABLE Borrower(Card_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name text, Address text, Phone char(12));

CREATE TABLE Library_Branch(Branch_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Branch_name text, Branch_address text);

CREATE TABLE Publisher(Publisher_name text, Phone char(12), Address text, PRIMARY KEY (Publisher_name));

.mode csv

.import --skip 1 "./LMSDataset/Book_Authors.csv" Book_Authors

.import --skip 1 "./LMSDataset/Book_Copies.csv" Book_Copies

.import --skip 1 "./LMSDataset/Book_Loans.csv" Book_Loans

.import --skip 1 "./LMSDataset/Book.csv" Book

.import --skip 1 "./LMSDataset/Borrower.csv" Borrower

.import --skip 1 "./LMSDataset/Library_Branch.csv" Library_Branch

.import --skip 1 "./LMSDataset/Publisher.csv" Publisher

.mode box