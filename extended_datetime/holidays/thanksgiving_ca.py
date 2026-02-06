from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class ThanksgivingCA(HolidayBase):

    name_en = "Thanksgiving"
    name_fr = "Action de grâce"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:

        # Second Monday in October (dates 8-14)
        if date_to_check.month != 10:
            return False

        if 8 <= date_to_check.day <= 14 and date_to_check.isoweekday() == 1:
            return True

        return False
