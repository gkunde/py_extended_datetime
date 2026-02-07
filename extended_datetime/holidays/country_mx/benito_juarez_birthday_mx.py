from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class BenitoJuarezBirthdayMX(HolidayBase):

    name_en: str = "Benito Juárez's Birthday"
    name_es: str = "Natalicio de Benito Juárez"

    is_statutory: bool = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 3:

            if date_to_check.day == 21:
                return True
            
            if date_to_check.day == 20 and date_to_check.isoweekday() == 5:
                return True
            
            if date_to_check.day == 22 and date_to_check.isoweekday() == 1:
                return True

        return False
