from datetime import datetime, timedelta
from typing import Iterable, Iterator, Optional

from extended_datetime.base.holiday_base import HolidayBase


class ExtendedDateTime(datetime):
    """
    Extend built-in datetime class with additional methods for common date
    calculations and other helpful properties.
    """

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

        # deep copy self by adding a 0-delta
        new_self = self + timedelta()

        if months:
            # normalize months, by reducing to years and months

            months_abs = abs(months)

            year_offset = months_abs // 12
            month_remaining = months_abs % 12

            # make sure years has been initialized with a numeric value
            years = years or 0

            if months < 0:
                years -= year_offset
                months = 0 - month_remaining

            else:
                years += year_offset
                months = month_remaining

        if years:

            new_year = new_self.year + years

            # For leap years, it becomes necassary to ensure that if the day
            # represents the end of the month, it is updated appropriately.
            new_days = min(
                self.day,
                self.end_of_month_day(new_year, new_self.month))

            # Creating a delta of only the parts that were modified.
            new_self += (datetime(new_year, new_self.month, new_days) -
                         datetime(new_self.year, new_self.month, new_self.day))

        if months:

            new_year = new_self.year

            new_month = new_self.month + months

            if new_month < 1:
                new_year -= 1

            if not new_month:
                new_month = 12
            elif new_month < 1:
                new_month = 12 + new_month

            # Make sure the new month's calculation does not overflow the
            # month's number of days.
            new_days = min(
                new_self.day,
                self.end_of_month_day(new_year, new_month))

            # Creating a delta of only the parts that were modified
            new_self += (datetime(new_year, new_month, new_days) -
                         datetime(new_self.year, new_self.month, new_self.day))

        # normalize by coalesce to 0 for values
        new_days = days or 0
        new_hours = hours or 0
        new_minutes = minutes or 0
        new_seconds = seconds or 0
        new_microseconds = microseconds or 0
        new_weeks = weeks or 0

        new_self += timedelta(
            days=new_days,
            hours=new_hours,
            minutes=new_minutes,
            seconds=new_seconds,
            microseconds=new_microseconds,
            weeks=new_weeks)

        return new_self

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

        if not year:
            year = self.year

        if not month:
            month = self.month

        end_of_month = 31

        if month in (4, 6, 9, 11, ):
            # Short months
            end_of_month = 30

        elif month == 2:
            # February
            end_of_month = 28

            if self.is_leap_year(year):
                # Leap Year
                end_of_month = 29

        return end_of_month

    def is_leap_year(self, year: Optional[int] = None) -> bool:
        """
        Identifies if the year datepart of the object is within a leap year.

        A leap year is defined as any year that is evenly divisable by 4, but
        not 100; or, evenly divisable by 4, 100, and 400.

        :param year: An optional parameter to test other year values.

        :returns: A boolean True indicates the year datepart is a leap year.
        """

        if not year:
            year = self.year

        if year % 4 == 0 and year % 100 != 0:
            return True

        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            return True

        return False

    def is_business_day(
            self,
            date_to_check: Optional[datetime] = None,
            holiday_schedules: Optional[Iterable[HolidayBase]] = None,
            weekend_weekdays: Optional[Iterable[int]] = None) -> bool:
        """
        Determine if the object's date is a traditional business day.

        :param date_to_check: Provide an alternative datetime object to the
            one in the object to check.

        :param holiday_schedules: A collection of BaseHoliday type objects
            that determine if a provided date is an observed holiday.

        :param weekend_weekdays: Provide an alternative set of weekdays to
            consider as weekends or non-business days. Defaults to Saturday
            and Sunday.
            (Zero based: Monday == 0 ... Sunday == 6)

        :returns: A Boolean to indicate the object is a business day.
        """

        if not date_to_check:
            date_to_check = self

        if not weekend_weekdays:
            weekend_weekdays = (5, 6, )

        if not holiday_schedules:
            holiday_schedules = []

        if date_to_check.weekday() in weekend_weekdays:
            return False

        for holiday in holiday_schedules:

            if holiday.check_date(date_to_check):
                return False

        return True
