import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read1(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        print(l)
        self.assertEqual(['value1A', ' value1B', ' value1C'], l[0])

    def test_read3(self):
        try:
            printer = CSVPrinter("sampl.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            pass