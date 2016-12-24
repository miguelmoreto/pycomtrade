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

# pyComtrade: A python Class for read and write IEEE
#             Comtrade files based on 1999 standard
#
#
# OBS: - The field names ara iqual to Comtrade 1999 standard;
#
# Developed by Miguel Moreto
# Brazil - 2013
#
#
__version__ = "$Revision$" # SVN revision.
__date__ = "$Date$" # Date of the last SVN revision.
import os
import numpy
import struct

class ComtradeRecord:
    """
    A python Class for read and write IEEE Comtrade files. 
    
    This is the main class of pyComtrade.
    """

    def __init__(self,filename):
        """
        pyComtrade constructor: 
            Prints a message. 
            Clear the variables
            Check if filename exists.
            If so, read the CFG file.

        filename: string with the path for the .cfg file.        
        
        """
        self.filename = ''
        self.filehandler = 0
        # Station name, identification and revision year:
        self.station_name = ''
        self.rec_dev_id = ''
        self.rev_year = 0000
        # Number and type of channels:
        self.TT = 0
        self.A = 0 # Number of analog channels.
        self.D = 0 # Number of digital channels.
        # Analog channel information:
        self.An = []
        self.Ach_id = []
        self.Aph = []
        self.Accbm = []
        self.uu = []
        self.a = []
        self.b = []
        self.skew = []
        self.min = []
        self.max = []
        self.primary = []
        self.secondary = []
        self.PS = []
        # Digital channel information:
        self.Dn = []
        self.Dch_id = []
        self.Dph = []
        self.Dccbm = []
        self.y = []
        self.# Line frequency:
        self.lf = 0
        self.# Sampling rate information:
        self.nrates = 0
        self.samp = []
        self.endsamp = []
        # Date/time stamps:
        #    defined by: [dd,mm,yyyy,hh,mm,ss.ssssss]
        self.start = [00,00,0000,00,00,0.0]
        self.trigger = [00,00,0000,00,00,0.0]
        # Data file type:
        self.ft = ''
        # Time stamp multiplication factor:
        self.timemult = 0.0
        self.DatFileContent = ''
        
        print 'pyComtrade instance created!'
        
        if os.path.isfile(filename):
            self.filename = filename
            self.ReadCFG()
        else:
            print "%s File not found." %(filename)
            return

    def clear(self):
        """
        Clear the internal (private) variables of the class.
        """
        self.filename = ''
        self.filehandler = 0
        # Station name, identification and revision year:
        self.station_name = ''
        self.rec_dev_id = ''
        self.rev_year = 0000
        # Number and type of channels:
        self.TT = 0
        self.A = 0 # Number of analog channels.
        self.D = 0 # Number of digital channels.
        # Analog channel information:
        self.An = []
        self.Ach_id = []
        self.Aph = []
        self.Accbm = []
        self.uu = []
        self.a = []
        self.b = []
        self.skew = []
        self.min = []
        self.max = []
        self.primary = []
        self.secondary = []
        self.PS = []
        # Digital channel information:
        self.Dn = []
        self.Dch_id = []
        self.Dph = []
        self.Dccbm = []
        self.y = []
        # Line frequency:
        self.lf = 0
        # Sampling rate information:
        self.nrates = 0
        self.samp = []
        self.endsamp = []
        # Date/time stamps:
        #    defined by: [dd,mm,yyyy,hh,mm,ss.ssssss]
        self.start = [00,00,0000,00,00,0.0]
        self.trigger = [00,00,0000,00,00,0.0]
        # Data file type:
        self.ft = ''
        # Time stamp multiplication factor:
        self.timemult = 0.0
        
        self.DatFileContent = ''
        
    def ReadCFG(self):
        """
        Reads the Comtrade header file (.cfg).
        """
            
        self.filehandler = open(self.filename,'r')
        # Processing first line:
        line = self.filehandler.readline()
        templist = line.split(',')
        self.station_name = templist[0]
        self.rec_dev_id = templist[1]
        # Odd cfg file may not contain all first line fields
        # checking vector length to avoid IndexError
        if len(templist) > 2:
            self.rev_year = int(templist[2])

        # Processing second line:
        line = self.filehandler.readline().rstrip() # Read line and remove spaces and new line characters.
        templist = line.split(',')
        self.TT = int(templist[0])
        self.A = int(templist[1].strip('A'))
        self.D = int(templist[2].strip('D'))

        # Processing analog channel lines:
        for i in range(self.A): #@UnusedVariable
            line = self.filehandler.readline()
            templist = line.split(',')
            self.An.append(int(templist[0]))
            self.Ach_id.append(templist[1])
            self.Aph.append(templist[2])
            self.Accbm.append(templist[3])
            self.uu.append(templist[4])
            self.a.append(float(templist[5]))
            self.b.append(float(templist[6]))
            self.skew.append(float(templist[7]))
            self.min.append(int(templist[8]))
            self.max.append(int(templist[9]))
            # Odd cfg file may not contain all analog channel fields
            # checking vector length to avoid IndexError
            if len(templist) > 10:
                self.primary.append(float(templist[10]))
            if len(templist) > 11:
                self.secondary.append(float(templist[11]))
            if len(templist) > 12:
                self.PS.append(templist[12])

        # Processing digital channel lines:
        for i in range(self.D): #@UnusedVariable
            line = self.filehandler.readline()
            templist = line.split(',')
            self.Dn.append(int(templist[0]))
            self.Dch_id.append(templist[1])
            self.Dph.append(templist[2])
            # Odd cfg file may not contain all digital channel fields
            # checking vector length to avoid IndexError
            if len(templist) > 3:
                self.Dccbm.append(templist[3])
            if len(templist) > 4:
                self.y.append(int(templist[4]))

        # Read line frequency:
        self.lf = int(float(self.filehandler.readline()))

        # Read sampling rates:
        self.nrates = int(self.filehandler.readline()) # nrates.
        for i in range(self.nrates): #@UnusedVariable
            line = self.filehandler.readline()
            templist = line.split(',')
            self.samp.append(int(float(templist[0])))
            self.endsamp.append(int(float(templist[1])))

        # Read start date and time ([dd,mm,yyyy,hh,mm,ss.ssssss]):
        line = self.filehandler.readline()
        templist = line.split('/')
        self.start[0] = int(templist[0]) # day.
        self.start[1] = int(templist[1]) # month.
        templist = templist[2].split(',')
        self.start[2] = int(templist[0]) # year.
        templist = templist[1].split(':')
        self.start[3] = int(templist[0]) # hours.
        self.start[4] = int(templist[1]) # minutes.
        self.start[5] = float(templist[2]) # seconds.

        # Read trigger date and time ([dd,mm,yyyy,hh,mm,ss.ssssss]):
        line = self.filehandler.readline()
        templist = line.split('/')
        self.trigger[0] = int(templist[0]) # day.
        self.trigger[1] = int(templist[1]) # month.
        templist = templist[2].split(',')
        self.trigger[2] = int(templist[0]) # year.
        templist = templist[1].split(':')
        self.trigger[3] = int(templist[0]) # hours.
        self.trigger[4] = int(templist[1]) # minutes.
        self.trigger[5] = float(templist[2]) # seconds.

        # Read file type:
        self.ft = self.filehandler.readline()
        
        # Read time multiplication factor:
        # Odd cfg file may not have multiplication field, so checking
        # its existance before reading is a safe measure
        # If the multiplication field is not available, it will be considered as 1
        self.timemul = self.filehandler.readline()
        if self.timemul != '':
            self.timemul = float(self.timemul)
        else:
            self.timemul = 1

        # END READING .CFG FILE.
        self.filehandler.close() # Close file.
    
    def getNumberOfSamples(self):
        """
        Return the number of samples of the oscillographic record.

        Only one smapling rate is taking into account for now.
        """
        return self.endsamp[0]
        
    def getSamplingRate(self):
        """
        Return the sampling rate.
        
        Only one smapling rate is taking into account for now.
        """
        return self.samp[0]

    def getTime(self):
        """
        Actually, this function creates a time stamp vector 
        based on the number of samples and sample rate.
        """
        T = 1/float(self.samp[self.nrates-1])
        endtime = self.endsamp[self.nrates-1] * T

        t = numpy.linspace(0,endtime,self.endsamp[self.nrates-1])

        return t

    def getAnalogID(self,num):
        """
        Returns the COMTRADE ID of a given channel number.
        The number to be given is the same of the COMTRADE header.
        """
        listidx = self.An.index(num) # Get the position of the channel number.
        return self.Ach_id[listidx]
        
    def getDigitalID(self,num):
        """
        Reads the COMTRADE ID of a given channel number.
        The number to be given is the same of the COMTRADE header.
        """
        listidx = self.Dn.index(num) # Get the position of the channel number.
        return self.Dch_id[listidx]
        
    def getAnalogType(self,num):
        """
        Returns the type  of the channel 'num' based 
        on its unit stored in the Comtrade header file.
        
        Returns 'V' for a voltage channel and 'I' for a current channel.
        """
        listidx = self.An.index(num)
        unit = self.uu[listidx]

        if unit == 'kV' or unit == 'V':
            return 'V'
        elif unit == 'A' or unit == 'kA':
            return 'I'
        else:
            print 'Unknown channel type'
            return 0
            
    def getAnalogUnit(self,num):
        """
        Returns the COMTRADE channel unit (e.g., kV, V, kA, A)
        of a given channel number.
        The number to be given is the same of the COMTRADE header.
        """
        listidx = self.An.index(num) # Get the position of the channel number.
        return self.uu[listidx]
    
    def ReadDataFile(self):
        """
        Reads the contents of the Comtrade .dat file and store them in a
        private variable.
        
        For accessing a specific channel data, see methods getAnalogData and
        getDigitalData.
        """
        if os.path.isfile(self.filename[0:-4] + '.dat'):
            filename = self.filename[0:-4] + '.dat'
    
        elif os.path.isfile(self.filename[0:-4] + '.DAT'):
            filename = self.filename[0:-4] + '.DAT'
        
        else:
            print "Data file File not found."
            return 0
        
        self.filehandler = open(filename,'rb')
        self.DatFileContent = self.filehandler.read()
    
        # END READING .dat FILE.
        self.filehandler.close() # Close file.        
        
        return 1
        
    def getAnalogChannelData(self,ChNumber):
        """
        Returns an array of numbers containing the data values of the channel
        number "ChNumber".
        
        ChNumber is the number of the channal as in .cfg file.
        """

        if not self.DatFileContent:
            print "No data file content. Use the method ReadDataFile first"
            return 0
        
        if (ChNumber > self.A):
            print "Channel number greater than the total number of channels."
            return 0
            
        # Fomating string for struct module:
        str_struct = "ii%dh" %(self.A + int(numpy.ceil((float(self.D)/float(16)))))
        # Number of bytes per sample:
        NB = 4 + 4 + self.A*2 + int(numpy.ceil((float(self.D)/float(16))))*2        
        # Number of samples:
        N = self.getNumberOfSamples()
        
        # Empty column vector:
        values = numpy.empty((N,1))

        ch_index = self.An.index(ChNumber)

        # Reading the values from DatFileContent string:
        for i in range(N):
            data = struct.unpack(str_struct,self.DatFileContent[i*NB:(i*NB)+NB])
            values[i] = data[ChNumber+1] # The first two number ar the sample index and timestamp

        values = values * self.a[ch_index] # a factor
        values = values + self.b[ch_index] # b factor
        
        return values
        
    def getDigitalChannelData(self,ChNumber):
        """
        Returns an array of numbers (0 or 1) containing the values of the 
        digital channel status.
        
        ChNumber: digital channel number.
        """

        if not self.DatFileContent:
            print "No data file content. Use the method ReadDataFile first"
            return 0
            
        if (ChNumber > self.D):
            print "Digital channel number greater than the total number of channels."
            return 0
        
        # Fomating string for struct module:
        str_struct = "ii%dh%dH" %(self.A, int(numpy.ceil((float(self.D)/float(16)))))
        # Number of bytes per sample:
        NB = 4 + 4 + self.A*2 + int(numpy.ceil((float(self.D)/float(16))))*2        
        # Number of samples:
        N = self.getNumberOfSamples()

        # Empty column vector:
        values = numpy.empty((N,1))
        # Number of the 16 word where digital channal is. Every word contains
        # 16 digital channels:
        byte_number = int(numpy.ceil((ChNumber-1)/16)+1)
        # Value of the digital channel. Ex. channal 1 has value 2^0=1, channel
        # 2 has value 2^1 = 2, channel 3 => 2^2=4 and so on.
        digital_ch_value = (1<<(ChNumber-1-(byte_number-1)*16))

        # Reading the values from DatFileContent string:
        for i in range(N):
            data = struct.unpack(str_struct,self.DatFileContent[i*NB:(i*NB)+NB])
            # The first two number ar the sample index and timestamp.
            # And logic to extract only one channel from the 16 bit.
            # Normalize the output to 0 or 1 
            values[i] = (digital_ch_value & data[self.A+1+byte_number]) * 1/digital_ch_value 
        
        # Return the array.
        return values
