from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class VeteransDayUS(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 11:
            return False

        if date_to_check.day == 11:
            return True

        if date_to_check.day == 10 and date_to_check.isoweekday() == 5:
            return True

        if date_to_check.day == 12 and date_to_check.isoweekday() == 1:
            return True

        return False
