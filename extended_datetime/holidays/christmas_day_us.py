from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class ChristmasDayUS(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 12:
            return False

        if date_to_check.day == 25:
            return True

        if date_to_check.day == 24 and date_to_check.isoweekday() == 5:
            return True

        if date_to_check.day == 26 and date_to_check.isoweekday() == 1:
            return True

        return False
