import unittest
from speciallecture.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer  = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(2, len(l))