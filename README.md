Description
===============

pyComtrade is a python module that provides you a transparent way for reading and writing (not implemented yet) oscillographic files stored in IEEE Comtrade format.

Comtrade stands for COMmon format for Transient Data Exchange for power systems. It is a file format standardised by the IEEE that is used to store transient signals from Digital Fault Recorders, Oscillographs or Digital Protective Relays.

pyComtrade was created and maintained by Miguel Moreto at Federal University of Santa Catarina - Brazil

Feel free to use the module in your program. Don't forget that pyComtrade is licensed under the GNU version 3 license. For more info about this read the *LICENSE.txt*.

Release Notes
===============
* Version 0.3.0
  - Added ASCII data file support.
  - Source code refactored.
  - Changed metadata handling from lists to dictionaries.
  - Python 3 support.

  Many thanks to the contributors @ldemattos and @bluesdog164 who made most of the changes for this release.

* Version 0.2.0

  - Implemented a method to read digital channels.
  - Updated example.
  - Added one more test data with digital channel data.

* Version 0.1.0

  - Reads only analog channels.
  - Reads only binary Comtrade files (1999 Standard).

To Do
===============

* Review the last version of Comtrade Standard C37.111-2013.
* Write Comtrade files.

Install
===============

Pip
---------------

Run pip install pyComtrade from the command line.


From source (windows and linux)
-------------------------------

Extract the source .zip file.

Run:

    python.exe setup.py install

Usage
===============

See **example1.py** at the source file.

Thanks for using pyComtrade module.
