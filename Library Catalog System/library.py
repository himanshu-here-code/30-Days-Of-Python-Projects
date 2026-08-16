import sqlite3

con = sqlite3.connect("Library Catalog System/library.db")
c = con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS books(
          id INTEGER PRIMARY KEY,
          title TEXT,
          author TEXT,
          status TEXT
          )""")
con.commit()
while True:
    print("1: Add a new book (Create)\n2: View all books (Read)\n3: Check out / Return a book (Update)\n4: Remove a lost book (Delete)\n5: Exit")
    user_choice = int(input("PLEASE ENTER A NUMBER(1,2,3,4,5): "))


    if user_choice not in (1,2,3,4,5):
        print("please enter a valid number.")
    elif user_choice == 1:
        print("------Add a Book-----\n")
        book_status = "Available"  
        book_title = input("Enter book title: ")
        book_title = book_title.capitalize()
        book_author = input("Enter author name: ")
        book_author = book_author.capitalize()
        c.execute("INSERT INTO books (title , author,status) VALUES (?,?,?)",(book_title,book_author,book_status))
        con.commit()
        print("book added successfully!\n")
        
    elif user_choice == 2:
        print("\n----View all Books----")
        c.execute("SELECT * FROM books")
        books = c.fetchall() 
        for book in books:
            print(f"{book[0]}. {book[1]} by {book[2]}")
        
    elif user_choice == 3:
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        for book in books:
            print(f"{book[0]}. {book[1]} by {book[2]}")
        
        try:
            library_book = int(input("Enter the book id: "))  
            c.execute("SELECT * FROM books WHERE id = ?", (library_book,))
            book = c.fetchone()
            
            if book is None:
                print("THIS IS NO BOOK WITH THIS ID.")
            else:
                print("1. Do you wanna issue it?\n2. Do you wanna return it?")
                action = input("(1, 2): ") 
                
                if action == "1":  
                    if book[3] == "Issued":
                        print("This book is already issued.")
                    else:
                        c.execute("UPDATE books SET status = 'Issued' WHERE id = ?", (library_book,))
                        con.commit()
                        print("Book issued successfully!")
                        
                elif action == "2": 
                    if book[3] == "Available":
                        print("This book is already available.")
                    else:
                        c.execute("UPDATE books SET status = 'Available' WHERE id = ?", (library_book,))
                        con.commit()
                        print("Book returned successfully!")
                else:
                    print("Invalid choice!")
                    
        except ValueError:
            print("Please enter a valid number for book ID.")

    elif user_choice == 4:
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        for book in books:
            print(f"{book[0]}. {book[1]} by {book[2]}")
        
        try:
            book_id = int(input("Enter the book id to remove: "))
            c.execute("SELECT * FROM books WHERE id = ?", (book_id,))
            book = c.fetchone()
            
            if book is None:
                print("THIS IS NO BOOK WITH THIS ID.")
            else:
                c.execute("DELETE FROM books WHERE id = ?", (book_id,))
                con.commit()
                print(f"Book '{book[1]}' removed successfully!")
                
        except ValueError:
            print("Please enter a valid number for book ID.")

    elif user_choice == 5:
        print("Exiting... Goodbye!")
        con.close()
        break
