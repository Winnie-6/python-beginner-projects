import json

def save_library():
     with open("library.json", "w") as file:
          json.dump(library, file)
def load_library():
     global library
     try:
         with open("library.json", "r")as file:
            library = json.load(file)
     except FileNotFoundError:
      
      library = {
    "python basics": "Available",
    "Data science 101": "Available",
    "C programming":"Available",
    "introduction to psychology": "Available",
    "English basics": "Borrowed",
    "statistics":  "Available"
}
load_library()
# display functions
def display_books():
    print("\nAvailable Books:")
    for book, status in library.items():
        print(f"-{book}({status})")

def add_book():
    book = input("Enter the book you want to add: ")
    if book in library:
        print("Book already exists! ")
    else:
        library[book] = "Available"
        print(f"{book} has already been added to the library.")

def remove_book():
    book = input("Enter the book name to remove: ")
    if book in library:
       del library[book]
       print(f"{book} has been removed from the library")
    else:
            print("Book not found")

def borrow_book():
        book = input("Enter the book name to borrow: ")
        if book in library and library[book] == "Available":
            library[book] = "Borrowed"
            print(f"You borrowed {book}.")
        elif book in library:
            print("sorry, this book is already borrowed")
        else:
            print("Book not found!")     
def return_book():
    book = input("Enter the book name to return: ")
    if book in library and library[book] ==  "Borrowed":
        library [book] = "Available"
        print(f"you have returned the book")
    else:
        print("This book was not borrowed from here")

        # main menu

while True:
            print("\n===Library Managment System===")
            print("1. Display all book")
            print("2: Add a book")
            print("3: Remove a book")
            print("4.Borrow a book")
            print("5. Return a book")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                display_books()
            elif choice == "2":
                add_book()
            elif choice == "3":
                remove_book()
            elif choice == "4":
                borrow_book()
            elif choice == "5":
                return_book()
            elif choice == "6":
                print("Existing the system. Goodbye!")
                break
            else: 
                print("Invalid choice! please try again.")
