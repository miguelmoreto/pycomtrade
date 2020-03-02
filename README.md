[![Build Status](https://travis-ci.com/fortes23/pycomtrade.svg?branch=feat_ci)](https://travis-ci.com/fortes23/pycomtrade)
[![codecov](https://codecov.io/gh/fortes23/pycomtrade/branch/feat_ci/graph/badge.svg)](https://codecov.io/gh/fortes23/pycomtrade)
[![PyPy Latest version](https://img.shields.io/pypi/v/pycomtrade.svg)](https://pypi.python.org/pypi/pycomtrade)
[![Requirements Status](https://requires.io/github/fortes23/pycomtrade/requirements.svg?branch=feat_ci)](https://requires.io/github/fortes23/pycomtrade/requirements/?branch=feat_ci)

Description
===============

pyComtrade is a python module that provides you a transparent way for reading and writing oscillographic files stored in IEEE Comtrade format.

Comtrade stands for COMmon format for Transient Data Exchange for power systems. It is a file format standardised by the IEEE that is used to store transient signals from Digital Fault Recorders, Oscillographs or Digital Protective Relays.

pyComtrade was created and maintained by Miguel Moreto at Federal University of Santa Catarina - Brazil


Feel free to use the module in your program. Don't forget that pyComtrade is licensed under the GNU version 3 license. For more info about this read the *COPYING.txt*.

Release Notes
===============

* Version 0.2.0

  - Implemented a method to read digital channels.
  - Updated example.
  - Added one more test data with digital channel data.

* Version 0.1.0

  - Reads only analog channels.
  - Reads only binary Comtrade files (1999 Standard).

To Do
===============

* Read ASCII Comtrade Files (only binary for now)
* Review the last version of Comtrade Standard C37.111-2013.

Install
===============

Binaries
---------------

Use the executables (win32 or win64). The binaries was generated for Python 2.7. If you have different version, install from source.

From source (windows and linux)
-------------------------------

Extract the source .zip file.

Run:

    python.exe setup.py install

Usage
===============

See **example1.py** at the source file.

Thanks for using pyComtrade module.
