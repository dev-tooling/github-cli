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
from riverstone_cli.common.utils import setup_subparser


class Command(object):
    """Base class for all commands
    """
    name = None
    sub_commands = []
    subparser = None

    def handler(self, args):
        """Handler for execution when command is issued
        """
        pass

    def register_opts(self):
        """Initiate registration of options.
        """
        self.subparser = setup_subparser(
            self.name,
            'Wireframe related tasks.',
            self.sub_commands
        )

        self._register_opts()

    def _register_opts(self):
        pass
