from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class VictoriaDayCA(HolidayBase):

    name_en = "Victoria Day"
    name_fr = "Fête de la Reine"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:

        # Victoria Day: Monday preceding May 25 (i.e., the last Monday on or before May 24)
        if date_to_check.month != 5:
            return False

        if 18 <= date_to_check.day <= 24 and date_to_check.isoweekday() == 1:
            return True

        return False
