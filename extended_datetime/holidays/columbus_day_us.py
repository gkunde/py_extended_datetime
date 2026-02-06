from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class ColumbusDayUS(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 10:
            return False

        if date_to_check.isoweekday() == 1 and 8 <= date_to_check.day and date_to_check.day <= 14:
            return True

        return False
