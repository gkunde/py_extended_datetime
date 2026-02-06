from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class NewYearsDayCA(HolidayBase):

    name_en = "New Year's Day"
    name_fr = "Jour de l'An"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month == 1 and date_to_check.day == 1:
            return True

        # Observed: if Jan 1 falls on Sunday observed on Monday Jan 2
        if date_to_check.month == 1 and date_to_check.day == 2 and date_to_check.isoweekday() == 1:
            return True

        # Observed: if Jan 1 falls on Saturday, observed previous Friday (Dec 31)
        if date_to_check.month == 12 and date_to_check.day == 31 and date_to_check.isoweekday() == 5:
            return True

        return False
