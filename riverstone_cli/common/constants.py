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
import argparse
from os import environ

from github import Github

PARSER = argparse.ArgumentParser(
    description='''Riverstone CLI is a command line utility for Riverstone
    employees. This utility automates routinely used commands and
    procedures used at Riverstone.'''
)

SUBPARSER = PARSER.add_subparsers(dest="commands")

GITHUB = Github(environ.get('RSCLI_GITHUB_KEY'))


LABELS = {
    'RFR': 'RFR',
    'WIP': 'WIP'
}
