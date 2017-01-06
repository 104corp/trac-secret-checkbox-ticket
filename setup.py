#!/usr/bin/env python
#
# Copyright (C) 2016 104 Corporation
# Copyright (C) 2016 Gea-Suan Lin <gslin@104.com.tw>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import find_packages, setup

PACKAGE = 'SecretCheckboxTicketPlugin'
VERSION = '0.1'

try:
    import trac
    if trac.__version__ < '1.0':
        print "%s %s requires Trac >= 1.0" % (PACKAGE, VERSION)
        sys.exit(1)
except ImportError:
    pass

setup(
    name = PACKAGE,
    version = VERSION,
    author = 'Gea-Suan Lin',
    author_email = 'gslin@104.com.tw',
    description = 'Adds ticket security policy',
    license = '3-Clause BSD',
    keywords = 'permission permissions acl trac plugin',
    packages = find_packages(),
    entry_points = {
        'trac.plugins': [
            'secretcheckboxticket = secretcheckboxticket.policy',
        ],
    },
)

