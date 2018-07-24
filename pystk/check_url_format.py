# !/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import logging
import re
import time

import config.output_log as ol


def check_url_format(url):
    """Check the format of url is normal or not.

    This function is designed to use regex to detect abnormal urls.

    :param url: The url which is tended to be checked.

    :return: The string result.
            'Normal' for normal url format.
            'Error' for abnormal url format.
    """
    # Define the regex pattern of normal url.
    pattern = r"^((https|http|ftp|rtsp|mms)?://)" \
     + "+(([0-9a-zA-Z_!~*'().&=+$%-]+: )?[0-9a-zA-Z_!~*'().&=+$%-]+@)?" \
     + "(([0-9]{1,3}\\.){3}[0-9]{1,3}" \
     + "|" \
     + "([0-9a-zA-Z_!~*'()-]+\\.)*" \
     + "([0-9a-zA-Z][0-9a-zA-Z-]{0,61})?[0-9a-zA-Z]\\." \
     + "[a-zA-Z]{2,6})" \
     + "(:[0-9]{1,4})?" \
     + "((/?)|" \
     + "(/[0-9a-zA-Z_!~*'().;?:@&=+$,%#-]+)+/?)$"

    # Run the regex for test.
    if re.match(pattern, url):
        return 'Normal'
    else:
        return 'Error'


def detect_abnormal_url(dataframe, column_name):
    """Check the pattern of urls.

    Given column name of urls, check urls' pattern and return column of results.

    :param dataframe: The input dataframe in pandas.
    :param column_name: The column name of target urls, which should be converted.

    :return: The new dataframe with attached result column, consisting of 'Normal' or 'Error'.
    """
    # Check patterns of urls whether they are normal or error.
    dataframe['url_pattern'] = dataframe[column_name].apply(check_url_format, axis=0)

    return dataframe


def main():
    """The main function to check normal url format.

    :return: The output file contains urls with their results.
            The content format is 'url\tresult'.
    """
    # Input the file name.
    parser = argparse.ArgumentParser(description='This is script to check the normal url format.')
    parser.add_argument('-i', required=True, help='The input file path.')
    parser.add_argument('-o', required=True, help='The output file path.')

    # Create logger for debugging.
    ol.init_log('./log/url_check')

    # Read, parse and check the urls in file.
    args = parser.parse_args()
    file_path = args.i
    output_path = args.o

    # Total records number.
    with open(file_path) as f:
        total_records = len(f.readlines())
    with open(file_path) as f:
        # Record the starting time.
        start_time = time.time()
        logging.info('Start analyzing the url format and outputing results. '
                     'Start time is %s.' % start_time)
        count = 0.0
        with open(output_path, 'a') as fr:
            for line in f.readlines():
                count += 1  # Add count number.
                if count % 1000 == 0:
                    logging.info('The percent of running records is %s' % count/total_records)
                line = line.strip()
                result = check_url_format(line)

                # Output the content with format 'url+result'.
                fr.writelines(line + '\t' + result + '\n')

    # Record ending time.
    end_time = time.time()
    logging.info('End analyzing the url format and outputing results. '
                 'End time is %s. \nAnd the duration is %s' % (end_time, end_time-start_time))


if __name__ == '__main__':
    main()
