#
## BEGIN LICENSE BLOCK
#
# Copyright (c) <2012-2014>, Raul Perez <repejota@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
## END LICENSE BLOCK
#

import sys
import argparse

from subcmd import base


class App(object):
    """CLI object entry point.

    Implements a Hippocampus entry point command that accepts options and
    arguments.
    All methods starting with "do" will become callable as a subcommands and
    will accept options and/or arguments defined as decorators.

    Example:::

        from subcmd.app import App

        class Application(App):
            \"""a description of the example app\"""
            pass

        if __name__ == "__main__":
            app = Application()
            app.cmdline()

    Another example:::

        from subcmd.app import App

        if __name__ == "__main__":
                app = App()
                app.cmdline()
    """

    __metaclass__ = base.SubCommand

    def __init__(self, name=None, description=None, version=None, epilog=None,
                 *args, **kwargs):
        """Application constructor"""

        # The program name
        self.__name = name

        # The program description
        self.__description = description

        # The program version
        self.__version = version

        # The program epilog
        self.__epilog = epilog

        # Default arguments
        self.__default_args = ['--help']

    @property
    def name(self):
        """Get Application's name"""
        if not self.__name:
            return self.__class__.__name__
        return self.__name

    @property
    def description(self):
        """Get Application's description"""
        if not self.__description:
            return u"%s's description" % self.name
        return self.__description

    @property
    def epilog(self):
        """Get Application's epilog"""
        if not self.__epilog:
            return u"%s's epilog" % self.name
        return self.__epilog

    @property
    def version(self):
        """Get current application version"""
        if not self.__version:
            return 0
        return self.__version

    def add_command(self, name, command_func):
        """Adds a new command"""
        self._argparse_subcmds[name]={'name': name, 'func': command_func, 'options': []}

    def remove_command(self, name):
        """Removes an existing command"""
        if name in self._argparse_subcmds:
            del self._argparse_subcmds[name]

    def list_commands(self):
        """Adds a new command"""
        return self._argparse_subcmds.keys()

    def cmdline(self):
        """Parsing cmdline and execution method.

        This class parses input from command line interface to extract the
        command, subcommands and arguments.
        It is also responsible for adding some default arguments for each
        command like:

            * -v or ---version
            * -h or ---help

        These arguments come already implemented by default and will be
        available automatically to any command and subcommand is implemented.

        :returns: None
        """

        # Builds main argparse structrure
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=self.description,
            epilog=self.epilog,
        )

        # Default arg --version
        parser.add_argument('-v', '--version', action='version',
                            version='%s %s' % (self.name, self.version))

        # Builds a secondary parser to implement subcommands
        subparsers = parser.add_subparsers(
            title='subcommands',
            description='valid subcommands',
            help='additional help',
        )

        for name in sorted(self._argparse_subcmds.keys()):
            subcmd = self._argparse_subcmds[name]
            subparser = subparsers.add_parser(subcmd['name'],
                                              help=subcmd['func'].__doc__)
            for args, kwds in subcmd['options']:
                subparser.add_argument(*args, **kwds)
            subparser.set_defaults(func=subcmd['func'])

        # If we have no no arguments parse default.
        if len(sys.argv) <= 1:
            options = parser.parse_args(self.__default_args)
        else:
            options = parser.parse_args()

        options.func(self, options)
