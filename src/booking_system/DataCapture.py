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

class InputOutput:
    """Performs Input and Output tasks"""

    @staticmethod
    def capture_first_name():
        """Captures First Name
        :param:  None
        :return strText: (String) First Name
        """
        while True:
            try:
                strText = str(input("Enter First Name: ")).strip()
                if strText.isnumeric():
                    raise ValueError(
                        "First Name is Numeric. Enter a valid First Name: "
                    )
                elif strText == "":
                    raise ValueError("First Name is empty. Enter a valid First Name: ")
            except ValueError as e:
                print(e)
            else:
                break

        return strText

    @staticmethod
    def capture_last_name():
        """Captures Last Name
        :param:  None
        :return strText: (String) Last Name
        """
        while True:
            try:
                strText = str(input("Enter Last Name: ")).strip()
                if strText.isnumeric():
                    raise ValueError("Last Name is Numeric. Enter a valid Last name: ")
                elif strText == "":
                    raise ValueError("Last Name is empty. Enter a valid Last Name: ")
            except ValueError as e:
                print(e)
            else:
                break

        return strText

    def capture_contents():
        """Captures Contents
        :param:  None
        :return strText: (String) Package Contents/Description
        """
        while True:
            try:
                strText = str(
                    input("Enter Contents, Enter Dangerous if Dangerous: ")
                ).strip()
                if strText.isnumeric():
                    raise ValueError("Content is Numeric. Enter a valid content: ")
                elif strText == "":
                    raise ValueError("Content is empty. Enter a valid content: ")
            except ValueError as e:
                print(e)
            else:
                break

        return strText

    @staticmethod
    def capture_weight():
        """Captures Weight
        :param:  None
        :return strText: (String) Weight
        """
        while True:
            try:
                strText = float(input("Enter Weight: "))

            except ValueError:
                print("Not a number! Try again. ")
                continue
            else:
                break

        return strText

    @staticmethod
    def capture_volume():
        """Captures Volume
        :param:  None
        :return strText: (String) Volume
        """
        while True:
            try:

                strText = float(input("Enter Volume: "))

            except ValueError:
                print("Not a number! Try again. ")
                continue
            else:
                break

        return strText

    @staticmethod
    def capture_delivery_date():
        """Captures Delivery Date
        :param:  None
        :return strText: (String) Delivery Date
        """
        formt = "%m/%d/%y"
        while True:
            try:
                strText = str(
                    input("Enter Delivery Date, mm/dd/yy (%m/%d/%y): ")
                ).strip()
                res = bool(datetime.datetime.strptime(strText, formt))

            except ValueError as e:
                print(e)

            else:
                break

        return strText