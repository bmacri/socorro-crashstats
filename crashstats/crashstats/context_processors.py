# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

def current_versions(request):
    """The views are decorator such that they have 'currentversions' attached
    on the request itself.
    By returning them in this context processor we make sure they are available
    in templates like {{ currentversions }}
    """
    data = {}
    if hasattr(request, 'currentversions'):
        data['currentversions'] = request.currentversions
        product = getattr(request, 'product', None)
        version = getattr(request, 'version', None)
        if product:
            data['product'] = product
        if version:
            data['version'] = version
    return data
