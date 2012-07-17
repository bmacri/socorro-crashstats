# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

from setuptools import setup, find_packages


setup(name='crashstats',
      version='1.0',
      description='Django application.',
      long_description='',
      author='',
      author_email='',
      license='',
      url='',
      include_package_data=True,
      classifiers = [],
      packages=find_packages(exclude=['tests']),
      install_requires=[])
