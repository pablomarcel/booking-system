#import booking_system.booking_system
from unittest.mock import patch

import booking_system.ProcessingClasses
import booking_system.DataClasses
# import booking_system.IOClasses
import pandas as pd
# from booking_system.ProcessingClasses import FileProcessor as Fp
from pandas._testing import assert_frame_equal
import re
import mock
import builtins
import booking_system.DataCapture

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

# validate if the system generates correct shipping options

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

def test_generate_booking_id():
    df = pd.read_csv("src\\booking_system\\bookings.csv")

    assert booking_system.ProcessingClasses.FileProcessor.generate_booking_id(df) == 10000012

def test_customer():

    first = 'Beatrix'
    last = 'T'
    customer1 = booking_system.DataClasses.Customer(first,last)

    assert customer1.first_name == first
    assert customer1.last_name == last

def test_package():

    contents = 'Dangerous'
    weight = 5.0
    volume = 120.0
    deliveryDate = '07/01/21'
    package1 = booking_system.DataClasses.Package(contents, weight, volume, deliveryDate)

    assert package1.content == contents
    assert package1.weight == weight
    assert package1.volume == volume
    assert package1.delivery_date == deliveryDate

def test_booking():

    first = 'Beatrix'
    last = 'T'
    contents = 'Dangerous'
    weight = 5.0
    volume = 120.0
    deliveryDate = '07/01/21'
    customer1 = booking_system.DataClasses.Customer(first, last)
    package1 = booking_system.DataClasses.Package(contents, weight, volume, deliveryDate)
    booking1 = booking_system.DataClasses.Booking(customer1, package1)

    assert booking1.content == contents
    assert booking1.weight == weight
    assert booking1.volume == volume
    assert booking1.delivery_date == deliveryDate

def test_shipping():

    method = 'air'
    cost = '55'
    shipping1 = booking_system.DataClasses.Shipping(method, cost)

    assert shipping1.shipping_method == method
    assert shipping1.cost == cost

def test_booking_quote():

    first = 'Beatrix'
    last = 'T'
    contents = 'Dangerous'
    weight = 8.0
    volume = 10.0
    method = 'truck'
    cost = '55'
    deliveryDate = '07/01/21'
    customer1 = booking_system.DataClasses.Customer(first, last)
    package1 = booking_system.DataClasses.Package(contents, weight, volume, deliveryDate)
    booking1 = booking_system.DataClasses.Booking(customer1, package1)
    shipping1 = booking_system.DataClasses.Shipping(method, cost)

    booking_quote1 = booking_system.DataClasses.BookingQuote(customer1,package1,shipping1)

    assert booking_quote1.first_name == first
    assert booking_quote1.last_name == last
    assert booking_quote1.content == contents
    assert booking_quote1.shipping_method == method
    assert booking_quote1.cost == cost
    assert booking_quote1.delivery_date == deliveryDate
    assert booking_quote1.weight == weight
    assert booking_quote1.volume == volume

def test_capture_first_name():
    with mock.patch.object(builtins, 'input', lambda _: 'Albert'):
        assert booking_system.DataCapture.InputOutput.capture_first_name() == 'Albert'

def test_capture_last_name():
    with mock.patch.object(builtins, 'input', lambda _: 'King'):
        assert booking_system.DataCapture.InputOutput.capture_last_name() == 'King'

def test_capture_contents():
    with mock.patch.object(builtins, 'input', lambda _: 'Dangerous'):
        assert booking_system.DataCapture.InputOutput.capture_contents() == 'Dangerous'

def test_capture_weight():
    with mock.patch.object(builtins, 'input', lambda _: 1.0):
        assert booking_system.DataCapture.InputOutput.capture_weight() == 1.0

def test_capture_volume():
    with mock.patch.object(builtins, 'input', lambda _: 50.0):
        assert booking_system.DataCapture.InputOutput.capture_volume() == 50.0

def test_capture_delivery_date():
    with mock.patch.object(builtins, 'input', lambda _: '6/20/21'):
        assert booking_system.DataCapture.InputOutput.capture_delivery_date() == '6/20/21'




