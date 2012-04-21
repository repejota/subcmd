.. _tutorial:

========
Tutorial
========

The most simple example use of **subcmd** is a class that inherits from
:class:`subcmd.app.App` base object. Then ( and by default ), all methods 
of this created class which starts with prefix "*do\_*" will be available 
as subcommands.

With :meth:`subcmd.decorators.option` and :meth:`subcmd.decorators.arg`
decorators you can add positional arguments and valued options to each command.

For example:

::

    from subcmd.app import App
    from subcmd.decorators import option
    from subcmd.decorators import arg

    class Application(App):
        """a description of the example app"""
        name = 'example'
        version = '0.1'
        default_args = ['--help']

        @option('--log', '-l', action='store_true', help='log foo is on')
        def do_foo(self, options):
            """help text for foo subcommand"""
            print options

        @option('-f', '--force', action='store_true', help='force bar execution')
        def do_bar(self, options):
            """help text for bar subcommand"""
            print options

    if __name__ == "__main__":
        app = Application()
        app.cmdline()

Executing this script with no command line arguments will output:

::

    $ python example.py

    usage: example.py [-h] [-v] {foo,bar} ...

    a description

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version

    subcommands:
      valid subcommands

      {foo,bar}      additional help
        bar          help text for bar subcommand
        foo          help text for foo subcommand

    an epilog

You can see how if no argument is specified an automatic usage help message
is shown.

Also all docstrings definint both class object and every method starting with
"do\_" are converted to help descriptions for each command.

Finally **subcmd** ads by default some arguments that are common on all CLI
based tools like ``--version`` ( wich shows the version string of your tool ) and
``--help`` ( wich generates the same usage message you see if no command line
arguments are specified ).

**subcmd** provides a lot of more features and customization options, refer to
the detailed :ref:`manual <manual>` for more information.

:ref:`Next: Complete Manual <manual>`