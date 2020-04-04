import os


class Library:

    def __init__(self, id:int, num_books: int, signup: int, ship_per_day: int, books: list):
        self.id = id
        self.num_books = num_books
        self.signup = signup
        self.ship_per_day = ship_per_day
        self.books = books

    def order_books(self, value):
        new = []

        order = []
        for book in value:
            if book in self.books:
                order.append((book, value[book]))
        order.sort(key=lambda x: x[1], reverse=True)
        for item in order:
            new.append(item[0])

        self.books = new


def main(input: list, file_name):
    """
    """
    print(1)
    line_1 = input[0].split(" ")
    num_books, num_libr, num_scan_day = int(line_1[0]), int(line_1[1]), int(line_1[2])

    book_scores = input[1].split(" ")
    scores = {}
    for idx, item in enumerate(book_scores):
        scores[idx] = int(item)

    libraries = []
    id = 0
    print(2)
    for j in range(2, len(input), 2):
        libr_line_1 = input[j].split(" ")
        books_in_lib = [int(k) for k in input[j+1].split(" ")]

        libraries.append(Library(id, int(libr_line_1[0]), int(libr_line_1[1]),
                                 int(libr_line_1[2]), books_in_lib))
        id += 1

    # for libr in libraries:
    #     libr.order_books(scores)
    #
    # def exp(x):
    #     return (num_scan_day-x.signup)*x.ship_per_day - x.num_books

    books_to_send = {}
    all_books_sent = []

    # libraries.sort(key=lambda x: exp(x))
    lib_q = libraries
    lib_to_scan = []
    print(3)
    for t in range(num_scan_day + 1):

        if lib_q:
            if lib_q[0].signup == 0:
                lib_to_scan.append(lib_q.pop(0))
            else:
                lib_q[0].signup -= 1

        for lib in lib_to_scan:
            j = 0
            while j < lib.ship_per_day:
                if len(lib.books) > 0:
                    if lib.books[0] not in all_books_sent:
                        all_books_sent.append(lib.books[0])
                        if lib.id in books_to_send:
                            books_to_send[lib.id].append(lib.books[0])
                        else:
                            books_to_send[lib.id] = [lib.books[0]]
                            lib.books.pop(0)
                            j += 1
                    else:
                        lib.books.pop(0)
                else:
                    break
    print(4)
    sol = ""

    sol += (str(len(lib_to_scan)) + "\n")
    for lib in lib_to_scan:
        if lib.id in books_to_send:
            sol += (str(lib.id) + " " + str(len(books_to_send[lib.id])) + "\n")
            to_send = ""
            for book in books_to_send[lib.id]:
                to_send += (str(book) + " ")
            sol += (to_send.strip() + "\n")
        else:
            break

    with open("./output/" + "out_" + file_name, "w") as out_f:
        out_f.write(sol.strip())
    out_f.close()




if __name__ == "__main__":

    for file in os.listdir("./input"):
        print(file)
        with open("./input/" + file) as f:
            input = []
            for line in f:
                line = line.strip()
                if line != " " and line != "":
                    input.append(line)

            main(input, file)

        f.close()
