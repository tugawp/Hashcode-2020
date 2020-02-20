import main


class Library:
    def __init__(self, nSignupDays, nBooksPerDay, books):
        self.nSignupDays = nSignupDays
        self.nBooksPerSecond = nBooksPerDay
        self.books = books

    def sumBookValues(self):
        sum = 0
        for i in self.books:
            sum += main.books[i]

    def heuristic(self):
        return self.sumBookValues() / self.nSignupDays * self.nBooksPerSecond
