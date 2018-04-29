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

from riverstone_cli.commands.base import Command


def _upload():
    pass


class WireframeCommand(Command):
    """WireframeCommand class defines the subcommands and logic for wireframe
    related tasks.
    """
    def __init__(self):
        """Setup subparser and other attributes
        """
        self.name = "wireframe"
        self.sub_commands = {
            'upload': _upload
        }

    def handler(self, args):
        """Handle issue commands.
        """
        sub_command = args['sub_command'].pop(0)
        self.sub_commands.get(sub_command)()
