from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class CanadaDayCA(HolidayBase):

    name_en = "Canada Day"
    name_fr = "Fête du Canada"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:
        # Canada Day is July 1. Observance rules:
        # - If July 1 is on a Sunday, observed on Monday July 2
        # - If July 1 is on a Saturday, observed on Monday July 3

        if date_to_check.month != 7:
            return False

        if date_to_check.day == 1:
            return True

        # Observed on July 2 when July 1 is Sunday
        if date_to_check.day == 2 and date_to_check.isoweekday() == 1:
            return True

        # Observed on July 3 when July 1 is Saturday
        if date_to_check.day == 3 and date_to_check.isoweekday() == 1:
            return True

        return False
