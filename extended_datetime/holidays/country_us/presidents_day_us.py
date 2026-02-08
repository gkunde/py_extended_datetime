from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class PresidentsDayUS(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 2:
            return False

        if date_to_check.isoweekday() == 1 and 15 <= date_to_check.day and date_to_check.day <= 21:
            return True

        return False
