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
from DataClasses import BookingQuote as BQ
from DataClasses import Shipping as Ship


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

        booking = Bk(
            Cus(firstName, lastName), Pac(contents, weight, volume, deliveryDate)
        )

        # Tests to see if the booking is possible. That is, weight less than 10kg
        # and volume less than 125m3

        isPossible = Fp.validate_booking(booking)

        if isPossible:

            # creates a blank dataframe

            df = IO.get_options_db()
            dframe = df[(df.ShippingMethod == 123)]
            new_df = dframe.copy()

            # clears up the helper options.csv file

            Fp.update_options_csv(new_df)

            # creates blank dictionaries

            options_dict = dict()
            new_dict = dict()

            # generates the booking options.
            # calls the generate_booking_quote method
            # and gets a tuple in return.
            # the tuple contains boolean values for
            # each variable

            air, truck, ocean, dangerous, urgent = Fp.generate_booking_quote(booking)

            # creates a shipping options dictionary

            options_dict = {"air": air, "truck": truck, "ocean": ocean}

            # the shipping options dictionary is filtered out by the
            # shipping options that are actually possible (boolean value = True)

            new_dict = {k: v for k, v in options_dict.items() if v == True}

            for k, v in new_dict.items():
                if k == "air":
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

                elif k == "truck":

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

                elif k == "ocean":

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

            # displays the shipping options to the user
            # so that the user can decide which
            # shipping option to book

            df_options = IO.get_options_db()
            new_df_options = df_options.copy()

            print("The possible Shipping Options are: ")

            print(
                tabulate(
                    new_df_options, headers="keys", tablefmt="psql", showindex=True
                )
            )

            # trigger event to ask for user input

            strChoice = IO.input_booking_choice()

            # selected shipping method

            new_df_options = new_df_options.filter(like=strChoice, axis=0)

            selected_df = new_df_options.copy()

            # prints the user selected shipping option

            print("Selected Shipping Option is: ")

            print(
                tabulate(selected_df, headers="keys", tablefmt="psql", showindex=False)
            )

            # trigger event for appending to bookings csv file

            # reads the selected Shipping Option from a dataframe

            shipping_method = selected_df.iat[0, 0]
            cost = selected_df.iat[0, 1]

            # creates a Shipping object

            shipping = Ship(shipping_method, cost)

            # creates a BookingQuote Object

            booking_quote = BQ(
                Cus(firstName, lastName),
                Pac(contents, weight, volume, deliveryDate),
                Ship(shipping_method, cost),
            )

            # trigger event to append booking quote to bookings csv file

            # Process booking_quote

            IO.add_booking_quote(booking_quote)

        else:

            # if the booking is not possible according to the rules
            # the user is notified
            print("Booking Not Possible. Try Again! ")

        pass

    def case_2(self):
        """User selected Display all Bookings"""
        # trigger an action

        IO.print_all_bookings(IO.get_bookings_db())

        pass

    def case_3(self):
        """User selected Display Cost Statistics"""

        df = IO.get_bookings_db()
        df = df[["cost"]]
        dframe = df.copy()

        print(
            tabulate(dframe.describe(), headers="keys", tablefmt="psql", showindex=True)
        )

        pass

    def case_4(self):
        """User selected Display Shipping Option Statistics"""

        df = IO.get_bookings_db()
        df = df[["shippingOption"]]
        dframe = df.copy()

        print(
            tabulate(dframe.describe(), headers="keys", tablefmt="psql", showindex=True)
        )

        pass

    def case_5(self):
        """User selected Display Weight Statistics"""

        df = IO.get_bookings_db()
        df = df[["weight"]]
        dframe = df.copy()

        print(
            tabulate(dframe.describe(), headers="keys", tablefmt="psql", showindex=True)
        )
        pass

    def case_6(self):
        """User selected Display Volume Statistics"""

        df = IO.get_bookings_db()
        df = df[["volume"]]
        dframe = df.copy()

        print(
            tabulate(dframe.describe(), headers="keys", tablefmt="psql", showindex=True)
        )
        pass

    def case_7(self):
        """User selected Exit"""

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
            return "3) Display Cost Statistics about all Bookings"

        def four():
            return "4) Display Shipping Option Statistics about all Bookings"

        def five():
            return "5) Display Weight Statistics about all Bookings"

        def six():
            return "6) Display Volume Statistics about all Bookings"

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
    def input_booking_choice():
        """Gets the Booking choice from a user
        :param: None
        :return: string
        """

        while True:
            try:
                choice = str(
                    input("Which Booking Option would you like? Enter Number Option - ")
                )
                if choice not in ["0", "1", "2"]:
                    raise ValueError(
                        "Choice not an option, possible values are 0, 1, 2"
                    )
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

    @staticmethod
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
        """Reads the helper options.csv file and puts it in a pandas dataframe
        :param: None
        :return df: (Data Frame) a pandas dataframe
        """

        df = pd.read_csv("options.csv")

        return df

    @staticmethod
    def add_booking_quote(booking_quote):
        """Writes a new row to the bookings.csv file.
        This method is used when the user decides to add a new record to the csv
        :param df: (Pandas DataFrame) DataFrame containing bookings information
        :return: nothing
        """
        df = IO.get_bookings_db()
        bookingId = Fp.generate_booking_id(df)
        firstName = booking_quote.first_name
        lastName = booking_quote.last_name
        contents = booking_quote.content
        weight = booking_quote.weight
        volume = booking_quote.volume
        deliveryDate = booking_quote.delivery_date
        shippingOption = booking_quote.shipping_method
        cost = booking_quote.cost

        df = Fp.append_row(
            df,
            bookingId,
            firstName,
            lastName,
            contents,
            weight,
            volume,
            deliveryDate,
            shippingOption,
            cost,
        )

        Fp.append_to_csv(df)

        pass

    @staticmethod
    def print_all_bookings(dframe):
        """Displays all employees
        :param dframe: (Pandas DataFrame) a Pandas DataFrame containing all employee info.
        :return: nothing
        """

        print("These are all the Booking Quotes so far: ")

        df = dframe.copy()

        df["deliveryDate"] = pd.to_datetime(df["deliveryDate"])

        print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
