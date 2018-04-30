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
import sys
from mock import patch, MagicMock

from riverstone_cli.commands.base import Command
from riverstone_cli.__main__ import main


class MockCommand(Command):
    """MockCommand for testing
    """
    def __init__(self):
        """Setup subparser and other attributes
        """
        self.name = "test"
        self.sub_commands = {
            'hello': MagicMock(),
        }

    def handler(self, args):
        """Handle issue commands.
        """
        sub_command = args['sub_command'].pop(0)
        self.sub_commands.get(sub_command)(args)


def test_main():
    """ Unit test for Main function
    """
    mock_commands = {
        "test": MockCommand()
    }

    testargs = ["rs", "test", "hello"]
    with patch.object(sys, 'argv', testargs):
        with patch('riverstone_cli.__main__.COMMANDS', mock_commands):
            assert isinstance(main(), type(None))
