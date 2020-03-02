#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 Miguel Moreto <http://sites.google.com/site/miguelmoreto/>

# This file is part of pyComtrade.
#
#    pyComtrade is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    pyComtrade is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyComtrade.  If not, see <http://www.gnu.org/licenses/>.
# ====================================================================

import os

from distutils.core import setup


def parse_requirements():
    """
    Reads requirements.txt
    """
    with open(os.path.join(os.path.dirname(__file__),
              "requirements/requirements.txt")) as f:
        requirements = f.read()
    return requirements.split('\n')


with open('README.md') as file:
    long_description = file.read()

setup(name='pyComtrade',
      version='0.2.0',
      description='Python module for reading and writing Comtrade files.',
      long_description=long_description,
      author='Miguel Moreto',
      author_email='moreto@ieee.org',
      maintainer='Miguel Moreto',
      maintainer_email='moreto@ieee.org',
      url='http://code.google.com/p/pycomtrade/',
      license='GPLv3',
      packages=['pyComtrade'],
      package_dir={'pyComtrade': 'src'},
      install_requires=parse_requirements())
