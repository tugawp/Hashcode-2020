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
<<<<<<< HEAD

    def biggerThanMinor(self, value):
        minorValue = books
        minorIndex = -1
        
        for 



        return -1

    def sendBooks(self):
        booksToSend = []

        for i in range(nBooksPerSecond):
                booksToSend += [i]
        
        for i in range(end, nBooks):
            indexToReplace = biggerThanMinor(i, booksToSend)
            if indexToReplace != -1:
                booksToSend[indexToReplace] = i
=======
>>>>>>> 12a60fafaffc69051f13fccf2116e0334d528f21
