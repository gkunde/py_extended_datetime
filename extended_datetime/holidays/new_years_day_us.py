from datetime import datetime

from extended_datetime.holidays.new_years_day import NewYearsDay


class NewYearsDayUS(NewYearsDay):

    def check_date(self, date_to_check: datetime) -> bool:

        if super().check_date(date_to_check):
            return True

        if date_to_check.month != 1:
            return False

        if date_to_check.day == 2 and date_to_check.isoweekday() == 1:
            return True

        return False
