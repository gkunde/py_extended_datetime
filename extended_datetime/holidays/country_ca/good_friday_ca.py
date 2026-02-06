from datetime import datetime, timedelta

from extended_datetime.base.holiday_base import HolidayBase


def _easter_sunday(year: int) -> datetime:
    # Anonymous Gregorian algorithm (Meeus/Jones) with descriptive names
    golden_number = year % 19
    century = year // 100
    year_of_century = year % 100
    century_div4 = century // 4
    century_mod4 = century % 4
    century_plus8_div25 = (century + 8) // 25
    century_correction = (century - century_plus8_div25 + 1) // 3

    # Epact: age of the moon on Jan 1 (used in Easter calculation)
    epact = (19 * golden_number + century - century_div4 - century_correction + 15) % 30

    year_of_century_div4 = year_of_century // 4
    year_of_century_mod4 = year_of_century % 4

    weekday_offset = (32 + 2 * century_mod4 + 2 * year_of_century_div4 - epact - year_of_century_mod4) % 7

    paschal_correction = (golden_number + 11 * epact + 22 * weekday_offset) // 451

    month = (epact + weekday_offset - 7 * paschal_correction + 114) // 31
    day = ((epact + weekday_offset - 7 * paschal_correction + 114) % 31) + 1

    return datetime(year, month, day)


class GoodFridayCA(HolidayBase):

    name_en = "Good Friday"
    name_fr = "Vendredi saint"
    federal = True

    def check_date(self, date_to_check: datetime) -> bool:

        easter = _easter_sunday(date_to_check.year)
        good_friday = easter - timedelta(days=2)
        return date_to_check.year == good_friday.year and date_to_check.month == good_friday.month and date_to_check.day == good_friday.day
