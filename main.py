from parse import parse
import library

books


def main():
    global books
    (n_days, books, tup_libraries) = parse()
    libraries = [library.Library(a, b, c) for (a, b, c) in tup_libraries]
    print(libraries)


if __name__ == "__main__":
    main()
