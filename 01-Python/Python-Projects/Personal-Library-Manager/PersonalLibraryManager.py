import mysql.connector as c

# Connect to MySQL Database
conn = c.connect(
    host="localhost",
    user="root",  
    password="Abdul@666",  
    database="library"
)
cursor = conn.cursor()

# Library Manager Menu
while True:
    print("\nWelcome to your Personal Library Manager!")
    userInput = input(""" cmd
1. Add a book  
2. Remove a book  
3. Search for a book  
4. Display all books  
5. Display statistics  
6. Exit  
Enter your choice:  """)

    if userInput == "1":
        print("\nYou selected: Add a Book")
        title = input("Enter The Book Title: ").strip() 
        author = input("Enter The Book Author: ").strip()
        publication_Year = input("Enter The Book Publication Year: ").strip()
        genre = input("Enter The Book Genre: ").strip()
        reading = input("Have you read this book? (yes/no): ").strip().lower()

        try:
            cursor.execute("""
                INSERT INTO Books (title, author, publication_year, genre, read_status) 
                VALUES (%s, %s, %s, %s, %s)
            """, (title, author, publication_Year, genre, reading))
            conn.commit()
            print("✅ Book Added Successfully!")
        except c.Error as err:
            print(f"❌ Error: {err}")

    elif userInput == "2":
        print("\nYou selected: Remove a Book")
        remove_title = input("Enter the title of the book to remove: ").strip()

        cursor.execute("DELETE FROM Books WHERE title = %s", (remove_title,))
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Book Removed Successfully!")
        else:
            print("❌ Book Not Found!")

    elif userInput == "3":
        print("\nYou selected: Search For a Book")
        search_choice = input("""
    Search by:  
1. Title  
2. Author  
Enter your choice: """)

        if search_choice == "1":
            search_title = input("Enter the title: ").strip()
            cursor.execute("SELECT * FROM Books WHERE title = %s", (search_title,))
            book = cursor.fetchone()

            if book:
                print("\n📚 Book Found!", book)
            else:
                print("❌ Book not found!")

        elif search_choice == "2":
            search_author = input("Enter the Author: ").strip()
            cursor.execute("SELECT * FROM Books WHERE author = %s", (search_author,))
            books = cursor.fetchall()

            if books:
                print(f"\n📚 Books by {search_author}:")
                for book in books:
                    print(f"- {book}")
            else:
                print("❌ No books found by this author!")

        else:
            print("❌ Invalid Choice!")

    elif userInput == "4":
        print("\nYou selected: Display All Books")
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()

        if books:
            print("\n📚 Library Collection:")
            for book in books:
                print(f"- {book}")
        else:
            print("❌ No books in the library!")

    elif userInput == "5":
        print("\nYou selected: Display Statistics")
        cursor.execute("SELECT COUNT(*) FROM Books")
        total_books = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Books WHERE read_status = 'yes'")
        read_books = cursor.fetchone()[0]

        unread_books = total_books - read_books
        print(f"📊 Total Books: {total_books}")
        print(f"📖 Read Books: {read_books}, 📘 Unread Books: {unread_books}")

    elif userInput == "6":
        print("\n📚 Exiting Library Manager. Goodbye! 👋")
        break

    else:
        print("❌ Invalid Choice! Please enter a valid option.")

# Close the Database Connection
cursor.close()
conn.close()
