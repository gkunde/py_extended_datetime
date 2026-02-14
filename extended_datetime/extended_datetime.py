"""
ExtendedDateTime class is to extend the built-in datetime class with methods
to perform localized date calculations.
"""
import calendar
from datetime import datetime, timedelta
from typing import Optional


class ExtendedDateTime(datetime):
    """
    Extend built-in datetime class with additional methods for common date
    calculations and other helpful properties.
    """

    def add_years(self, years: int) -> 'ExtendedDateTime':
        """
        Docstring for add_years

        :param years: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        _self = self + timedelta()

        _year = _self.year + years

        _, y = calendar.monthrange(_year, _self.month)

        return _self.replace(year=_year, day=min(_self.day, y))

    def add_months(self, months: int) -> 'ExtendedDateTime':
        """
        Docstring for add_months

        :param months: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        _self = self + timedelta()

        _self = _self.add_years(months // 12)

        _month = _self.month + (months % 12)

        _, y = calendar.monthrange(_self.year, _month)

        return _self.replace(month=_month, day=min(_self.day, y))

    def add_days(self, days: int) -> 'ExtendedDateTime':
        """
        Docstring for add_days

        :param days: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        return self + timedelta(days=days)

    def add_weeks(self, weeks: int) -> 'ExtendedDateTime':
        """
        Docstring for add_weeks

        :param weeks: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        return self + timedelta(weeks=weeks)

    def add_hours(self, hours: int) -> 'ExtendedDateTime':
        """
        Docstring for add_hours

        :param hours: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        return self + timedelta(hours=hours)

    def add_minutes(self, minutes: int) -> 'ExtendedDateTime':
        """
        Docstring for add_minutes

        :param minutes: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        return self + timedelta(minutes=minutes)

    def add_seconds(self, seconds: int) -> 'ExtendedDateTime':
        """
        Docstring for add_seconds

        :param seconds: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        return self + timedelta(seconds=seconds)

    def add_microseconds(self, microseconds: int) -> 'ExtendedDateTime':
        """
        Docstring for add_microseconds

        :param microseconds: Description
        :return: Description
        """

        # deep copy self by adding a 0-delta
        return self + timedelta(microseconds=microseconds)

    def date_add(
            self,
            years: Optional[int] = None,
            months: Optional[int] = None,
            days: Optional[int] = None,
            hours: Optional[int] = None,
            minutes: Optional[int] = None,
            seconds: Optional[int] = None,
            microseconds: Optional[int] = None,
            weeks: Optional[int] = None) -> 'ExtendedDateTime':
        """
        Add the provided values for each unit of time to the value stored in
        this ExtendedDateTime object.

        Note: Avoid chaining calculations. Use the same base object and
        increment the interval to the next desired value.

            example = ExtendedDateTime(2020, 1, 31)

            print(example.date_add(months=1)) # 2020-02-29 00:00:00
            print(example.date_add(months=2)) # 2020-03-31 00:00:00

            example = ExtendedDateTime(2020, 2, 29)

            print(example.date_add(years=1)) # 2021-02-28 00:00:00
            print(example.date_add(years=2)) # 2022-02-28 00:00:00
            print(example.date_add(years=3)) # 2023-02-28 00:00:00
            print(example.date_add(years=4)) # 2024-02-29 00:00:00

        :param years: A numeric value to increment the year attribute.

        :param months: A numeric value to increment the month attribute.

        :param days: A numeric value to increment the day attribute.

        :param hours: A numeric value to increment the hour attribute.

        :param minutes: A numeric value to increment the minute attribute.

        :param seconds: A numeric value to increment the second attribute.

        :param microseconds: A numeric value to increment the microsecond
            attribute.

        :param weeks: A numeric value to increment the day, month, and year
            attributes.

        :returns: A new instance of ExtendedDateTime with computed value.
        """

        return self \
            .add_years(years or 0) \
            .add_months(months or 0) \
            .add_days(days or 0) \
            .add_hours(hours or 0) \
            .add_minutes(minutes or 0) \
            .add_seconds(seconds or 0) \
            .add_microseconds(microseconds or 0) \
            .add_weeks(weeks or 0)

    def end_of_month_day(self, year: Optional[int] = None, month: Optional[int] = None) -> int:
        """
        Determines the last day of the month using the object's year and
        month dateparts.

        :param year: An option value to determine an end of month for a
            different year than this object's year value. 

        :param month: An option value to determine an end of month for a
            different month than this object's month value.

        :returns: The last day of the object's year and month
        """

        return calendar.monthrange(year or self.year, month or self.month)[1]

    def is_leap_year(self, year: Optional[int] = None) -> bool:
        """
        Identifies if the year datepart of the object is within a leap year.

        A leap year is defined as any year that is evenly divisable by 4, but
        not 100; or, evenly divisable by 4, 100, and 400.

        :param year: An optional parameter to test other year values.

        :returns: A boolean True indicates the year datepart is a leap year.
        """

        return calendar.isleap(year or self.year)
