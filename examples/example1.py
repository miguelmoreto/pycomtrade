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
#
# This is an example of using the pyComtrade module to read a comtrade record.
# The Comtrade data are in the test_data folder.
#
# Developed by Miguel Moreto
# Brazil - 2013
#
__version__ = "$Revision$"  # SVN revision.
__date__ = "$Date$"         # Date of the last SVN revision.

# Matplotlib module is needed for this example.
# pyComtrade needs numpy.
import pyComtrade
import pylab

# Create an instance of the ComtradeRecord class and read the CFG file:
comtradeObj = pyComtrade.ComtradeRecord()
comtradeObj.read('./test_data3/test3.cfg', './test_data3/test3.dat')

print(comtradeObj.get_analog_ids())  # print the ids of the analog channels.

N = comtradeObj['endsamp'][-1]

print('Record has {} samples'.format(N))
print('Sampling rate is {} samples/sec.'.format(comtradeObj['samp'][-1]))

# Reading channel 4:
AnalogChannelData = comtradeObj['A'][22]['values']

DigitalChannelData = comtradeObj['D'][25]['values']

# Reading time vector:
time = comtradeObj.get_timestamps()

# Ploting with matplotlib
# pylab.plot(time,channelData)
f, axarr = pylab.subplots(2, sharex=True)

axarr[0].plot(time, AnalogChannelData)
axarr[0].set_title('pyComtrade Demo')
axarr[0].grid()
axarr[1].plot(time, DigitalChannelData)
axarr[1].set_ylim(top=1.05)  # bottom unchanged
axarr[1].grid()
axarr[1].set_xlabel('Time [s]')
pylab.show()
