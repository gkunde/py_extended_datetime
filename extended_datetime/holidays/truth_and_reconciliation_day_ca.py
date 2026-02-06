from datetime import datetime

from extended_datetime.base.holiday_base import HolidayBase


class TruthAndReconciliationDayCA(HolidayBase):

    name_en = "National Day for Truth and Reconciliation"
    name_fr = "Journée nationale de la vérité et de la réconciliation"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:
        # Sept 30; observed on preceding Friday if on Saturday, or following Monday if on Sunday

        if date_to_check.month == 9:

            if date_to_check.day == 30:
                return True

            if date_to_check.day == 29 and date_to_check.isoweekday() == 5:
                return True

            return False

        if date_to_check.month == 10 and date_to_check.day == 1 and date_to_check.isoweekday() == 1:
            return True

        return False
