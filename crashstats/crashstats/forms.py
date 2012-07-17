# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django import forms


class BugInfoForm(forms.Form):

    bug_ids = forms.CharField(required=True)
    include_fields = forms.CharField(required=True)

    def clean_bug_ids(self):
        value = self.cleaned_data['bug_ids']
        return [x.strip() for x in value.split(',') if x.strip()]

    def clean_include_fields(self):
        value = self.cleaned_data['include_fields']
        return [x.strip() for x in value.split(',') if x.strip()]
