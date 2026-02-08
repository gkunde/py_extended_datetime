from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class LaborDayUS(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 9:
            return False

        if date_to_check.isoweekday() == 1 and 1 <= date_to_check.day and date_to_check.day <= 7:
            return True

        return False
