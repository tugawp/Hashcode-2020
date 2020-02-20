import main


class Library:
    def __init__(self, nSignupDays, nBooksPerDay, books):
        self.nSignupDays = nSignupDays
        self.nBooksPerSecond = nBooksPerDay
        self.books = books
        self.booksSent = []

    def sumBookValues(self, bookValues):
        sm = 0

        for i in self.books:
            sm += bookValues[i]

        return sm

    def heuristic(self, bookValues):
        return self.sumBookValues(bookValues) / self.nSignupDays * self.nBooksPerSecond

    def biggerThanMinor(self, value, bookValues):
        minorValue = bookValues[self.books[0]]
        minorIndex = 0

        for i in range(1, len(self.books)):
            if bookValues[self.books[i]] < minorValue:
                minorValue = bookValues[self.books[i]]
                minorIndex = i

        if minorValue < value:
            return minorIndex

        return -1

    def sendBooks(self, bookValues):
        booksToSend = []

        for i in range(min(len(self.books), self.nBooksPerSecond)):
            booksToSend += [i]

        for i in range(min(len(self.books), self.nBooksPerSecond), len(self.books)):
            indexToReplace = self.biggerThanMinor(i, booksToSend) #returns the index of the minor value if smaller then the value of the current i, -1 otherwise
            if indexToReplace != -1:
                booksToSend[indexToReplace] = i

        for i in booksToSend: #So we don't send the same book again
            bookValues[i] = 0
            self.books.remove(i)

        self.sentBooks += booksToSend

