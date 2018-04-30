#!/usr/bin/env python
'''
Copyright 2018 Riverstone Software, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from __future__ import absolute_import
import os.path

from setuptools import setup
from setuptools import find_packages


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

setup(
    name='riverstone_cli',
    version='0.0.4',
    description=('Riverstone CLI for Riverstone employees.'),
    author='Riverstone Software, LLC',
    author_email='info@riverstone.io',
    license='Apache License (2.0)',
    url='https://riverstone.io/',
    install_requires=[
        'GitPython==2.1.9',
        'PyGithub==1.39'
    ],
    dependency_links=[],
    test_suite='tests',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['setuptools', 'tests']),
    scripts=['bin/rsc'],
    entry_points={}
)
