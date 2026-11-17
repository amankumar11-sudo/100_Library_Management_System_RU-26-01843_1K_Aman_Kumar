# Library Management System -- Project Summary

## 1. Project Overview

The Library Management System is a console-based application developed
using Python 3.

The project helps manage library books. It provides options to add
books, issue books to members, return books, search books by title or
author, and display all books.

Book details are stored as dictionaries inside a list. The program uses
a text file named `library.txt` to load and save book records.

## 2. Features Implemented

-   Add new books with automatically generated Book IDs.
-   Issue books to library members.
-   Prevent issuing a book that is already issued.
-   Return books.
-   Search books by title or author.
-   Display all book records.
-   Load and save book records using text file handling.

## 3. Difficulties Faced and Solutions

### 1. File Handling

**Difficulty:** Loading and saving book records using a text file.

**Solution:** Used `with open()` to read records from and write records
to `library.txt`.

### 2. Book ID Generation

**Difficulty:** Generating IDs for newly added books.

**Solution:** Used a simple ID-generation method that starts with `B101`
and increases for subsequent books.

### 3. Issue Book Management

**Difficulty:** Preventing a book from being issued more than once.

**Solution:** Checked the book's status before issuing it. If its status
is already `Issued`, the program displays a message and does not issue
it again.

### 4. Managing Book Records

**Difficulty:** Storing and accessing each book's details.

**Solution:** Used dictionaries inside a list to store the book ID,
title, author, and status.

## 4. Testing and Results

The project was checked against the four test cases provided in the
assignment.

### Test Case 1: Normal Input

-   Selected option 1 (Add Book).
-   Title: Python Basics
-   Author: Mark Lutz
-   Expected Book ID: B101
-   Expected result: The book is added with status `Available`.

### Test Case 2: Boundary / Minimum Input

-   Selected option 2 (Issue Book).
-   Book ID: B101
-   Member: Piya
-   Expected result: Book B101 is issued to Riya and the available book
    count is 0.

### Test Case 3: Invalid Input

-   Selected option 2 (Issue Book).
-   Book ID: B999
-   Expected result: `Book ID B999 not found.`

### Test Case 4: Different Valid Scenario

-   Added a book titled Data Science by Wes McKinney.
-   Expected new Book ID: B102.
-   Searched by author: McKinney.
-   Returned Book ID: B101.
-   Expected result: B102 is displayed in the search result and B101 is
    returned with status `Available`.

## 5. Concepts Learned

Through this project, I practised:

-   Variables and data types
-   Conditional statements
-   Loops
-   Functions
-   Lists and dictionaries
-   Text file handling
-   Exception handling
-   Basic problem-solving and logical thinking

## 6. Conclusion

This project helped me understand how Python programming concepts can be
used to develop a practical console-based application. I gained practice
in using functions, lists, dictionaries, conditions, loops, and text
file handling to manage library book records.
