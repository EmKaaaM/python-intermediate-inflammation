"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np




def attach_names(data, names):
    """Create datastructure containing patient records."""
    assert len(data) == len(names)
    output = []

    for data_row, name in zip(data, names):
        output.append({'name': name,
                       'data': data_row})

    return output
    

def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    
   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    
    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    
   :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
   :returns: An array of minimum values of measurements for each day.
    
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    
    if not isinstance(data, np.ndarray):
        raise TypeError('data should be a ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflammation array should be 2-dimensional')
    
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    
    maxima = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / maxima[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return self.value



class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)

        self.observations = []
        ### MODIFIED START ###
        if observations is not None:
            self.observations = observations
        ### MODIFIED END ###

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(value, day)

        self.observations.append(new_observation)
        return new_observation


class Doctor(Person):
    "Doctor with many patients"
    def __init__(self, name):
        self.name = name
        self.patients = []
        
    def add_patient(self, new_patient):
        for patient in self.patients:
            if patient.name == new_patient.name:
                return
        self.patients.append(new_patient)
            
    
    def __str__(self):
        return self.name + " responsible for " + self.patients
    

class Book:
    "A test class for a book"
    def __init__(self, name, author):
         super().__init__(name)
         self.author = author
         
    def __str__(self):
        return self.name + " by " + self.author
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def by_author(self, author):
        matches = []
        for book in self.books:
            if book.author == author:
                matches.append(book)

        if not matches:
            raise KeyError('Author does not exist')

        return matches
        
    @property
    def titles(self):
        titles = []
        for book in self.books:
            titles.append(book.title)

        return titles

    @property
    def authors(self):
        authors = []
        for book in self.books:
            if book.author not in authors:
                authors.append(book.author)

        return authors    

    def union(self, other):
        books = []
        for book in self.books:
            if book not in books:
                books.append(book)

        for book in other.books:
            if book not in books:
                books.append(book)

        return Library(books)
        
        
        
