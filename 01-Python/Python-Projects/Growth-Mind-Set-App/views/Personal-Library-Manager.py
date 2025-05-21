import streamlit as st
import mysql.connector as c

# Database Connection
def get_db_connection():
    return c.connect(
        host="localhost",
        user="root",  
        password="Abdul@666",  
        database="library"
    )

# Function to add a book
def add_book(title, author, year, genre, read_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Books (title, author, publication_year, genre, read_status) 
            VALUES (%s, %s, %s, %s, %s)
        """, (title, author, year, genre, read_status))
        conn.commit()
        st.success("✅ Book Added Successfully!")
    except c.Error as err:
        st.error(f"❌ Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to remove a book
def remove_book(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Books WHERE title = %s", (title,))
    conn.commit()
    if cursor.rowcount > 0:
        st.success("✅ Book Removed Successfully!")
    else:
        st.error("❌ Book Not Found!")
    cursor.close()
    conn.close()

# Function to search for books
def search_books(search_type, value):
    conn = get_db_connection()
    cursor = conn.cursor()
    if search_type == "Title":
        cursor.execute("SELECT * FROM Books WHERE title = %s", (value,))
    else:
        cursor.execute("SELECT * FROM Books WHERE author = %s", (value,))
    
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books

# Function to display all books
def get_all_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books

# Function to display statistics
def get_statistics():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Books")
    total_books = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Books WHERE read_status = 'yes'")
    read_books = cursor.fetchone()[0]

    unread_books = total_books - read_books
    cursor.close()
    conn.close()
    
    return total_books, read_books, unread_books

# Streamlit UI
st.title("📚 Library Manager")

menu = ["Add a Book", "Remove a Book", "Search Books", "View All Books", "Library Statistics"]
choice = st.sidebar.selectbox("Select an Option", menu)

if choice == "Add a Book":
    st.subheader("📥 Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    read_status = st.selectbox("Have you read this book?", ["yes", "no"])
    
    if st.button("Add Book"):
        add_book(title, author, year, genre, read_status)

elif choice == "Remove a Book":
    st.subheader("🗑️ Remove a Book")
    title = st.text_input("Enter the title of the book to remove")
    
    if st.button("Remove Book"):
        remove_book(title)

elif choice == "Search Books":
    st.subheader("🔍 Search for a Book")
    search_type = st.radio("Search By:", ["Title", "Author"])
    search_value = st.text_input(f"Enter {search_type}")
    
    if st.button("Search"):
        results = search_books(search_type, search_value)
        if results:
            for book in results:
                st.write(book)
        else:
            st.warning("❌ No books found!")

elif choice == "View All Books":
    st.subheader("📚 All Books in Library")
    books = get_all_books()
    if books:
        for book in books:
            st.write(book)
    else:
        st.warning("No books found in the library!")

elif choice == "Library Statistics":
    st.subheader("📊 Library Statistics")
    total, read, unread = get_statistics()
    st.write(f"📘 Total Books: {total}")
    st.write(f"📖 Read Books: {read}")
    st.write(f"📕 Unread Books: {unread}")
