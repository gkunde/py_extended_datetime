from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class RemembranceDayCA(HolidayBase):

    name_en = "Remembrance Day"
    name_fr = "Jour du Souvenir"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:
        # Nov 11; observed on preceding Friday if on Saturday, or following Monday if on Sunday

        if date_to_check.month != 11:
            return False

        if date_to_check.day == 11:
            return True

        if date_to_check.day == 10 and date_to_check.isoweekday() == 5:
            return True

        if date_to_check.day == 12 and date_to_check.isoweekday() == 1:
            return True

        return False
