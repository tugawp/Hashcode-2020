def parse():
    # _ is number of books, don't care
    [_, n_libraries, n_days] = [int(x) for x in input().split()]
    book_values = [int(x) for x in input().split()]
    libraries = []
    for _ in range(n_libraries):
        # _ is number books lib, don't care
        [_, n_days_lib, book_rate] = \
            [int(x) for x in input().split()]
        lib_books = [int(x) for x in input().split()]
        library = (n_days_lib, book_rate, lib_books)
        libraries.append(library)
    return (n_days, book_values, libraries)


if __name__ == "__main__":
    print(parse())
