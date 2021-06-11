if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

import sys
import pyfiglet
import pandas as pd
import numpy as np
from tabulate import tabulate
import dateutil
from datetime import datetime
import re

class FileProcessor:
    """Processes data to and from a file and a list of objects:
    methods:
        validate_booking(booking): -> (Boolean)
        save_data_to_file(file_name,list_of_objects):
        read_data_from_file(file_name): -> (a list of objects)
    """

    @staticmethod
    def validate_booking(booking):
        """ validate a booking
        :param booking: (object) object that represents a booking
        :return: (bool) with status of success status
        """
        # how to translate the representation of an object as variables

        success_status = False
        heavy = False
        large = False
        contents = booking.content
        weight = booking.weight
        volume = booking.volume
        del_date = booking.delivery_date

        if weight >= 10:
            heavy = True

        if volume >= 125:
            large = True

        if heavy == True:
            success_status=False
        elif large == True:
            success_status=False
        else:
            success_status=True

        return success_status

    @staticmethod
    def generate_booking_quote(booking):
        """ Generate a booking quote if the package can be shipped
        :param booking: (object) object that represents a booking
        :return: (list) list of objects that represent shipping options
        """

        lst_shipping = []
        dangerous = False
        urgent = False
        air = False
        ocean = False
        truck = True

        del_date = booking.delivery_date

        dt_obj = datetime.strptime(del_date, '%m/%d/%y')

        date = datetime.today().replace(microsecond=0)

        delta = dt_obj - date

        day_delta = int(delta.days)

        if day_delta < 3:
            urgent = True

        contents = booking.content

        if contents == 'Dangerous':
            dangerous = True

        if dangerous == False and urgent == True:
            air = True

        if (dangerous == False and urgent == False) or (dangerous == True and urgent == False):

            ocean = True

        return air, truck, ocean


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



# class ValidateBooking:
#     """Validates a Booking:
#
#     properties:
#         booking: (object) object that represents a booking
#
#     methods:
#         to_string() returns comma separated booking data (alias for __str__())
#
#     """
#     # -- Constructor --
#     def __init__(self, booking):
#         # -- Attributes --
#         self.__booking = booking
