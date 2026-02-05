from datetime import datetime


class IndependenceDayUS:

    def check_date(self, date_to_check: datetime) -> bool:

        if date_to_check.month != 7:
            return False

        if date_to_check.day == 4:
            return True

        if date_to_check.day == 3 and date_to_check.isoweekday() == 5:
            return True

        if date_to_check.day == 5 and date_to_check.isoweekday() == 1:
            return True

        return False
