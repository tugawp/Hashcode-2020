from parse import parse
from main import books

class Library:
    def __init__(self, nBooks, nSignupDays, nBooksPerSecond, books):
        self.nBooks = nBooks
        self.nSignupDays = nSignupDays
        self.nBooksPerSecond = nBooksPerSecond
        self.books = books
    
    def sumBookValues(self):
        sum = 0
        for i in self.books:
            sum += books[i]

    def heuristic(self):
        return self.sumBookValues() / self.nSignupDays * self.nBooksPerSecond