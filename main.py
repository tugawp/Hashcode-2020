from parse import parse
import library


def choose_library(libs, n_days_remain, bookValues):
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
    libraries = [library.Library(a, b, c) for (a, b, c) in tup_libraries]
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


if __name__ == "__main__":
    main()
