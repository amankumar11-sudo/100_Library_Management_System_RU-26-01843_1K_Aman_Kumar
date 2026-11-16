library = []

# 1. Load books from file
def load_books():
    try:
        with open("library.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) != 5:
                    continue

                book = {
                    "id": data[0],
                    "title": data[1],
                    "author": data[2],
                    "status": data[3],
                    "member": data[4]
                }

                library.append(book)

    except FileNotFoundError:
        print("New library created.")


# 2. Save books into file
def save_books():
    with open("library.txt", "w") as file:
        for book in library:
            data = [
                book["id"],
                book["title"],
                book["author"],
                book["status"],
                book["member"]
            ]

            file.write("|".join(data) + "\n")


# 3. Find book using ID
def find_book(book_id):
    for book in library:
        if book["id"] == book_id:
            return book

    return None


# 4. Generate unique book ID
def generate_id():
    last_id = 100

    for book in library:
        current_id = int(book["id"][1:])

        if current_id > last_id:
            last_id = current_id

    return "B" + str(last_id + 1)


# 5. Add a new book
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    if "|" in title or "|" in author:
        print("Please don't use | in book details.")
        return

    book = {
        "id": generate_id(),
        "title": title,
        "author": author,
        "status": "Available",
        "member": ""
    }

    library.append(book)
    save_books()

    print("Book added successfully!")
    print("Book ID:", book["id"])


# 6. Issue a book
def issue_book():
    book_id = input("Enter book ID: ").strip().upper()

    book = find_book(book_id)

    if book is None:
        print("Book not found.")
        return

    if book["status"] == "Issued":
        print("Book is already issued.")
        return

    member_name = input("Enter member name: ").strip()

    if not member_name:
        print("Member name cannot be empty.")
        return

    if "|" in member_name:
        print("Invalid member name.")
        return

    book["status"] = "Issued"
    book["member"] = member_name

    save_books()

    print("Book issued successfully!")


# 7. Return a book
def return_book():
    book_id = input("Enter book ID: ").strip().upper()

    book = find_book(book_id)

    if book is None:
        print("Book not found.")
        return

    if book["status"] == "Available":
        print("Book is already available.")
        return

    book["status"] = "Available"
    book["member"] = ""

    save_books()

    print("Book returned successfully!")


# 8. Search a book
def search_book():
    search_name = input("Enter title or author: ").strip().lower()

    if not search_name:
        print("Search cannot be empty.")
        return

    found = False

    for book in library:
        if (search_name in book["title"].lower()
                or search_name in book["author"].lower()):

            print(
                book["id"], "|",
                book["title"], "|",
                book["author"], "|",
                book["status"]
            )

            found = True

    if not found:
        print("No matching book found.")


# 9. Display all books
def display_books():
    if not library:
        print("Library is empty.")
        return

    print("\nID | TITLE | AUTHOR | STATUS")
    print("-" * 50)

    available = 0
    issued = 0

    for book in library:
        print(
            book["id"], "|",
            book["title"], "|",
            book["author"], "|",
            book["status"]
        )

        if book["status"] == "Available":
            available += 1
        else:
            issued += 1

    print("-" * 50)
    print("Total books:", len(library))
    print("Available books:", available)
    print("Issued books:", issued)


# 10. Main program
load_books()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display All Books")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        display_books()

    elif choice == "6":
        save_books()
        print("Thank you! Program closed.")
        break

    else:
        print("Invalid choice. Try again.")
