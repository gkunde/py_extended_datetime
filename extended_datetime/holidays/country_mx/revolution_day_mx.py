from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class RevolutionDayMX(HolidayBase):

    name_en = "Revolution Day"
    name_es = "Día de la Revolución"

    is_statutory = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 11 and date_to_check.day == 20:
            return True
        
        if date_to_check.month == 11 and date_to_check.day == 19 and date_to_check.isoweekday() == 5:
            return True
        
        if date_to_check.month == 11 and date_to_check.day == 21 and date_to_check.isoweekday() == 1:
            return True

        return False
