import sys
import pyfiglet
import pandas as pd
import numpy as np
from tabulate import tabulate
import dateutil
import datetime
import re
from IOClasses import UserSelection as us
from IOClasses import IO as io


result = pyfiglet.figlet_format("b o o k i n g s", font="slant")
strStatus = ""

# Main Body of Script  ------------------------------------------------------ #

if __name__ == "__main__":

    while True:

        print(result)
        print("Menu of Options")
        print(io.get_menu(1))
        print(io.get_menu(2))
        print(io.get_menu(3))
        print(io.get_menu(4))
        print(io.get_menu(5))
        print(io.get_menu(6))
        print(io.get_menu(7))
        print()

        # menu printed

        strChoice = io.input_menu_choice()  # Get menu option

        s = us()
        s.switch(
            strChoice
        )  # Calls the UserSelection class to handle the tasks in the menu

        io.input_press_to_continue(strStatus)
        continue  # to show the menu
