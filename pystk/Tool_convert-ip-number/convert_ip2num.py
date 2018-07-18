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
    # Iterate through ip.
    number = 0
    part_num = 0
    part_str = ''
    for i in xrange(len(ip_address)):
        num = len(ip_address) - i - 1
        if ip_address[num] == '.' or num == 0:
            if num == 0:
                part_str = ip_address[num] + part_str
            if len(part_str.strip()) > 4:
                logging.error('The ip address %s has wrong length in some parts.\n' % ip_address)
                return 'Error'
            try:
                # Add number.
                number = number + int(part_str.strip()) * 2**(part_num * 8)
            except ValueError as e:
                logging.error('The ip address %s is in error: %s.\n' % (ip_address, str(e)))
                return 'Error'
            if int(part_str.strip()) > 255 or int(part_str.strip()) < 0:
                logging.error('The ip address %s has abnormal number out of bound 0~255.\n' % ip_address)
                return 'Error'
            part_num += 1
            part_str = ''
        else:
            part_str = ip_address[num] + part_str

    # Check part number.
    if part_num != 4:
        logging.error('The ip address %s is in wrong length.\n' % ip_address)
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
