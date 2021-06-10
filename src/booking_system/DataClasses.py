if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else:
    pass

import sys
import pyfiglet
import pandas as pd
import numpy as np
from tabulate import tabulate
import dateutil
import datetime
import re

class Customer:
    """Stores data about a Customer:

    properties:
        first_name: (string) with the persons's first name

        last_name: (string) with the persons's last name
    methods:
        to_string() returns comma separated product data (alias for __str__())

    """

    # -- Constructor --
    def __init__(self, first_name, last_name):
        # -- Attributes --
        self.__first_name = first_name
        self.__last_name = last_name

    # -- Properties --
    @property
    def first_name(self):
        return str(self.__first_name).title()

    @first_name.setter
    def first_name(self, value):
        if not str(value).isnumeric():
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def last_name(self):
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value):
        if not str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.first_name + ',' + self.last_name

class Package:
    """Stores data about a Customer:

    properties:
        content: (string) with the package contents: dangerous or non dangerous
        weight: (string) with the package weight
        volume: (string) with the package volume
        delivery_date: (string) with the package delivery date

    methods:
        to_string() returns comma separated product data (alias for __str__())

    """

    # -- Constructor --
    def __init__(self, content, weight, volume, delivery_date):
        # -- Attributes --
        self.__content = content
        self.__weight = weight
        self.__volume = volume
        self.__delivery_date = delivery_date

    # -- Properties --
    @property
    def content(self):
        return str(self.__content).title()

    @content.setter
    def content(self, value):
        if not str(value).isnumeric():
            self.__content = value
        else:
            raise Exception("Contents cannot be numbers")

    @property
    def weight(self):
        return str(self.__weight).title()

    @weight.setter
    def weight(self, value):
        if not str(value).isnumeric():
            self.__weight = value
        else:
            raise Exception("Weight cannot be numbers")

    @property
    def volume(self):
        return str(self.__volume).title()

    @volume.setter
    def volume(self, value):
        if not str(value).isnumeric():
            self.__volume = value
        else:
            raise Exception("Volume cannot be numbers")

    @property
    def delivery_date(self):
        return str(self.__delivery_date).title()

    @delivery_date.setter
    def delivery_date(self, value):
        if not str(value).isnumeric():
            self.__delivery_date = value
        else:
            raise Exception("Delivery Date cannot be numbers")

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.content + ',' + self.weight


