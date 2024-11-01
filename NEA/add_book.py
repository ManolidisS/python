from book_database import book_database

def add_book(name,author,withdrawn):
    book_database.append({
        "Name": name,
        "Author": author,
        "Withdrawn": withdrawn}
    )
    with open("book_database.py", "w") as file:
        file.write(("book_database = ")+str(book_database))

add_book(str(input("Enter the book's title: ")), str(input("Enter the book's author: ")), "No")