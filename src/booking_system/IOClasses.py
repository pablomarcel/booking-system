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


class UserSelection:
    """Handles User Selection Logic
    the class is used to implement a case-switch construct in python
    """

    def switch(self, strChoice):
        """Builds a function name based off user choice and triggers the actions"""

        default = "Incorrect Selection"
        return getattr(self, "case_" + str(strChoice), lambda: default)()

    def case_1(self):
        """User selected print a list of all employees"""
        # trigger an action
        pass

    def case_2(self):
        """User selected Print a list of employees currently employed"""
        # trigger an action
        pass

    def case_3(self):
        """User selected Print a list of employees who have left in the past month"""
        # trigger an action
        pass

    def case_4(self):
        """User selected Display a reminder to schedule annual review"""
        # trigger an action
        pass

    def case_5(self):
        """User selected Capture employee information"""
        # trigger an action
        pass

    def case_6(self):
        """User selected Delete record"""
        # trigger an action
        pass

    def case_7(self):
        """User selected Exit"""
        # trigger an action
        print("Goodbye ")

        sys.exit()

class IO:
    """Performs Input and Output tasks"""

    @staticmethod
    def get_menu(argument):
        """Uses dictionaries to display options to the user
        :param argument: (Integer) None
        :return: (String) the value of the switcher dictionary
        """

        def one():
            return "1) Capture Booking Information"

        def two():
            return "2) Display all Bookings"

        def three():
            return "3) Print a list of employees who have left in the past month"

        def four():
            return "4) Display reminder to schedule annual review"

        def five():
            return "5) Capture employee information"

        def six():
            return "6) Delete record"

        def seven():
            return "7) Exit"

        switcher = {
            1: one(),
            2: two(),
            3: three(),
            4: four(),
            5: five(),
            6: six(),
            7: seven(),
        }
        return switcher.get(argument, "Invalid Selection")

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from a user
        :param: None
        :return: string
        """

        while True:
            try:
                choice = str(
                    input("Which option would you like to perform? [1 to 7] - ")
                ).strip()
                if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                    raise ValueError("Choice not an option, enter 1, 2, 3, 4, 5, 6, 7")
            except ValueError as e:
                print(e)
            else:
                break
        print()  # Add an extra line for looks

        return choice

    @staticmethod
    def input_press_to_continue(optional_message=""):
        """Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input("Press the [Enter] key to continue.")