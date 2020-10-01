# Start of script -----------------------------------------------#
"""
Created on Tue Sep 29 15:20:00 2020

@author: David Brink and Bill Roth
"""
# Imports -------------------------------------------------------#

import datetime


# class definitions----------------------------------------------#

class Person:

    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.dateOfBirth = datetime.datetime(1900, 1, 1)

    # ------------------- Begin Getter/Setter Function Section --------------------
    # Function to return the value of the "firstName" attribute
    def getFirstName(self):
        return self.firstName

    # Function to set the value of the "firstName" attribute
    def setFirstName(self, firstName):
        self.firstName = firstName

    # Function to return the value of the "lastName" attribute
    def getLastName(self):
        return self.lastName

    # Function to set the value of the "lastName" attribute
    def setLastName(self, lastName):
        self.lastName = lastName

    # Function to return the value of the "dateOfBirth" attribute
    def getDateOfBirth(self):
        return self.dateOfBirth

    # Function to set the value of the "dateOfBirth" attribute
    def setDateOfBirth(self, year, month, day):
        self.dateOfBirth = datetime.datetime(year, month, day)

    # -------------------- End Getter/Setter Function Section ---------------------

    # __str__


class Actor(Person):

    def __init__(self):
        super().__init__()
        self.nationality = ""
        self.bio = ""
        self.filmography = []

    # ------------------- Begin Getter/Setter Function Section --------------------
    # Function to return the value of the "nationality" attribute
    def getNationality(self):
        return self.nationality

    # Function to set the value of the "nationality" attribute
    def setNationality(self, nationality):
        self.nationality = nationality

    # Function to return the value of the "bio" attribute
    def getBio(self):
        return self.bio

    # Function to set the value of the "bio" attribute
    def setBio(self, bio):
        self.bio = bio

    # Function to return the value of the "filmography" attribute
    def getFilmography(self):
        return self.filmography

    # Function to set the value of the "filmography" attribute
    def setFilmography(self, filmography):
        self.filmography = filmography
    # -------------------- End Getter/Setter Function Section ---------------------

    def __str__(self):
        stringToReturn = "{0} {1}".format(self.firstName, self.lastName)
        return stringToReturn




class Movie:

    def __init__(self):
        self.title = ""
        self.genre = []
        self.year = 1900
        self.review = ""
        self.actors = []
        self.watchCount = 0
        self.borrowedFlag = False
        self.borrower = Person()

    # ------------------- Begin Getter/Setter Function Section --------------------
    # Function to return the value of the "title" attribute
    def getTitle(self):
        return self.title

    # Function to set the value of the "title" attribute
    def setTitle(self, title):
        self.title = title

    # Function to return the value of the "genre" attribute
    def getGenre(self):
        return self.genre

    # Function to set the value of the "genre" attribute
    def setGenre(self, genre):
        self.genre = genre

    # Function to return the value of the "year" attribute
    def getYear(self):
        return self.year

    # Function to set the value of the "year" attribute
    def setYear(self, year):
        self.year = year

    # Function to return the value of the "review" attribute
    def getReview(self):
        return self.review

    # Function to set the value of the "review" attribute
    def setReview(self, review):
        self.review = review

    # Function to return the value of the "actors" attribute
    def getActors(self):
        return self.actors

    # Function to set the value of the "actors" attribute
    def setActors(self, actors):
        self.actors = actors

    # Function to return the value of the "watchCount" attribute
    def getWatchCount(self):
        return self.watchCount

    # Function to set the value of the "watchCount" attribute
    def setWatchCount(self, watchCount):
        self.watchCount = watchCount

    # Function to return the value of the "borrowedFlag" attribute
    def getBorrowedFlag(self):
        return self.borrowedFlag

    # Function to set the value of the "borrowedFlag" attribute
    def setBorrowedFlag(self, borrowedFlag):
        self.borrowedFlag = borrowedFlag

    # Function to return the value of the "borrower" attribute
    def getBorrower(self):
        return self.borrower

    # Function to set the value of the "borrower" attribute
    def setBorrower(self, borrower):
        self.borrower = borrower

    # -------------------- End Getter/Setter Function Section ---------------------

    # --------------------- Begin Function Definition Section ---------------------

    # increase movie count
    def incrementWatchCount(self, numberToIncrementBy):
        self.watchCount += numberToIncrementBy

    def checkIn(self):
        self.borrowedFlag = False
        self.borrower = None

    def checkOut(self, personCheckingOut):
        self.borrowedFlag = True
        self.borrower = personInput

    def __str__(self):
        genreToReturn = ""
        for genre in self.genre:
            if len(genreToReturn) > 0:
                genreToReturn += ", "
            genreToReturn += genre

        actorsToReturn = ""
        for actor in self.actors:
            if len(actorsToReturn) > 0:
                actorsToReturn += "\n"
            actorsToReturn += "\t" + str(actor)

        stringToReturn = "Movie: {0} \t Year: {1} \n Genre: {2} \n List of Actors: \n {3}".format(self.title, self.year,
                                                                                                  genreToReturn,
                                                                                                  actorsToReturn)
        return stringToReturn

    # ---------------------- End Function Definition Section ----------------------
    #


# End Class Definitions ---------------------------------------------------------------#


def TestMovieClasses():
    testActor1 = Actor()
    testActor1.setFirstName("Adam")
    testActor1.setLastName("Driver")
    testActor1.setDateOfBirth(1971,3,10)

    testActor2 = Actor()
    testActor2.setFirstName("Jon")
    testActor2.setLastName("Hamm")
    testActor2.setDateOfBirth(1971,3,10)

    testMovie = Movie()
    testMovie.setTitle("The Report")
    testMovie.setYear(2019)
    testMovie.setGenre(["Thriller", "Crime", "Drama"])
    testMovie.getActors().append(testActor1)
    testMovie.getActors().append(testActor2)

    print(testMovie)

TestMovieClasses()
