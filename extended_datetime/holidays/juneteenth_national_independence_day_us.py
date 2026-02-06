from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class JuneteenthNationalIndependenceDayUS(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 2:
            return False

        if date_to_check.day == 19:
            return True

        if date_to_check.day == 18 and date_to_check.isoweekday() == 5:
            return True

        if date_to_check.day == 20 and date_to_check.isoweekday() == 1:
            return True

        return False
