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
        generate_booking_quote(booking): -> (list of Boolean)
        update_csv(dframe): -> Nothing
        update_options_csv(dframe): -> Nothing
        generate_booking_id(dframe): -> (Integer)
        append_option_row(df, method, cost): -> Nothing
        append_option_to_csv(df): -> Nothing
        append_row(df,
                id,
                first,
                last,
                contents,
                weight,
                volume,
                deliveryDate,
                shippingOption,
                cost): -> (DataFrame)

    """

    @staticmethod
    def validate_booking(booking):
        """validates a booking. This method tells whether or not the shipping is possible
        :param booking: (object) object that represents a booking
        :return: (bool) with status of success status
        """

        # initializes variables

        success_status = False
        heavy = False
        large = False
        contents = booking.content
        weight = booking.weight
        volume = booking.volume
        del_date = booking.delivery_date

        # changes variable status according to the rules

        if weight >= 10:
            heavy = True

        if volume >= 125:
            large = True

        if heavy == True:
            success_status = False
        elif large == True:
            success_status = False
        else:
            success_status = True

        return success_status

    @staticmethod
    def generate_booking_quote(booking):
        """Generate a booking quote if the package can be shipped
        :param booking: (object) object that represents a booking
        :return air: (Boolean) tells if air shipment is possible or not
        :return truck: (Boolean) tells if truck shipment is possible or not
        :return ocean: (Boolean) tells if ocean shipment is possible or not
        :return dangerous: (Boolean) tells if the package is dangerous or not
        :return urgent: (Boolean) tells if the package is urgent or not
        """

        lst_shipping = []
        dangerous = False
        urgent = False
        air = False
        ocean = False
        truck = True

        del_date = booking.delivery_date

        dt_obj = datetime.strptime(del_date, "%m/%d/%y")

        date = datetime.today().replace(microsecond=0)

        delta = dt_obj - date

        day_delta = int(delta.days)

        # Determines if the shippment is urgent

        if day_delta < 3:
            urgent = True

        contents = booking.content

        if contents == "Dangerous":
            dangerous = True

        if dangerous == False and urgent == True:
            air = True

        if (dangerous == False and urgent == False) or (
            dangerous == True and urgent == False
        ):
            ocean = True

        return air, truck, ocean, dangerous, urgent

    @staticmethod
    def update_csv(dframe):
        """Writes a DataFrame to the bookings.csv file.
        This method is used when the user decides to add a row
        :param dframe: (Pandas DataFrame) DataFrame containing bookings information
        :return: nothing
        """

        dframe.to_csv("bookings.csv", index=False)

    @staticmethod
    def update_options_csv(dframe):
        """Writes the Shipping Options DataFrame to a temporary options.csv file.
        The options.csv is a helper file that temporarily stores
        a list of shipping options while working on a single booking.
        This method is used when the user decides to file a booking
        :param dframe: (Pandas DataFrame) DataFrame containing shipping options
        :return: nothing
        """

        dframe.to_csv("options.csv", index=False)

    @staticmethod
    def generate_booking_id(dframe):
        """Generates unique booking id for the next booking to be added
        :param dframe: (Pandas DataFrame) DataFrame containing bookings information
        :return next_id: (Integer) Next ID to be used for a booking record
        """
        max_id = dframe["BookingID"].max()
        next_id = max_id + 1

        return next_id

    @staticmethod
    def append_option_row(df, method, cost):
        """Generates a row of data to be appended to a pandas DataFrame
        :param dframe: (Pandas DataFrame) DataFrame containing bookings information
        :param method: (String) Shipping Method
        :param cost: (Float) Cost
        :return df: (Pandas DataFrame) a new Pandas DataFrame to be written to a csv
        """

        new_row = {
            "ShippingMethod": method,
            "Cost": cost,
        }

        # append row to the dataframe

        df = df.append(new_row, ignore_index=True)

        return df

    @staticmethod
    def append_options_to_csv(df):
        """Writes to the options.csv
        :param df: (Pandas DataFrame) DataFrame containing bookings information
        :return: nothing
        """

        df.to_csv("options.csv", index=False)

    @staticmethod
    def append_row(
        df,
        id,
        first,
        last,
        contents,
        weight,
        volume,
        deliveryDate,
        shippingOption,
        cost,
    ):
        """Generates a row of data to be appended to a pandas DataFrame
        :param dframe: (Pandas DataFrame) DataFrame containing bookings information
        :param id: (Integer) Next ID to be used for a booking record
        :param first: (String) First Name
        :param last: (String) Last Name
        :param contents: (String) The contents of the package
        :param weight: (Float) Weight
        :param Volume: (Float) Volume
        :param deliveryDate: (String) Delivery Date
        :param shippingOption: (String) Shipping Option
        :param cost: (Float) Cost
        :return df: (Pandas DataFrame) a new Pandas DataFrame to be written to a csv
        """

        new_row = {
            "BookingID": id,
            "firstName": first,
            "lastName": last,
            "contents": contents,
            "weight": weight,
            "volume": volume,
            "deliveryDate": deliveryDate,
            "shippingOption": shippingOption,
            "cost": cost,
        }

        # append row to the dataframe

        df = df.append(new_row, ignore_index=True)

        return df

    @staticmethod
    def append_to_csv(df):
        """Writes a new DataFarme to the csv file.
        This method is used when the system determines it is ok to write to teh
        bookings.csv file
        :param df: (Pandas DataFrame) DataFrame containing employee information
        :return: nothing
        """

        df.to_csv("bookings.csv", index=False)



