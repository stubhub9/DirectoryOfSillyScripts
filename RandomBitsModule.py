#!/usr/bin/python3
# Broken hashbang on line 2. # !/usr/env python3

#  Makes the script an .exe on BSD Unix [if \n]; just a comment otherwise.

#  Python Module Exploratory; with definitions, scripts, 


#  Managed Attributes
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value
    
    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:
    age = LoggedAgeAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday (self):
        self.age += 1


#  Dynamic Lookups
import os

class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:
    size = DirectorySize()          #Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname      #Regular instance attribute
#>>s = Directory('songs') matches local Songs dir





#  A couple simple descriptor classes.
class Ten:
    """ This class is a DESCRIPTOR, that always returns 10. """
    def __get__(self, obj, objtype=None):
        return 10
    

class A:
    x=5         #regular class attribute
    y=Ten()     # DESCRIPTOR INSTANCE
