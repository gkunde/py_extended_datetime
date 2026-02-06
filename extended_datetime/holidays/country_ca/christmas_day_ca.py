from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class ChristmasDayCA(HolidayBase):

    name_en = "Christmas Day"
    name_fr = "Noël"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 12:
            return False

        if date_to_check.day == 25:
            return True

        # If Christmas falls on Saturday, observed previous Friday (24)
        if date_to_check.day == 24 and date_to_check.isoweekday() == 5:
            return True

        # If Christmas falls on Sunday, observed following Monday (26)
        if date_to_check.day == 26 and date_to_check.isoweekday() == 1:
            return True

        return False
