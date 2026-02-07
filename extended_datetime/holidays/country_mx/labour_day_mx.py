from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class LabourDayMX(HolidayBase):

    name_en = "Labour Day"
    name_es = "Día del Trabajo"

    is_statutory = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 5 and date_to_check.day == 1:
            return True
        
        if date_to_check.month == 4 and date_to_check.day == 30 and date_to_check.isoweekday() == 5:
            return True
        
        if date_to_check.month == 5 and date_to_check.day == 2 and date_to_check.isoweekday() == 1:
            return True

        return False
