import unittest
from datetime import datetime

from extended_datetime.extended_datetime import ExtendedDateTime
from extended_datetime.holidays.new_years_day import NewYearsDay


class Test_ExtendedDateTime(unittest.TestCase):

    # There are no tests for date_add using units less than months. All other
    # time units make use of the timedelta library's calculations.

    def test_date_add_years(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertEqual(o.date_add(years=1), datetime(2001, 1, 1, 0, 0, 0))

    def test_date_add_months(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertEqual(o.date_add(months=1), datetime(2000, 2, 1, 0, 0, 0))

    def test_date_add_months_from_base(self):

        o = ExtendedDateTime(2000, 1, 31)

        self.assertEqual(o.date_add(months=1), datetime(2000, 2, 29, 0, 0, 0))
        self.assertEqual(o.date_add(months=2), datetime(2000, 3, 31, 0, 0, 0))
        self.assertEqual(o.date_add(months=3), datetime(2000, 4, 30, 0, 0, 0))

    def test_date_add_months_chained(self):

        # Example of when chaining each calculation from the previous

        o = ExtendedDateTime(2000, 1, 31)

        # This will arrive at the 29th since the 2nd month of the year does not have 31 days
        n = o.date_add(months=1)
        self.assertEqual(n, datetime(2000, 2, 29, 0, 0, 0))

        # This will carry the 29th since the 3rd month of the year does have at least 29 days.
        n = n.date_add(months=1)
        self.assertEqual(n, datetime(2000, 3, 29, 0, 0, 0))

    def test_date_add_days(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertEqual(o.date_add(days=1), datetime(2000, 1, 2))

    def test_date_add_hours(self):

        o = ExtendedDateTime(2000, 1, 1, 0, 0, 0)

        self.assertEqual(o.date_add(hours=1), datetime(2000, 1, 1, 1, 0, 0, 0))

    def test_is_leap_year(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertTrue(o.is_leap_year())

        o = ExtendedDateTime(1999, 1, 1)

        self.assertFalse(o.is_leap_year())

    def test_is_business_day(self):

        o = ExtendedDateTime(2000, 1, 1)

        self.assertFalse(o.is_business_day())

        o = ExtendedDateTime(2000, 1, 5)

        self.assertTrue(o.is_business_day())

    def test_is_business_day_custom(self):

        o = ExtendedDateTime(2000, 1, 2)

        # Using -1 as it cannot be used to represent a weekday
        self.assertTrue(o.is_business_day(weekend_weekdays=(-1, )))

    def test_is_business_day_holiday(self):

        h = NewYearsDay()
        o = ExtendedDateTime(2010, 1, 1)

        self.assertTrue(o.is_business_day())
        self.assertFalse(o.is_business_day(holiday_schedules=[h, ]))
