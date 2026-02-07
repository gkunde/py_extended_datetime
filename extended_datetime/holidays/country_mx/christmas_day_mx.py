from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class ChristmasDayMX(HolidayBase):

    name_en = "Christmas Day"
    name_es = "Navidad"

    is_statutory = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 12 and date_to_check.day == 24:
            return True
        
        if date_to_check.month == 12 and date_to_check.day == 23 and date_to_check.isoweekday() == 5:
            return True
        
        if date_to_check.month == 12 and date_to_check.day == 25 and date_to_check.isoweekday() == 1:
            return True

        return False
