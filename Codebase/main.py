# Store all books in a list
books = []


# Load books from text file
def load_books():
    try:
        with open("library.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                # Store each book as a dictionary
                book = {
                    "id": data[0],
                    "title": data[1],
                    "author": data[2],
                    "status": data[3]
                }

                books.append(book)

    except FileNotFoundError:
        pass


# Save all books to text file
def save_books():
    with open("library.txt", "w") as file:
        for book in books:
            file.write(
                f"{book['id']}|{book['title']}|"
                f"{book['author']}|{book['status']}\n"
            )


# Add a new book
def add_book():
    title = input("Title: ")
    author = input("Author: ")

    # Generate a new book ID
    book_id = "B" + str(101 + len(books))

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print(f"Book added. ID: {book_id} | {title} | {author} | Available")


# Issue a book to a member
def issue_book():
    book_id = input("Book ID: ")

    for book in books:
        if book["id"] == book_id:

            # Check if book is already issued
            if book["status"] == "Issued":
                print("Book is already issued.")
                return

            member = input("Member: ")
            book["status"] = "Issued"

            # Count available books
            count = 0
            for b in books:
                if b["status"] == "Available":
                    count += 1

            print(f"Book {book_id} issued to {member}. Status: Issued")
            print(f"Available books: {count}")
            return

    print(f"Book ID {book_id} not found.")


# Return an issued book
def return_book():
    book_id = input("Book ID: ")

    for book in books:
        if book["id"] == book_id:
            book["status"] = "Available"
            print(f"Book {book_id} returned. Status: Available")
            return

    print(f"Book ID {book_id} not found.")


# Search books by title or author
def search_book():
    key = input("Search by title/author: ").lower()

    for book in books:
        if key in book["title"].lower() or key in book["author"].lower():
            print(f"{book['id']} | {book['title']} | {book['author']} | {book['status']}")


# Display all books
def view_all():
    for book in books:
        print(f"{book['id']} | {book['title']} | {book['author']} | {book['status']}")


# Main program starts here
load_books()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All Books")
    print("6. Exit")

    choice = input("Choose option (1-6): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        view_all()
    elif choice == "6":
        save_books()
        print("Saved & Exited!")
        break
    else:
        print("Invalid option!")