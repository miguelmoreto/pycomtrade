#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (c) 2010 Miguel Moreto <http://sites.google.com/site/miguelmoreto/>

#This file is part of pyComtrade.
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
#
# This is an example of using the pyComtrade module to read a comtrade record.
# The Comtrade data are in the test_data folder.
#
# Developed by Miguel Moreto
# Federal University of Santa Catarina
# Brazil - 2010
#
__version__ = "$Revision$" # SVN revision.
__date__ = "$Date$" # Date of the last SVN revision.
import pyComtrade

comtradeObj = pyComtrade.ComtradeRecord() # Create an instance of the ComtradeRecord class.

# Reading the header file.
comtradeObj.ReadCFG('./test_data/test1.cfg')

print comtradeObj.Ach_id # print the ids of the analog channels.

print 'Record has %d samples' %(comtradeObj.getNumberOfSamples())
print 'Sampling rate is %d samples/sec.' %(comtradeObj.getSamplingRate())