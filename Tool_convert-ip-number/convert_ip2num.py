#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import necessary packages.
import argparse
import logging
import os

from config import output_log

# Create logger for debugging.
output_log.init_log('./log/converter')


def convert_to_num(ip_address):
    """Convert ip into number.

    Convert ip address into 32-bit integer number.

    :param ip_address: The ip address, eg. 127.125.5.1.

    :return: The 32-bit number converted from ip address.
    """
    # Iterate through ip once and split ip into four parts.
    ip_parts = ip_address.split('.')
    # Check ip address is legal or not.
    if len(ip_parts) != 4:
        logging.error('The ip address %s is in wrong length.\n' % ip_address)
        return 'Error'

    # Loop through ip list and convert into integer.
    number = 0
    for i in xrange(len(ip_parts)):
        try:
            number = number + int(ip_parts[i].strip()) * 2**((len(ip_parts) - i - 1) * 8)
        except ValueError as e:
            logging.error('The ip address %s is in error: %s.\n' % (ip_address, str(e)))
            return 'Error'

    return number


def main():
    """The main function to convert ip address into 32-bit integer.

    :return: Save result into text file.
    """
    # Parse the argument and read into the ip address.
    # ------------------------------------------
    parser = argparse.ArgumentParser(description='This is script to convert ip address into integer.')
    parser.add_argument('-f', required=True, help='The file which saves ip addresses.')
    args = parser.parse_args()
    file_name = args.f

    # Read file and parse ip into list.
    ip_list = []
    try:
        with open(file_name, 'r') as f:
            for line in f.readlines():
                ip_list.append(line.strip())
    except IOError as e:
        logging.error('Not found the input file with error info: %s.\n' % str(e))
        return 1

    # Go through ip list and convert ip address into integer.
    file_path = 'result/ip_num_result.txt'
    directory = os.path.dirname(file_path)
    try:
        os.stat(directory)
    except OSError as e:
        logging.error('Not found the input directory with error info: %s.\n' % str(e))
        os.mkdir(directory)
    with open(file_path, 'w') as f:
        for ip in ip_list:
            num = convert_to_num(ip)
            f.writelines(str(ip) + ' : ' + str(num) + '\n')


if __name__ == '__main__':
    # Run main body of script.
    main()
