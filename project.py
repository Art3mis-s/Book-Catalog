import json

def main():
    print("Welcome to the Book Catalog!")
    catalog = load_catalog()

    while True:
        print("\n1. Add Book\n2. View Catalog\n3. Search Book\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_book(catalog)
        elif choice == "2":
            view_catalog(catalog)
        elif choice == "3":
            search_books(catalog)
        elif choice == "4":
            save_catalog(catalog)
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def load_catalog():
    try:
        with open("catalog.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": []}


def save_catalog(catalog):
    with open("catalog.json", "w") as file:
        json.dump(catalog, file, indent=2)

def add_book(catalog):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    status = input("Enter the status of the book (e.g., read, unread): ")
    review = input("Enter a brief review of the book: ")

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "status": status,
        "review": review,
    }

    catalog["books"].append(book)
    print(f"Book '{title}' added to the catalog.")




def view_catalog(catalog):
    if not catalog["books"]:
        print("The catalog is empty.")
    else:
        for index, book in enumerate(catalog["books"], start=1):
            print(f"{index}. {book['title']} by {book['author']} ({book['status']})")

def search_books(catalog):
    keyword = input("Enter a keyword to search for books: ").lower()
    results = []

    for book in catalog["books"]:
        if (
            keyword in book["title"].lower()
            or keyword in book["author"].lower()
            or keyword in book["genre"].lower()
        ):
           results.append(book)

    if not results:
        print("No matching books found.")
    else:
        print("\nMatching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['status']})")


if __name__ == "__main__":
    main()

