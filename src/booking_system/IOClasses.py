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
from ProcessingClasses import FileProcessor as Fp
from DataClasses import Booking as Bk
from DataClasses import Customer as Cus
from DataClasses import Package as Pac

class UserSelection:
    """Handles User Selection Logic
    the class is used to implement a case-switch construct in python
    """

    def switch(self, strChoice):
        """Builds a function name based off user choice and triggers the actions"""

        default = "Incorrect Selection"
        return getattr(self, "case_" + str(strChoice), lambda: default)()

    def case_1(self):
        """User selected Book a Shipment"""

        (
            bookingID,
            firstName,
            lastName,
            fullName,
            contents,
            weight,
            volume,
            deliveryDate,
        ) = IO.capture_booking_data(IO.get_bookings_db())

        # instantiates an object of the booking class

        booking = Bk(Cus(firstName,lastName),Pac(contents,weight,volume,deliveryDate))

        print(booking.to_string())

        # Tests to see if the booking is possible. That is, weight less than 10kg
        # and volume less than 125m3

        isPossible = Fp.validate_booking(booking)

        if isPossible:

            # generates the booking options.
            # calls the method and gets a tuple in return
            # the tuple contains boolean values for
            # each variable

            options_dict = dict()
            new_dict = dict()

            air, truck, ocean, dangerous, urgent = Fp.generate_booking_quote(booking)

            options_dict={'air': air, 'truck': truck, 'ocean': ocean}

            # print(options_dict.items())

            new_dict = {k: v for k, v in options_dict.items() if v == True}

            for k, v in new_dict.items():
                if k == 'air':
                    cost1 = 10 * weight

                    highest = cost1

                    cost2 = 20 * volume

                    if cost2 > cost1:
                        highest = cost2

                    df = Fp.append_option_row(
                        IO.get_options_db(),
                        k,
                        highest,
                    )

                    Fp.append_options_to_csv(df)

                    pass

                elif k=='truck':

                    if urgent:

                        highest = 45

                    else:

                        highest = 25

                    df = Fp.append_option_row(
                        IO.get_options_db(),
                        k,
                        highest,
                    )

                    Fp.append_options_to_csv(df)

                    pass

                elif k=='ocean':

                    highest = 30

                    df = Fp.append_option_row(
                        IO.get_options_db(),
                        k,
                        highest,
                    )

                    Fp.append_options_to_csv(df)

                    pass
                else:

                    pass


            # print(new_dict)

            # print(Fp.generate_booking_quote(booking))

            # if air:
            #
            #     shipping = 'air'
            #
            #     cost1= 10*weight
            #
            #     highest = cost1
            #
            #     cost2= 20*volume
            #
            #     if cost2>cost1:
            #
            #         highest = cost2
            #
                # df = Fp.append_option_row(
                #     IO.get_options_db(),
                #     shipping,
                #     highest,
                # )
            #
            #     pass
            #
            # if ocean:
            #
            #     shipping = 'ocean'
            #
                # highest = 30
                #
                # df = Fp.append_option_row(
                #     IO.get_options_db(),
                #     shipping,
                #     highest,
                # )
            #
            #     pass
            #
            # if truck:
            #
            #     shipping = 'truck'
            #
                # if urgent:
                #
                #     highest = 45
                #
                # else:
                #
                #     highest = 25
                #
                # df = Fp.append_option_row(
                #     IO.get_options_db(),
                #     shipping,
                #     highest,
                # )
            #
            #     pass



        else:

            print('Booking Not Possible. Try Again! ')



        # generate a dataframe and print it to screen



        # df = Processor.append_row(
        #     IO.get_bookings_db(),
        #     employeeID,
        #     firstName,
        #     lastName,
        #     fullName,
        #     address,
        #     ssn,
        #     dateOfBirth,
        #     jobTitle,
        #     startDate,
        #     endDate,
        # )
        #
        # Processor.append_to_csv(df)

        pass



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
            return "1) Book a Shippment"


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


    @staticmethod
    def capture_booking_data(dframe):
        """Captures data for new Booking
        :param dframe: (Pandas DataFrame) a DataFrame with bookings info
        :return bookingID: (Integer) Unique Booking ID
        :return firstName: (String) First Name
        :return lastName: (String) Last Name
        :return fullName: (String) Full Name
        :return contents: (String) Contents
        :return weight: (float) Weight
        :return volume: (float) Volume
        :return deliveryDate: (String) Delivery Date
        """
        bookingID = Fp.generate_booking_id(dframe)
        firstName = IO.capture_first_name()
        lastName = IO.capture_last_name()
        fullName = firstName + " " + lastName
        contents = IO.capture_contents()
        weight = IO.capture_weight()
        volume = IO.capture_volume()
        deliveryDate = IO.capture_delivery_date()

        return (
            bookingID,
            firstName,
            lastName,
            fullName,
            contents,
            weight,
            volume,
            deliveryDate,
        )

    @staticmethod
    def capture_first_name():
        """Captures First Name
        :param:  None
        :return: Nothing
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
        :return: Nothing
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

    @staticmethod
    def capture_contents():
        """Captures Contents
        :param:  None
        :return strText: (String) Package Contents
        """
        while True:
            try:
                strText = str(input("Enter Contents, Enter Dangerous if Dangerous: ")).strip()
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
                # if strText.isalpha():
                #     raise ValueError(
                #         "Weight is alpha. Enter a valid Weight: "
                #     )
                # elif strText == "":
                #     raise ValueError("Weight is empty. Enter a valid Weight: ")
            except ValueError:
                print('Not a number! Try again. ')
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
                # if strText.isalpha():
                #     raise ValueError("Volume is alpha. Enter a valid Volume: ")
                # elif strText == "":
                #     raise ValueError("Volume is empty. Enter a valid Volume: ")
            except ValueError:
                print('Not a number! Try again. ')
                continue
            else:
                break

        return strText

    @staticmethod
    def capture_delivery_date():
        """Captures Date of Birth
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

    @staticmethod
    def get_bookings_db():
        """Reads the csv and puts it in a pandas dataframe
        :param: None
        :return df: (Data Frame) a pandas dataframe
        """

        df = pd.read_csv("bookings.csv")

        return df

    @staticmethod
    def get_options_db():
        """Reads the csv and puts it in a pandas dataframe
        :param: None
        :return df: (Data Frame) a pandas dataframe
        """

        df = pd.read_csv("options.csv")

        return df