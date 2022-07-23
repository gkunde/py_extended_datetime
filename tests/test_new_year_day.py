import unittest
from datetime import datetime

from extended_datetime.holidays.new_years_day import NewYearsDay


class Test_NewYearsDay(unittest.TestCase):

    def test_check_date(self):

        o = NewYearsDay()

        self.assertTrue(o.check_date(datetime(2000, 1, 1)))
        self.assertFalse(o.check_date(datetime(2000, 1, 2)))
