from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class NewYearsDay(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 1 and date_to_check.day == 1:
            return True

        return False
