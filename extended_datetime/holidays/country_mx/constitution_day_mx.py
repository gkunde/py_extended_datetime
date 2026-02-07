from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class ConstitutionDayMX(HolidayBase):

    name_en: str = "Constitution Day"
    name_es: str = "Día de la Constitución"

    is_statutory: bool = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 2:

            if date_to_check.day == 5:
                return True
            
            if date_to_check.day == 4 and date_to_check.isoweekday() == 5:
                return True
            
            if date_to_check.day == 6 and date_to_check.isoweekday() == 1:
                return True

        return False
