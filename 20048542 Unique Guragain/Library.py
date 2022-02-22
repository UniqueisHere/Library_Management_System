from message import message
from date_and_time import get_date, get_time
from book_management import get_available_book, adding_new_book
from list_management import split_into_list, name_of_book, name_of_author, quantity_of_books,cost_of_books


def update_borrowed_details(book_value):
    with open("list_of_books.txt", "w+") as update_file:
        quantity_of_books[book_value] = int(quantity_of_books[book_value]) - 1
        for i in range(3):
            update_file.write(
                name_of_book[i] + "," + name_of_author[i] + "," + str(quantity_of_books[i]) + "," + "$" + cost_of_books[i] + "\n")


def update_return_detais(book_value):
    with open("list_of_books.txt", "w+") as update_file:
        quantity_of_books[book_value] = quantity_of_books[book_value] + 1
        for i in range(3):
            update_file.write(
                name_of_book[i] + "," + name_of_author[i] + "," + str(quantity_of_books[i]) + "," + "$" + cost_of_books[i] + "\n")


def borrow_book():
    first_name = input("Enter the first name of the borrower: ")
    last_name = input("Enter the last name of the borrower: ")
    borrower_text_file_name = f"Borrow-{first_name}.txt"
    print("Please select a option below:")

    for i in range(len(name_of_book)):
        print("Enter", i, "to borrow book", name_of_book[i])

    try:
        value = int(input("Choice: "))
        try:
            if(int(quantity_of_books[value]) > 0):
                with open(borrower_text_file_name, "w+") as write_file:
                    write_file.write("\t\t\t\t\t\tBook Borrower Details:-  \n")
                    write_file.write(
                        f"\t\t\t\tBorrowed By: {first_name} {last_name}\n")
                    write_file.write(
                        f"\tBorrowed Date: {get_date()} Borrowed Time: {get_time()}\n\n")
                    write_file.write(
                        "S.N. \t\t Bookname \t      Authorname \n")
                with open(borrower_text_file_name, "a") as f:
                    f.write(
                        "1. \t\t" + name_of_book[value] + "\t\t  " + name_of_author[value] + "\n")

                update_borrowed_details(value)
                print(
                    f"Book Borrowed Successfully by {first_name} {last_name} on {get_date()}")
                print(
                    f"Name of book : {name_of_book[value]} Price ${cost_of_books[value]}")
            else:
                print("The requested book is not available")
                borrow_book()
        except IndexError:
            print("")
            print("Only Books from numbers are valid!")
    except ValueError:
        print("")
        print("Please choose as printed.")


def return_book():
    first_name = input("Please enter first name of borrower: ")
    input("Please enter last name of borrower: ")
    borrower_text_file_name = f"Borrow-{first_name}.txt"
    try:
        with open(borrower_text_file_name, "r") as read_file:
            lines = []
            for item in read_file.readlines():
                lines.append(item.strip("$"))

        with open(borrower_text_file_name, "r") as read_file:
            data = read_file.read()
            print(data)
    except FileNotFoundError:
        print("The borrower name is incorrect")
        return_book()

    returner_text_file_name = f"Return-{first_name}.txt"

    with open(returner_text_file_name, "w+")as f:
        f.write("                Book Returner Details:- \n")
        f.write("                   Returned By: " + first_name+"\n")
        f.write("    Return Date: " + get_date() +
                "    Return Time:" + get_time()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")

    total = 0.0
    for i in range(3):
        if name_of_book[i] in data:
            with open(returner_text_file_name, "a") as f:
                f.write(str(i+1) +"\t\t" + name_of_book[i] + "\t\t$" + cost_of_books[i] + "\n")
            total += float(cost_of_books[i])
            update_return_detais(i)

    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat = input()
    if stat.lower() == "y":
        print("By how many days was the book returned late?")
        try:
            day = int(input())
            fine = 2*day
            with open(returner_text_file_name, "a")as f:
                f.write("\t\t\t\t\tFine: $" + str(fine)+"\n")
                total = total+fine
                f.write("\t\t\t\t\tTotal price: $" + str(total) + "\n")
            print("Final Total: " + "$"+str(total))
        except ValueError:
            print("Please enter integer number")
    elif stat.lower() == 'n':
        with open(returner_text_file_name, "a")as f:
            f.write("\t\t\t\t\tTotal: $" + str(total) + "\n")
    else:
        print("Invalid input")


def main_func():
    print("\t\t\tWelcome to the library management system :)")
    message()
    while True:
        input_data = input("Select a choice either A, D, B, R, E or H: ").upper()
        print()

        if input_data == 'D':
            print(get_available_book())
        elif input_data == 'A':
            adding_new_book()
        elif input_data == 'B':
            split_into_list(',')
            borrow_book()
        elif input_data == 'R':
            split_into_list(',')
            return_book()
        elif input_data == 'E':
            print("Thank you for using library management system")
            break
        elif input_data == 'H':
            message()
        else:
            print("The alphabet value you have enter is not in the suggested list.")
            print("Please type the following alphabet value")
            message()


main_func()