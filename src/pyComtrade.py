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

# pyComtrade: A python Class for read and write IEEE
#             Comtrade files based on 1999 standard
#
#
# OBS: - The field names are equal to Comtrade 1999 standard;
#
# Developed by Miguel Moreto
# Brazil - 2013
#
#
from __future__ import division
__version__ = "$Revision$"  # SVN revision.
__date__ = "$Date$"         # Date of the last SVN revision.


import numpy as np
import struct
import pandas as pd
import yaml

from .utils import _unicode


class ComtradeRecord(object):
    """
    A python Class for reading and writing IEEE Comtrade files.

    This is the main class of pyComtrade.
    """

    def __init__(self):
        """
        Initializes a ComtradeRecord instance.
        """

        # Argument string
        self.arg_str = ['header', 'nchannels', 'A', 'D', 'line_freq', 'nrates',
                        'samples', 'start', 'trigger', 'file_type', 'timemult',
                        'time_code', 'tmq_code']

        # Function dictionary
        self.fun_dct = {
            'header': self.dct_header,
            'nchannels': self.dct_nchannels,
            'A': self.dct_analog,
            'D': self.dct_digital,
            'line_freq': self.dct_lf,
            'nrates': self.dct_nrates,
            'samples': self.dct_samples,
            'start': self.dct_start,
            'trigger': self.dct_trigger,
            'file_type': self.dct_ft,
            'timemult': self.dct_tml,
            'time_code': self.dct_tcd,
            'tmq_code': self.dct_tmq
        }

        # Initializing variables
        self.reset()

    def reset(self):
        '''
        Resets an instance to its initial state.
        '''

        # Resets the variables
        self.cfg_data = {}  # Config data
        self.bdata = None   # Binary file data

    def cast_data(self, data):
        '''
        Cast data to the correct type.

        @param data argument to be casted.

        @return data with the correctly parsed type.
        '''

        # Test each type
        try:
            # int
            return int(data)
        except ValueError:
            pass
        try:
            # float
            return float(data)
        except ValueError:
            pass
        if data in ['True', 'False']:
            # boolean
            return data == 'True'
        # A string
        return _unicode(data)

    def proc_line(self, line, arg):
        '''
        Processes a COMTRADE config file line.

        @param line input line.
        @param arg type of line/argument.

        @return dictionary with the lines elements.
        '''

        # Stripe line from end data and split each property
        line = line.rstrip().split(',')

        # Parsing, if needed
        if arg == 'nchannels':
            line[1] = line[1][:-1]  # Removing the 'A' letter from the number
            line[2] = line[2][:-1]  # Removing the 'D' letter from the number

        # Casting
        line = [self.cast_data(l) for l in line]

        # Processing and returning dictionary
        return self.fun_dct[arg](line)

    def dct_header(self, data):
        '''
        Converts header line to dictionary form.

        @param data data to be converted.
        @return station name, recording device id, and standard revision year
        '''
        output = {}
        output['station_name'] = data[0]  # Station name
        output['rec_dev_id'] = data[1]  # Recording device ID
        if len(data) > 2:  # From 1999 revision
            output['rev_year'] = data[2]  # Standard revision year
        return output

    def dct_nchannels(self, data):
        '''
        Converts number of channels line to dictionary form.

        @param data data to be converted.
        @return number of channels info.
        '''
        output = {}
        output['TT'] = data[0]  # Number of channels (#A+#D)
        output['#A'] = data[1]  # Number of analogic channels
        output['#D'] = data[2]  # Number of analogic channels
        return output

    def dct_analog(self, data):
        '''
        Converts analog channel line to dictionary form.

        @param data data to be converted.
        @return analog channel data.
        '''

        # Setting initial output and properties string
        output = {}
        dt_str = [
            'An',         # analog channel index number
            'ch_id',      # station_name:channel_name
            'ph',         # channel phase identification (0 to 2)
            'ccbm',       # circuit component being monitored
            'uu',         # channel units
            'a',          # channel multiplier
            'b',          # channel offset
            'skew',       # time skew between channels
            'min',        # data range minimum value
            'max',        # data range maximum value
            'primary',    # PT/CT primary ratio factor
            'secondary',  # PT/CT scondary ratio factor
            'P_S'         # primary or secondary PT/CT scaling identifier. 'P' or 'S'
        ]

        # For each data property
        for dtidx, dt in enumerate(data):

            # Getting data
            dn = dt_str[dtidx]
            output[dn] = dt

        # Return output
        return output

    def dct_digital(self, data):
        '''
        Converts digital channel line to dictionary form.

        @param data data to be converted
        @return digital channel data.
        '''

        # Setting initial output and properties string
        output = {}
        dt_str = [
            'Dn',     # Digital channel index
            'ch_id',  # station_name:channel_name
            'ph',     # channel phase identification
            'ccbm',   # circuit component being monitore
            'y'       # normal state of the channel
        ]

        # For each data property
        for dtidx, dt in enumerate(data):

            # Getting data
            dn = dt_str[dtidx]
            output[dn] = dt

        # Return output
        return output

    def dct_lf(self, data):
        '''
        Converts line freq line to dictionary form.

        @param data data to be converted.
        @return line frequency.
        '''
        output = {}
        output['line_freq'] = data[0]  # Line frequency in Hz
        return output

    def dct_nrates(self, data):
        '''
        Converts nrates line to dictionary form.

        @param data data to be converted.
        @return number of sampling rates.
        '''
        output = {}
        output['nrates'] = data[0]  # Number of sampling rates in the file
        return output

    def dct_samples(self, data):
        '''
        Converts samples line to dictionary form.

        @param data data to be converted
        @return sampling rates and number of samples.
        '''
        output = {'samp': [], 'endsamp': []}

        # For each sample rate
        for i in range(self.cfg_data['nrates']):
            output['samp'].append(data[0])     # Sample rates
            output['endsamp'].append(data[1])  # Number of samples
        return output

    def dct_start(self, data):
        '''
        Converts start date/time line to dictionary form.

        @param data data to be converted.
        @return start date/time data.
        '''
        output = {}
        output['start_date'] = data[0]  # Start date
        output['start_time'] = data[1]  # Start time
        return output

    def dct_trigger(self, data):
        '''
        Converts trigger date/time line to dictionary form.

        @param data data to be converted
        @return trigger date/time data.
        '''
        output = {}
        output['trigger_date'] = data[0]  # Trigger date
        output['trigger_time'] = data[1]  # Trigger time
        return output

    def dct_ft(self, data):
        '''
        Converts file type line to dictionary form.

        @param data data to be converted
        @return file type.
        '''
        output = {}
        output['file_type'] = data[0]  # File type
        return output

    def dct_tml(self, data):
        '''
        Converts timemult line to dictionary form.

        @param data data to be converted.
        @param time multiplication factor/scale.
        '''
        output = {}
        output['timemult'] = data[0]  # time multiplication factor/scale
        return output

    def dct_tcd(self, data):  # TODO
        return NotImplementedError

    def dct_tmq(self, data):  # TODO
        return NotImplementedError

    def get_timestamps(self):
        '''
        Returns the samples timestamp

        @return timestamp vector.
        '''
        t_interval = 1/float(self.cfg_data['samp'][-1])
        n_samples = self.cfg_data['endsamp'][-1]
        t_end = n_samples*t_interval
        return np.linspace(0, t_end, n_samples)

    def get_analog_ids(self):
        '''
        Returns analog channels ID

        @return string with analog channels ID.
        '''
        analog_ids = [v['ch_id'] for v in self.cfg_data['A']]
        analog_ids = ';'.join(analog_ids)
        return analog_ids

    def get_digital_ids(self):
        '''
        Returns digital channels ID

        @return string with digital channels ID.
        '''
        digitial_ids = [v['ch_id'] for v in self.cfg_data['D']]
        digitial_ids = ';'.join(digitial_ids)
        return digitial_ids

    def read_ascii(self, file_path):
        '''
        Reads ASCII data file.

        @param file_path ASCII file path.
        '''

        # Open data
        data = pd.read_csv(file_path, index_col=0, header=None)

        # Convert values
        data = data.T.values.tolist()
        data = data[1:]

        # For each analog channel
        for cidx in range(self.cfg_data['#A']):

            # Reading channels
            values = np.array(data[cidx])
            values = values * self.cfg_data['A'][cidx]['a']
            values = values + self.cfg_data['A'][cidx]['b']
            self.cfg_data['A'][cidx]['values'] = values.tolist()

        # Removing analog channels
        data = data[self.cfg_data['#A']:]

        # For each digital channel
        for cidx in range(self.cfg_data['#D']):

            # Reading channels
            self.cfg_data['D'][cidx]['values'] = data[cidx]

    def read_binary(self, file_path):
        '''
        Reads binary data file.

        @param file_path binary file path.
        '''

        # Opens file and reads all data
        with open(file_path, 'rb') as bdata:
            self.bdata = bdata.read()

        # Reading analogic data
        self.read_bin_analog()
        self.read_bin_digital()

    def read_bin_analog(self):
        '''
        Reads analog channels data from binary data.
        '''

        # Getting auxiliary variables
        nA = self.cfg_data['#A']
        nD = self.cfg_data['#D']
        nH = int(np.ceil(nD/16.0))
        nS = self.cfg_data['endsamp'][-1]

        # Setting struct string
        str_struct = "ii{0}h".format(nA + nH)

        # Number of bytes per sample
        nbps = 4+4+nA*2+nH*2

        # For each channel
        for cidx in range(self.cfg_data['#A']):

            # Setting initial values
            values = []
            for sidx in range(nS):

                # Unpacking data
                data = self.bdata[sidx*nbps:(sidx+1)*nbps]
                data = struct.unpack(str_struct, data)
                values.append(data[cidx+2])

            # Converting values
            values = np.array(values)
            values = values * self.cfg_data['A'][cidx]['a']
            values = values + self.cfg_data['A'][cidx]['b']
            self.cfg_data['A'][cidx]['values'] = values.tolist()

    def read_bin_digital(self):
        '''
        Reads digitals channels data from binary data.
        '''

        # Getting auxiliary variables
        nA = self.cfg_data['#A']
        nD = self.cfg_data['#D']
        nH = int(np.ceil(nD/16.0))
        nS = self.cfg_data['endsamp'][-1]

        # Setting struct string
        str_struct = "ii{0}h{1}H".format(nA, nH)

        # Number of bytes per sample
        nbps = 4+4+nA*2+nH*2

        # For each channel
        for cidx in range(self.cfg_data['#D']):

            # Byte number
            bnum = int(np.ceil(cidx/16))

            # Digital channel value
            dchan_val = (1 << (cidx-(bnum-1)*16))

            # Setting initial values
            values = []
            for sidx in range(nS):

                # Unpacking data
                data = self.bdata[sidx*nbps:(sidx+1)*nbps]
                data = struct.unpack(str_struct, data)
                data = (dchan_val & data[nA+1+bnum]) * 1/dchan_val
                values.append(data)

            # Converting values
            values = np.array(values)
            self.cfg_data['D'][cidx]['values'] = values.tolist()

    def read(self, cfg_path, dat_path):
        '''
        Reads a COMTRADE file.

        @param cfg_path configuration data file (*.CFG).
        @param dat_path data file (*.DAT).

        @return dictionary with the COMTRADE file content.
        '''

        # Reset data content
        self.reset()

        # Try to open the config file
        with open(cfg_path, 'r') as cfg_file:

            # For each argument
            for arg in self.arg_str:

                # Extracting and testing arguments
                if arg in ['A', 'D']:

                    # Number of channels
                    nchnn = self.cfg_data['#A']
                    if arg == 'D':
                        nchnn = self.cfg_data['#D']

                    # Reading analog/digital  channels
                    self.cfg_data[arg] = []
                    for i in range(nchnn):

                        # Read line
                        line = cfg_file.readline()
                        if line.rstrip() == '':
                            break

                        # Process line
                        out_dct = self.proc_line(line, arg)
                        self.cfg_data[arg].append(out_dct.copy())

                else:

                    # Remaining channels

                    # Read line
                    line = cfg_file.readline()
                    if line.rstrip() == '':
                        break

                    # Process line
                    out_dct = self.proc_line(line, arg)
                    self.cfg_data.update(out_dct)

        # Reading data file. Add ASCII option
        if self.cfg_data['file_type'] == 'ASCII':
            # Read ASCII file
            self.read_ascii(dat_path)
        else:
            # Read binary
            self.read_binary(dat_path)

    def __getitem__(self, key):
        '''
        Returns a COMTRADE file key value.

        @param key target key.

        @return key value.
        '''
        return self.cfg_data[key]

    def __setitem__(self, key, item):
        '''
        Sets a COMTRADE file key value

        @param key target key.
        @param item target key value.
        '''
        self.cfg_data[key] = item

    def to_yaml(self, path):
        '''
        Saves file in yaml format.

        @param path file path.
        '''

        # Converto to yaml
        with open(path, 'w') as stream:
            yaml.dump(self.cfg_data, stream)

    def to_csv(self, path):
        '''
        Saves channels signals in a csv file.

        @param path csv file
        '''

        # Saving values
        achan = self.cfg_data['A']
        dchan = self.cfg_data['D']

        # Keys
        k = 'values'
        c = 'ch_id'

        # Converting each channel signal into a dictionary
        values = {}
        values.update({v[c]: v[k] for v in achan})
        values.update({v[c]: v[k] for v in dchan})

        # Saving into dataframe
        values = pd.DataFrame(values, self.get_timestamps().tolist())
        values.to_csv(path, header=True, index_label='timestamp')
