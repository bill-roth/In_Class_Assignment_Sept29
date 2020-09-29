# - something i don't know what it means ------------------------#
# -*- coding: utf-8 -*-
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
        self.dateOfBirth = datetime(1000, 1, 1)

    #__str__


class Actor(Person):

    def __init__(self):
        self.nationality = ""
        self.bio = ""
        self.filmography = []

    # include a method for resetting an attribute from a previously inputted value

    #__str__

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

    # getters and setters
        # set title, etc
        # also give review

    # increase movie count


    def checkIn(self):
        self.borrowedFlag = False
        self.borrower = None

    def checkOut(self,personInput):
        self.borrowedFlag = True
        self.borrower = personInput

    # __str__

    #
# End Class Definitions ---------------------------------------------------------------#
