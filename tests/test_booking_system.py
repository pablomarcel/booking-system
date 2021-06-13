#import booking_system.booking_system
import booking_system.ProcessingClasses
import booking_system.DataClasses
# import booking_system.IOClasses
import pandas as pd
from pandas._testing import assert_frame_equal
import re

# Validate if a package can be shipped

def test_validate_booking_1():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Dangerous', 5, 120, '07/01/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.validate_booking(book1) == True
    pass

def test_validate_booking_2():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Dangerous', 5, 125, '07/01/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.validate_booking(book1) == False
    pass

def test_validate_booking_3():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Dangerous', 10, 120, '07/01/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.validate_booking(book1) == False
    pass

def test_validate_booking_4():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Dangerous', 10, 125, '07/01/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.validate_booking(book1) == False
    pass

def test_validate_booking_5():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Dangerous', 5.0, 120.0, '07/01/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.validate_booking(book1) == True
    pass

def test_generate_booking_quote_1():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Dangerous', 5.0, 120.0, '07/01/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.generate_booking_quote(book1) == (False, True, True, True, False)
    pass

def test_generate_booking_quote_2():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Non-dangerous', 5.0, 120.0, '07/01/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.generate_booking_quote(book1) == (False, True, True, False, False)
    pass

def test_generate_booking_quote_3():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Dangerous', 5.0, 120., '06/13/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.generate_booking_quote(book1) == (False, True, False, True, True)
    pass

def test_generate_booking_quote_4():
    objP1 = booking_system.DataClasses.Customer('Pablo', 'Marcel')
    objPac1 = booking_system.DataClasses.Package('Non-dangerous', 5.0, 120.0, '06/13/21')
    book1 = booking_system.DataClasses.Booking(objP1, objPac1)
    assert booking_system.ProcessingClasses.FileProcessor.generate_booking_quote(book1) == (True, True, False, False, True)
    pass
