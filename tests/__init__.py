# tests
# init file for tests package
#
# Author:   Allen Leis <allen@pingthings.io>
# Created:  Tue Feb 02 13:54:17 2016 -0500
#
# Copyright (C) 2016 Allen Leis
# For license information, see LICENSE.txt
#
# ID: __init__.py [] allen@pingthings.io $

"""
init file for tests package
"""

##########################################################################
# Imports
##########################################################################

import unittest

##########################################################################
# Classes
##########################################################################


class InitializationTests(unittest.TestCase):
    def test_initialization(self):
        """
        Check the test suite runs by affirming 2+2=4
        """
        self.assertEqual(2 + 2, 4)

    def test_import(self):
        """
        Ensure the test suite can import our module
        """
        try:
            import pyComtrade
        except ImportError:
            self.fail("Was not able to import the pyComtrade")


##########################################################################
# Execution
##########################################################################

if __name__ == "__main__":
    pass
