def get_available_book():
    with open("list_of_books.txt", "r") as read_file:
        return read_file.read()

def adding_new_book():
    book_name = input("Enter the name of book: ")
    author_name = input("Enter author name: ")
    book_quantity = input(f"How many {book_name} book you want to add: ")
    price = input(f"Enter the price of {book_name} book: ")
    with open('list_of_books.txt', 'a') as add_book:
        add_book.writelines(
            f"{book_name},{author_name},{book_quantity},{price}\n")
    print("**********Book added sucessfully***************")

