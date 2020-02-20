from parse import parse
import library
import math


def choose_library(libs, n_days_remain, bookValues):
    if len(libs) == 0:
        return math.inf, None
    curr_max = libs[0].heuristic(bookValues)
    max_lib_i = 0
    for i in range(len(libs)):
        lib = libs[i]
        if lib.nSignupDays >= n_days_remain:
            continue
        h = lib.heuristic(bookValues)
        if h > curr_max:
            curr_max = h
            max_lib_i = i
    max_lib = libs.pop(max_lib_i)
    return max_lib.nSignupDays, max_lib


def main():
    (n_days, bookValues, tup_libraries) = parse()
    libraries = []
    for idx in range(len(tup_libraries)):
        (a, b, c) = tup_libraries[idx]
        libraries.append(library.Library(a, b, c, idx))
    day = 0
    days_till_sign_up = 0
    signed_up_libs = []
    next_lib = None
    while day < n_days:
        if days_till_sign_up == 0:
            if next_lib:
                signed_up_libs.append(next_lib)
            days_till_sign_up, next_lib = choose_library(libraries, n_days - day, bookValues)
        day += 1
        days_till_sign_up -= 1

        for lib in signed_up_libs:
            lib.sendBooks(bookValues)
    # output
    print(str(len(signed_up_libs)))
    for lib in signed_up_libs:
        print(str(lib.idx), str(len(lib.booksSent)))
        line = ""
        for book in lib.booksSent:
            line += str(book) + ", "
        print(line[:-2])


if __name__ == "__main__":
    main()

