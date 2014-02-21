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


def option(*args, **kwds):
    """
    Option decorator.

    Adds an argument or an option to this command.

    Example option:::

        @option('--log', '-l', action='store_true', help='log is on')
        def do_foo(self):
            # do something
            # ...
            pass

    Example argument:::

        @arg('package', help='package to be (un)installed'))
        def do_foo(self):
            # do something
            # ...
            pass

    """
    def _decorator(func):
        _option = (args, kwds)
        if hasattr(func, 'options'):
            func.options.insert(0, _option)
        else:
            func.options = [_option]
        return func
    return _decorator


arg = option


def option_group(*options):
    """
    Combines option decorators.

    Combines a number of options or arguments for a single command.
    When two or more commands use option and / or arguments in a common manner,
    we can combine in a single sentence to make it more easy and clear
    implementation.

    Example:::

        option_group common_options = (
            option ('--type','-t' action = 'store', help = 'Specify type')
            arg ('package ', help = 'package to be (a) installed')
            option ('--log', '-l', action = 'store_true', help = 'log is on ')
        )

        @option_group_common_options
        def do_foo(self):
            # do something
            # ...
            pass

    :returns: list - List of options and arguments
    """
    def _decorator(func):
        for option in options:
            func = option(func)
        return func
    return _decorator
