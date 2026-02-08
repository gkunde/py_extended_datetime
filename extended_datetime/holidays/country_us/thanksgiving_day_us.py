from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class ThanksgivingDayUS(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 11:
            return False

        if date_to_check.isoweekday() == 4 and 22 <= date_to_check.day and date_to_check.day <= 28:
            return True

        return False
