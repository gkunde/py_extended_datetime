import unittest
from datetime import datetime

from extended_datetime.extended_datetime import ExtendedDateTime


class Test_ExtendedDateTime(unittest.TestCase):

    # There are no tests for date_add using units less than months. All other
    # time units make use of the timedelta library's calculations.

    def test_date_add_years(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertEqual(o.date_add(years=1), datetime(2001, 1, 1, 0, 0, 0))
        self.assertEqual(o.date_add(years=-1), datetime(1999, 1, 1, 0, 0, 0))

    def test_date_add_months(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertEqual(o.date_add(months=1), datetime(2000, 2, 1, 0, 0, 0))

    def test_date_add_months_from_base(self):

        o = ExtendedDateTime(2000, 1, 31)

        self.assertEqual(o.date_add(months=1), datetime(2000, 2, 29, 0, 0, 0))
        self.assertEqual(o.date_add(months=2), datetime(2000, 3, 31, 0, 0, 0))
        self.assertEqual(o.date_add(months=3), datetime(2000, 4, 30, 0, 0, 0))
        self.assertEqual(o.date_add(months=6), datetime(2000, 7, 31, 0, 0, 0))
        self.assertEqual(o.date_add(months=11), datetime(2000, 12, 31, 0, 0, 0))

        self.assertEqual(o.date_add(months=-1), datetime(1999, 12, 31, 0, 0, 0))
        self.assertEqual(o.date_add(months=-2), datetime(1999, 11, 30, 0, 0, 0))
        self.assertEqual(o.date_add(months=-6), datetime(1999, 7, 31, 0, 0, 0))
        self.assertEqual(o.date_add(months=-11), datetime(1999, 2, 28, 0, 0, 0))
    
    def test_date_add_months_long_range(self):

        o = ExtendedDateTime(2000, 1, 1, 0, 0 ,0)

        self.assertEqual(o.date_add(months=12), datetime(2001, 1, 1, 0, 0, 0))
        self.assertEqual(o.date_add(months=13), datetime(2001, 2, 1, 0, 0, 0))
        self.assertEqual(o.date_add(months=15), datetime(2001, 4, 1, 0, 0, 0))
        self.assertEqual(o.date_add(months=24), datetime(2002, 1, 1, 0, 0, 0))

        self.assertEqual(o.date_add(months=-12), datetime(1999, 1, 1, 0, 0, 0))
        self.assertEqual(o.date_add(months=-13), datetime(1998, 12, 1, 0, 0, 0))
        self.assertEqual(o.date_add(months=-15), datetime(1998, 10, 1, 0, 0, 0))
        self.assertEqual(o.date_add(months=-24), datetime(1998, 1, 1, 0, 0, 0))

    def test_date_add_months_chained(self):

        # Example of when chaining each calculation from the previous

        o = ExtendedDateTime(2000, 1, 31)

        # This will arrive at the 29th since the 2nd month of the year does not have 31 days
        n = o.date_add(months=1)
        self.assertEqual(n, datetime(2000, 2, 29, 0, 0, 0))

        # This will carry the 29th since the 3rd month of the year does have at least 29 days.
        n = n.date_add(months=1)
        self.assertEqual(n, datetime(2000, 3, 29, 0, 0, 0))

    def test_date_add_months_and_years(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertEqual(o.date_add(years=1, months=1), datetime(2001, 2, 1))
        self.assertEqual(o.date_add(years=1, months=-1), datetime(2000, 12, 1))

        self.assertEqual(o.date_add(years=-1, months=14), datetime(2000, 3, 1))
        self.assertEqual(o.date_add(years=1, months=-14), datetime(1999, 11, 1))

        self.assertEqual(o.date_add(years=2, months=14), datetime(2003, 3, 1))
        self.assertEqual(o.date_add(years=-2, months=-14), datetime(1996, 11, 1))

    def test_date_add_days(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertEqual(o.date_add(days=1), datetime(2000, 1, 2))

    def test_is_leap_year(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertTrue(o.is_leap_year())

        o = ExtendedDateTime(1999, 1, 1)

        self.assertFalse(o.is_leap_year())
