#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate all dates from inputed date to before 2023."""


def leap(year):
    """Determine if a year is leap or not."""
    div_by_4 = (year % 4 == 0)
    div_by_100 = (year % 100 == 0)
    div_by_400 = (year % 400 == 0)
    return div_by_4 and (not div_by_100 or div_by_400)


def days_by_month(year, month):
    """Total days by month."""
    if month == 2:
        return 28 + leap(year)
    if month in [4, 6, 9, 11]:
        return 30
    return 31


def next_date(year, month, day):
    """Calculate the next date adding one day."""
    day += 1
    if day > days_by_month(year, month):
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return year, month, day


def main():
    """Generate all dates from inputed date to before 2023."""
    print('Please input a date')
    year = int(input('year: '))
    month = int(input('month: '))
    day = int(input('day: '))

    while True:
        print(f'{year}\\{month}\\{day}')
        year, month, day = next_date(year, month, day)
        if year == 2024:
            break


if __name__ == '__main__':
    main()
