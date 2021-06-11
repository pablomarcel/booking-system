if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

import sys
import pyfiglet
import pandas as pd
import numpy as np
from tabulate import tabulate
import dateutil
import datetime
import re

class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)

    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

class Booking:
    """Stores data about a Booking:

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

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.customer + ',' + self.package
