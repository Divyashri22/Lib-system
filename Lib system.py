
class Library:

    def __init__(self):
        self.books = {}
        self.members = {}
        self.transactions = []

    # ADD BOOK
    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author: ")

        try:
            copies = int(input("Enter Number of Copies: "))
            if copies <= 0:
                print("Copies must be greater than zero!")
                return
        except ValueError:
            print("Enter a valid number!")
            return

        self.books[book_id] = {
            "title": title,
            "author": author,
            "total": copies,
            "available": copies
        }

        print("Book added successfully!")

    # UPDATE BOOK
    def update_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        print("1. Update Title")
        print("2. Update Author")
        print("3. Update Copies")

        choice = input("Enter choice: ")

        if choice == "1":
            self.books[book_id]["title"] = input("New Title: ")

        elif choice == "2":
            self.books[book_id]["author"] = input("New Author: ")

        elif choice == "3":
            try:
                copies = int(input("New Total Copies: "))
                borrowed = (
                    self.books[book_id]["total"]
                    - self.books[book_id]["available"]
                )

                if copies < borrowed or copies <= 0:
                    print("Invalid number of copies!")
                    return

                self.books[book_id]["total"] = copies
                self.books[book_id]["available"] = copies - borrowed

            except ValueError:
                print("Invalid number!")
                return

        else:
            print("Invalid choice!")
            return

        print("Book updated successfully!")

    # REMOVE BOOK
    def remove_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        if book["available"] != book["total"]:
            print("Cannot remove borrowed books!")
            return

        del self.books[book_id]
        print("Book removed successfully!")

    # REGISTER MEMBER
    def add_member(self):
        member_id = input("Enter Member ID: ")

        if member_id in self.members:
            print("Member already exists!")
            return

        name = input("Enter Member Name: ")

        self.members[member_id] = {
            "name": name,
            "borrowed": []
        }

        print("Member registered successfully!")

    # LIST MEMBERS
    def list_members(self):
        if not self.members:
            print("No members registered!")
            return

        for member_id, member in self.members.items():
            print(
                member_id,
                "|",
                member["name"],
                "| Borrowed:",
                len(member["borrowed"])
            )

    # BORROW BOOK
    def borrow_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        if member_id not in self.members:
            print("Member not found!")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book["available"] <= 0:
            print("No copies available!")
            return

        if len(member["borrowed"]) >= 3:
            print("Borrowing limit reached!")
            return

        book["available"] -= 1
        member["borrowed"].append(book_id)

        self.transactions.append({
            "book": book_id,
            "member": member_id,
            "status": "Borrowed"
        })

        print("Book borrowed successfully!")

    # RETURN BOOK
    def return_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if member_id not in self.members:
            print("Member not found!")
            return

        member = self.members[member_id]

        if book_id not in member["borrowed"]:
            print("This member has not borrowed this book!")
            return

        member["borrowed"].remove(book_id)
        self.books[book_id]["available"] += 1

        self.transactions.append({
            "book": book_id,
            "member": member_id,
            "status": "Returned"
        })

        print("Book returned successfully!")

    # SEARCH BOOK
    def search_book(self):
        keyword = input("Enter title, author or ID: ").lower()
        found = False

        for book_id, book in self.books.items():

            if (
                keyword in book_id.lower()
                or keyword in book["title"].lower()
                or keyword in book["author"].lower()
            ):
                print("\nBook ID:", book_id)
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Available:", book["available"])
                found = True

        if not found:
            print("No matching books found!")

    # AVAILABLE BOOKS
    def available_books(self):
        found = False

        for book_id, book in self.books.items():
            if book["available"] > 0:
                print(
                    book_id,
                    "-",
                    book["title"],
                    "- Available:",
                    book["available"]
                )
                found = True

        if not found:
            print("No available books!")

    # BORROWED BOOKS
    def borrowed_books(self):
        found = False

        for member_id, member in self.members.items():
            for book_id in member["borrowed"]:
                print(
                    self.books[book_id]["title"],
                    "- Borrowed by:",
                    member["name"]
                )
                found = True

        if not found:
            print("No borrowed books!")

    # ALL BOOKS
    def list_books(self):
        if not self.books:
            print("Library is empty!")
            return

        for book_id, book in self.books.items():
            print("\nBook ID:", book_id)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Total Copies:", book["total"])
            print("Available Copies:", book["available"])

    # TRANSACTION HISTORY
    def history(self):
        if not self.transactions:
            print("No transactions found!")
            return

        for transaction in self.transactions:
            book_id = transaction["book"]
            member_id = transaction["member"]

            print(
                "Book:", self.books[book_id]["title"],
                "| Member:", self.members[member_id]["name"],
                "| Status:", transaction["status"]
            )

    # DASHBOARD
    def dashboard(self):
        total = 0
        available = 0
        borrowed = 0

        for book in self.books.values():
            total += book["total"]
            available += book["available"]

        borrowed = total - available

        print("\n========== LIBRARY DASHBOARD ==========")
        print("Unique Book Titles:", len(self.books))
        print("Total Book Copies:", total)
        print("Available Copies:", available)
        print("Borrowed Copies:", borrowed)
        print("Registered Members:", len(self.members))
        print("Total Transactions:", len(self.transactions))
        print("=======================================")


# MAIN PROGRAM

library = Library()

while True:

    print("\n========== SMART LIBRARY MANAGEMENT ==========")
    print("1. Add New Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. Register New Member")
    print("5. List Members")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Search Book")
    print("9. List Available Books")
    print("10. Show Borrowed Books")
    print("11. List All Books")
    print("12. Transaction History")
    print("13. Library Dashboard")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.update_book()

    elif choice == "3":
        library.remove_book()

    elif choice == "4":
        library.add_member()

    elif choice == "5":
        library.list_members()

    elif choice == "6":
        library.borrow_book()

    elif choice == "7":
        library.return_book()

    elif choice == "8":
        library.search_book()

    elif choice == "9":
        library.available_books()

    elif choice == "10":
        library.borrowed_books()

    elif choice == "11":
        library.list_books()

    elif choice == "12":
        library.history()

    elif choice == "13":
        library.dashboard()

    elif choice == "0":
        print("Thank you for using Smart Library!")
        break

    else:
        print("Invalid choice! Try again.")
