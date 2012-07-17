# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ceritfi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""

import os

def where():
    f = os.path.split(__file__)[0]

    return os.path.join(f, 'cacert.pem')

if __name__ == '__main__':
    print(where())
