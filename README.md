📚 Library Management System

Project Information

- Project Title: Library Management System
- Student Name: Aman Kumar
- Course: B.Tech Computer Science and Engineering
- Semester: 1st Semester
- ERP Number: RU-26-018
- Language: Python 3

Project Description

The Library Management System is a simple console-based Python application used to manage library books.

It allows users to add new books, issue books to members, return books, search books by title or author, and display all available book records.

All book details are stored in a text file named "library.txt" using file handling.

Features

1. Add Book: Add new books with a unique book ID.
2. Issue Book: Issue books to members.
3. Return Book: Return issued books.
4. Search Book: Search books by title or author.
5. Display All Books: View all books with their current status.
6. File Handling: Save and load book records using a text file.

Technologies Used

- Python 3
- Lists and Dictionaries
- Functions
- Conditional Statements
- Loops
- Text File Handling
- Exception Handling

Project Files

Library-Management-System/
│
├── main.py
├── library.txt
├── README.md
└── Summary.md

Requirements

- Python 3 installed on your system.
- No external libraries are required.

How to Run the Project

1. Download or clone the project repository.
2. Open the project folder.
3. Run the following command:

python main.py

4. Select an option from the menu.
5. Follow the instructions displayed on the screen.
6. Select Exit to save the book records and close the program.

Sample Input and Output

Example 1: Add Book

Input:

Choose option (1-6): 1
Title: Python Basics
Author: Mark Lutz

Output:

Book added. ID: B101 | Python Basics | Mark Lutz | Available

Example 2: Issue Book

Input:

Choose option (1-6): 2
Book ID: B101
Member: Riya

Output:

Book B101 issued to Riya. Status: Issued
Available books: 0

Example 3: Invalid Book ID

Input:

Choose option (1-6): 2
Book ID: B999

Output:

Book ID B999 not found.

Data Storage

All book records are stored in "library.txt".

Each record contains:

- Book ID
- Book Title
- Author Name
- Book Status

The records are separated using the "|" symbol.

Conclusion

This project helped me understand Python programming concepts such as functions, lists, dictionaries, loops, conditional statements, and file handling.

It also improved my logical thinking and practical programming skills.
