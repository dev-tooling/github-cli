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
from __future__ import print_function

from six import iteritems

from riverstone_cli.commands.commands import COMMANDS
from riverstone_cli.common.constants import PARSER


def main():
    """Riverstone CLI main entry point.
    """
    for (_, value) in iteritems(COMMANDS):
        value.register_opts()
    args = vars(PARSER.parse_args())
    COMMANDS[args.get('commands')].handler(args)


if __name__ == "__main__":
    main()
