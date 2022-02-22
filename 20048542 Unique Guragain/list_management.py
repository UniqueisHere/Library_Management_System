name_of_book = []
name_of_author = []
quantity_of_books = []
cost_of_books = []

def split_into_list(split_on):
    with open("list_of_books.txt", "r") as nex:
        lines = []
        for line in nex.readlines():
            lines.append(line.strip('\n'))
        for i in range(len(lines)):
            index = 0
            for items in lines[i].split(split_on):
                if index == 0:
                    if items not in name_of_book:
                        name_of_book.append(items)
                elif index == 1:
                    if items not in name_of_author:
                        name_of_author.append(items)
                elif index == 2:
                    if items not in quantity_of_books:
                        quantity_of_books.append(items)
                elif index == 3:
                    if items not in cost_of_books:
                        cost_of_books.append(items.strip("$"))
                index += 1
