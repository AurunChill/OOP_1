#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Date:
    def __init__(self, year=1, month=1, day=1):
        """
        Initialize the date.

        :param year: Year (default is 1)
        :param month: Month (default is 1)
        :param day: Day (default is 1)
        """
        self.year = year
        self.month = month
        self.day = day
        self.validate_date()

    def validate_date(self):
        if self.month < 1 or self.month > 12:
            raise ValueError("Month must be between 1 and 12.")
        if self.day < 1 or self.day > self.days_in_month():
            raise ValueError("Invalid day for the given month.")

    def days_in_month(self):
        days_in_months = [31, 29 if self.is_leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_months[self.month - 1]

    def is_leap_year(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    @classmethod
    def from_string(cls, date_string):
        """
        Initialize the date from a string in the format "year.month.day".

        :param date_string: String representing the date
        :return: Instance of the Date class
        """
        year, month, day = map(int, date_string.split('.'))
        return cls(year, month, day)

    def add_days(self, days):
        """
        Adds a specified number of days to the date.

        :param days: Number of days to add
        :return: New date
        """
        from datetime import timedelta, datetime
        original_date = datetime(self.year, self.month, self.day)
        new_date = original_date + timedelta(days=days)
        return Date(new_date.year, new_date.month, new_date.day)

    def subtract_days(self, days):
        """
        Subtracts a specified number of days from the date.

        :param days: Number of days to subtract
        :return: New date
        """
        from datetime import timedelta, datetime
        original_date = datetime(self.year, self.month, self.day)
        new_date = original_date - timedelta(days=days)
        return Date(new_date.year, new_date.month, new_date.day)

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def days_between(self, other):
        """
        Calculates the number of days between the current date and another date.

        :param other: Another date
        :return: Number of days between the dates
        """
        from datetime import datetime
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return abs((date1 - date2).days)

    def read(self):
        """
        Reads the date from the keyboard.
        """
        date_string = input("Enter the date in the format 'year.month.day': ")
        date_instance = self.from_string(date_string)
        self.year, self.month, self.day = date_instance.year, date_instance.month, date_instance.day

    def display(self):
        """
        Displays the date in the format 'year.month.day'.
        """
        print(f"{self.year}.{self.month:02}.{self.day:02}")


if __name__ == '__main__':
    date1 = Date(2023, 10, 1)
    date2 = Date.from_string("2023.10.31")
    date1.display()
    date2.display()

    new_date = date1.add_days(30)
    new_date.display()

    new_date = date2.subtract_days(10)
    new_date.display()

    print(f"Date 1 is less than Date 2: {date1 < date2}")
    print(f"Number of days between dates: {date1.days_between(date2)}")

    date3 = Date()
    date3.read()
    date3.display()