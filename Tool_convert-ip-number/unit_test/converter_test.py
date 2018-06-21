# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
The file is designed for unit test.
"""
import sys
import unittest
sys.path.append('../../')

from ip_convertor import convert_ip2num
from ip_convertor.config import output_log


class TestSpider(unittest.TestCase):
    """Test the functions in ip converter.

    Test the separate modules's function imported in convert_ip2num.py.

    Attributes:
        log_file = The log file address to save the log info.
    """
    def __init__(self, *args, **kwargs):
        """Init the test class with all the attributes."""
        super(TestSpider, self).__init__(*args, **kwargs)
        self.log_file = './log/test'

    def test_convert_to_num(self):
        """Test the function 'convert_to_num'.

        Returns: Boolean.
        """
        # Import the logger.
        output_log.init_log(self.log_file)
        # Set test cases and check result.
        cases = ['172.168.5.1', '12 3.34.22.1', '1.2.3', '123 . 34.3.41']
        answers = ['2896692481', 'Error', 'Error', '2065826601']
        numbers = []
        for case in cases:
            number = convert_ip2num.convert_to_num(case)
            numbers.append(str(number))

        # Test results.
        self.assertTrue(numbers == answers)


if __name__ == "__main__":
    # Use 'python -m unittest converter_test' in console for unit test.
    unittest.main()
