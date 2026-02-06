from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class BoxingDayCA(HolidayBase):

    name_en = "Boxing Day"
    name_fr = "Lendemain de Noël"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 12:
            return False

        if date_to_check.day == 26:
            return True

        # If Boxing Day falls on Saturday, observed previous Friday (25)
        if date_to_check.day == 25 and date_to_check.isoweekday() == 5:
            return True

        # If Boxing Day falls on Sunday, observed following Monday (27)
        if date_to_check.day == 27 and date_to_check.isoweekday() == 1:
            return True

        return False
