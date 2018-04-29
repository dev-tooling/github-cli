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
from riverstone_cli.common.constants import SUBPARSER


def setup_subparser(name, description, commands):
    """Setup a subparser and add commands argument.
    """
    subparser = SUBPARSER.add_parser(
        name,
        help=description
    )
    subparser.add_argument(
        'sub_command',
        metavar='sub_command',
        type=str,
        nargs='+',
        help='Which command to run. Options: %s' % ', '.join(commands),
        choices=commands
    )

    return subparser
