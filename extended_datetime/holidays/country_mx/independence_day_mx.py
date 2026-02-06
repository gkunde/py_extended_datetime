from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class IndependenceDayMX(HolidayBase):

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 9 and date_to_check.day == 16:
            return True

        return False
