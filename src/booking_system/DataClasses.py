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
        """Explicitly returns a string with this object's data"""
        return self.__str__()

    def __str__(self):
        """Implicitly returns a string with this object's data"""
        return self.first_name + "," + self.last_name


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
        return self.__weight

    @weight.setter
    def weight(self, value):
        if not str(value).isalpha():
            self.__weight = value
        else:
            raise Exception("Weight cannot be letters")

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if not str(value).isalpha():
            self.__volume = value
        else:
            raise Exception("Volume cannot be letters")

    @property
    def delivery_date(self):
        return str(self.__delivery_date)

    @delivery_date.setter
    def delivery_date(self, value):
        if not str(value).isnumeric():
            self.__delivery_date = value
        else:
            raise Exception("Delivery Date cannot be numbers")

    # -- Methods --
    def to_string(self):
        """Explicitly returns a string with this object's data"""
        return self.__str__()

    def __str__(self):
        """Implicitly returns a string with this object's data"""
        return f"{self.content},{self.weight},{self.volume},{self.delivery_date}"


class Booking:
    """Stores data about a single Booking:

    properties:
        customer: (object) object that represents the customer
        package: (object) object that represents the package

    methods:
        to_string() returns comma separated booking data (alias for __str__())

    """

    # -- Constructor --
    def __init__(self, customer, package):
        # -- Attributes --
        self.__customer = customer
        self.__package = package
        self.__content = package.content
        self.__weight = package.weight
        self.__volume = package.volume
        self.__delivery_date = package.delivery_date

    # -- Properties --
    @property
    def customer(self):
        return str(self.__customer)

    @customer.setter
    def customer(self, value):
        if not str(value).isnumeric():
            self.__customer = value
        else:
            raise Exception("Customer cannot be numbers")

    @property
    def package(self):
        return str(self.__package)

    @package.setter
    def package(self, value):
        if not str(value).isnumeric():
            self.__package = value
        else:
            raise Exception("Package cannot be numbers")

    @property
    def content(self):
        return str(self.__content)

    @content.setter
    def content(self, value):
        if not str(value).isnumeric():
            self.__content = value
        else:
            raise Exception("Content cannot be numbers")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if not str(value).isalpha():
            self.__weight = value
        else:
            raise Exception("Weight cannot be letters")

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if not str(value).isalpha():
            self.__volume = value
        else:
            raise Exception("Volume cannot be letters")

    @property
    def delivery_date(self):
        return str(self.__delivery_date)

    @delivery_date.setter
    def delivery_date(self, value):
        if not str(value).isnumeric():
            self.__delivery_date = value
        else:
            raise Exception("Delivery date cannot be numbers")

    # -- Methods --
    def to_string(self):
        """Explicitly returns a string with this object's data"""
        return self.__str__()

    def __str__(self):
        """Implicitly returns a string with this object's data"""
        return f"{self.customer},{self.package}"


class BookingQuote:
    """Stores data about a shipping options for a Booking:

    """

