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


class SubCommand(type):
    """
    This metaclass implements an entry point based on a standard
    command-subcommand in which any method belonging to a particular
    superclass that implements it and it starts with "do".

    The class methods that start with "do" will serve as command and by
    decorators and arg option subcommands can be implemented and pass data to
    these subcommands to be processed.

    Example:::

        class CommandTool(object):
            __metaclass__ = Subcommand
            name = "CommandTool"
            description = "A desc for CommandTool"
            epilog = "An epilog for CommandTool"

    :returns: object - A class implementing subcommands pattern.
    """

    def __new__(cls, classname, bases, classdict):
        """
        Class creation.

        Get all methods starting with "do" and put them available as commands.
        """

        # Default subcommands
        subcmds = {}

        for name, func in classdict.items():
            # If method starts with 'do_' is a command.
            if name.startswith('do_'):
                name = name[3:]
                subcmd = {
                    'name': name,
                    'func': func,
                    'options': []
                }
                # Get subcommand custom arguments
                if hasattr(func, 'options'):
                    subcmd['options'] = func.options
                subcmds[name] = subcmd

        classdict['_argparse_subcmds'] = subcmds
        return type.__new__(cls, classname, bases, classdict)
