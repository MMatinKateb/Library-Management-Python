import Library
import sys

if __name__ == "__main__":

    book1 = Library.Book("OS", "Silberschatz", 1111, 15, 20)
    book2 = Library.Book("DS & A", "CLRS", 2222, 10, 20)
    book3 = Library.Book("Pearson1", "John Doe1", 3333, 20, 30)
    book4 = Library.Book("Pearson2", "John Doe2", 4444, 15, 20)
    book5 = Library.Book("Pearson3", "John Doe3", 5555, 15, 20)
    lib = Library.Library([book1, book2, book3, book4, book5])

    if "--find-by-author" in sys.argv:
        lib.search_by_author(sys.argv[sys.argv.index("--find-by-author")+1])
    if "--remove-by-title" in sys.argv:
        lib.remove_book(sys.argv[sys.argv.index("--remove-by-title")+1])
    if "--show-all" in sys.argv:
        lib2 = Library.Library([]) # new instance
        lib2.show_books()
        lib2.__del__()
    if "--flush-data" in sys.argv:
        lib.remove_book("")