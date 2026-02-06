from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class LabourDayCA(HolidayBase):

    name_en = "Labour Day"
    name_fr = "Fête du Travail"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:

        # First Monday in September
        if date_to_check.month != 9:
            return False

        if 1 <= date_to_check.day and date_to_check.day <= 7 and date_to_check.isoweekday() == 1:
            return True

        return False
