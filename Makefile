# Makefile
# File for make utility
#
# Usage: make clean
#
# Author:   Allen Leis <allen@pingthings.io>
# Created:  Tue Feb 02 14:57:54 2016 -0500
#
# Copyright (C) 2015 pingthings.io
# For license information, see LICENSE.txt
#
# ID: Makefile [] allen@pingthings.io $


example:
	python examples/example1.py

test:
	nosetests -v --with-coverage --cover-package=pyComtrade --cover-inclusive --cover-erase tests

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
