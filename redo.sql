DROP TABLE Book_Authors;
CREATE TABLE Book_Authors(Book_id int not null, Author_name text, FOREIGN KEY (Book_id) REFERENCES Book (Book_id));

DROP TABLE Book_Copies;
CREATE TABLE Book_Copies(Book_id int, Branch_id int, No_of_copies int, FOREIGN KEY (Book_id) REFERENCES Book (Book_id), FOREIGN KEY (Branch_id) REFERENCES Library_Branch (Branch_id));

DROP TABLE Book_Loans;
CREATE TABLE Book_Loans(Book_id int, Branch_id int, Card_no integer, Date_out date, Due_date date, Returned_date date, FOREIGN KEY (Book_id) REFERENCES Book (Book_id), FOREIGN KEY (Branch_id) REFERENCES Library_Branch (Branch_id), FOREIGN KEY (Card_no) REFERENCES Borrower (Card_no));

DROP TABLE Book;
CREATE TABLE Book(Book_id integer not null, Title text, Book_publisher text, PRIMARY KEY (Book_id), FOREIGN KEY (Book_publisher) REFERENCES Publisher(Publisher_name));

DROP TABLE Borrower;
CREATE TABLE Borrower(Card_no integer not null, Name text, Address text, Phone char(12), PRIMARY KEY (Card_no));

DROP TABLE Library_Branch;
CREATE TABLE Library_Branch(Branch_id int not null, Branch_name text, Branch_address text, PRIMARY KEY (Branch_id));

DROP TABLE Publisher;
CREATE TABLE Publisher(Publisher_name text, Phone char(12), Address text, PRIMARY KEY (Publisher_name));

.mode csv

.import --skip 1 "/Users/kevincheung/Desktop/school/UTA/Spring 2023/CSE 3330/sqlite/Project 2/LMSDataset/Book_Authors.csv" Book_Authors

.import --skip 1 "/Users/kevincheung/Desktop/school/UTA/Spring 2023/CSE 3330/sqlite/Project 2/LMSDataset/Book_Copies.csv" Book_Copies

.import --skip 1 "/Users/kevincheung/Desktop/school/UTA/Spring 2023/CSE 3330/sqlite/Project 2/LMSDataset/Book_Loans.csv" Book_Loans

.import --skip 1 "/Users/kevincheung/Desktop/school/UTA/Spring 2023/CSE 3330/sqlite/Project 2/LMSDataset/Book.csv" Book

.import --skip 1 "/Users/kevincheung/Desktop/school/UTA/Spring 2023/CSE 3330/sqlite/Project 2/LMSDataset/Borrower.csv" Borrower

.import --skip 1 "/Users/kevincheung/Desktop/school/UTA/Spring 2023/CSE 3330/sqlite/Project 2/LMSDataset/Library_Branch.csv" Library_Branch

.import --skip 1 "/Users/kevincheung/Desktop/school/UTA/Spring 2023/CSE 3330/sqlite/Project 2/LMSDataset/Publisher.csv" Publisher

.mode box