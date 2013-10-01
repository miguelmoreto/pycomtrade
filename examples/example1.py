#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (c) 2013 Miguel Moreto <http://sites.google.com/site/miguelmoreto/>

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
# Brazil - 2013
#
__version__ = "$Revision$" # SVN revision.
__date__ = "$Date$" # Date of the last SVN revision.

# Matplotlib module is needed for this example.
# pyComtrade needs numpy.
import pyComtrade
import pylab

 # Create an instance of the ComtradeRecord class and read the CFG file:
comtradeObj = pyComtrade.ComtradeRecord('./test_data1/test1.cfg')

print comtradeObj.Ach_id # print the ids of the analog channels.

N = comtradeObj.getNumberOfSamples()

print 'Record has %d samples' %(N)
print 'Sampling rate is %d samples/sec.' %(comtradeObj.getSamplingRate())

# Reading data file:
comtradeObj.ReadDataFile()

# Reading channel 4:
channelData = comtradeObj.getAnalogChannelData(4)

# Reading time vector:
time = comtradeObj.getTime()

# Ploting with matplotlib
pylab.plot(time,channelData)
pylab.show()