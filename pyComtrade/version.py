# pyComtrade.version
# Helper module for managing pyComtrade version information
#
# Author:   Allen Leis <allen@pingthings.io>
# Created:  Tue Feb 02 14:57:54 2016 -0500
#
# Copyright (C) 2015 pingthings.io
# For license information, see LICENSE.txt
#
# ID: version.py [] allen@pingthings.io $

"""
Helper module for managing pyComtrade version information
"""

##########################################################################
## Versioning
##########################################################################

__version_info__ = {
    "major": 1,
    "minor": 0,
    "micro": 0,
    "releaselevel": "final",
    "serial": 0,
}


def get_version(short=False):
    """
    Returns the version from the version info.
    """
    assert __version_info__["releaselevel"] in ("alpha", "beta", "final")
    vers = [
        "%(major)i.%(minor)i" % __version_info__,
    ]
    if __version_info__["micro"]:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__["releaselevel"] != "final" and not short:
        vers.append(
            "%s%i" % (__version_info__["releaselevel"][0], __version_info__["serial"])
        )
    return "".join(vers)


##########################################################################
## Execution
##########################################################################

if __name__ == "__main__":
    print(get_version())
