
from abc import ABCMeta, abstractmethod
from datetime import datetime


class HolidayBase(metaclass=ABCMeta):
    """
    An abstract base class to define the required methods for a Holiday date
    check.
    """

    @abstractmethod
    def check_date(self, date_to_check: datetime) -> bool:
        """
        Validates if a given datetime object matches the defined holiday.

        :param date_to_check: A datetime object to assess.

        :returns: A boolean result indicating if the date matches.
        """
        pass
