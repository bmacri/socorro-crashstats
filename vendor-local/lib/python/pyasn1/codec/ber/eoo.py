# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pyasn1.type import base, tag

class EndOfOctets(base.AbstractSimpleAsn1Item):
    defaultValue = 0
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x00)
        )
endOfOctets = EndOfOctets()
