# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Example views. Feel free to delete this app."""

import logging

from django import http
from django.shortcuts import render

import bleach
import commonware
from funfactory.log import log_cef
from mobility.decorators import mobile_template
from session_csrf import anonymous_csrf


log = commonware.log.getLogger('playdoh')


@mobile_template('examples/{mobile/}home.html')
def home(request, template=None):
    """Main example view."""
    data = {}  # You'd add data here that you're sending to the template.
    log.debug("I'm alive!")
    return render(request, template, data)


@anonymous_csrf
def bleach_test(request):
    """A view outlining bleach's HTML sanitization."""
    allowed_tags = ('strong', 'em')

    data = {}

    if request.method == 'POST':
        bleachme = request.POST.get('bleachme', None)
        data['bleachme'] = bleachme
        if bleachme:
            data['bleached'] = bleach.clean(bleachme, tags=allowed_tags)

        # CEF logging: Log user input that needed to be "bleached".
        if data['bleached'] != bleachme:
            log_cef('Bleach Alert', logging.INFO, request,
                    username='anonymous', signature='BLEACHED',
                    msg='User data needed to be bleached: %s' % bleachme)

    return render(request, 'examples/bleach.html', data)
