#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import necessary packages.
import argparse
import datetime


def date_convert(date, days):
    """Increase or decrease date by days.

    It's designed for conveniently increasing or decreasing date.

    :param date: The date format is as followings:
                '2018-07-10' or '20180710' or '2018/07/10'
    :param days: Numerical value. Positive or negative.

    :return: Converted date in the same format of input date.
    """
    # Convert date into same formate.
    if '-' in date:
        delimiter = '-'
        date = date.replace('-', '')
    elif '/' in date:
        delimiter = '/'
        date = date.replace('/', '')
    else:
        delimiter = ''

    # Decrease or increase date.
    start_date = datetime.datetime.strptime(date, '%Y%m%d')
    delta = datetime.timedelta(days=days)
    end_date = start_date + delta

    # Convert end date into suitable format.
    end_date = end_date.strftime('%Y%m%d')
    output_date = end_date[0:4] + delimiter + end_date[4:6] + delimiter + end_date[6:8]

    return output_date


def main():
    """The main function to increase date or decrease date.

    :return: Output converted date.
    """
    # Parse the argument and read into the date.
    # ------------------------------------------
    parser = argparse.ArgumentParser(description='This is script to increase date or decrease date.')
    parser.add_argument('-d', required=True, help='The input date.')
    parser.add_argument('-n', required=True, help='The days to increase or decrease.')
    args = parser.parse_args()
    date = args.d
    days = args.n

    # Convert input date to output date, according to days.
    output_date = date_convert(date, int(days))

    print output_date


if __name__ == '__main__':
    main()
