.. _manual_options:

========================================
Defining Command Line Optional Arguments
========================================

Now we have commands in our CLI tool its time to add some modificators to
them. With **subcmd** adding modificators means to append *arguments* to one
or more commands.

There is two types or argugments in **subcmd**, *optional arguments* or
*options* and *parameters* or *arguments*.

In this chapter we will cover the first kind of arguments.

Command Line Optional Arguments are also called *flags* or *switches* beacuse
its pourpose is to modify the operation of a command.


Command Line Optional Arguments in inherited mode
=================================================

If you are using inherited mode in **subcmd** adding optional arguments
involves python decorators.

Lets take the example command we added in the previous chapter and modify its
operation adding an optional argument.

::

    from subcmd.app import App

    class Application(App):
            name = "myapp"
            description = "My cli application"
            version = "0.2"
            epilog = "CLI rocks!"

            def do_action(self, options):
                    """Action subcommand"""
                    print "execute action!"

    if __name__ == "__main__":
            app = Application()
            app.cmdline()

Image we want to add a flag that when its active no out will be printed to
stdout. To add this optional argument we need to decorate our created
*do_action* command like this:

::

    from subcmd.decorators import option

    @option('-q', '--quiet',
            action='store_true',
            help='Quiet mode, no print to stdout')
    def do_action(self, options):
            """Action subcommand"""
            print "execute action!"

*@option* decorator uses the same arguments than Python's
:py:meth:`argparse.add_argument` method wich are:

.. method:: @option.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

Define how a single command-line argument should be parsed. Each parameter has
its own more detailed description below, but in short they are:

name or flags
    Either a name or a list of option strings, e.g. foo or -f, --foo.
action
    The basic type of action to be taken when this argument is encountered
    at the command line.
nargs
    The number of command-line arguments that should be consumed.
const
    A constant value required by some action and nargs selections.
default
    The value produced if the argument is absent from the command line.
type
    The type to which the command-line argument should be converted.
choices
    A container of the allowable values for the argument.
required
    Whether or not the command-line option may be omitted (optionals only).
help
    A brief description of what the argument does.
metavar
    A name for the argument in usage messages.
dest
    The name of the attribute to be added to the object returned by
    parse_args().

Command Line Optional Arguments in builder mode
===============================================

Adding command line optional arguments in builder mode is quite similar to
the inherited mode.

Consider this example:

::

    from subcmd.app import App

    def do_action(self, options):
        """Action subcommand"""
        print "execute action!"

    if __name__ == "__main__":
        app = App(name="myapp",
                  description="My cli application",
                  version="0.2",
                  epilog="CLI list!")

        app.add_command("action", do_action)
        for method_name in app.list_commands():
            print method_name
        app.remove_command("action")
        app.cmdline()

To add an optional argument you should use the :class:`subcmd.app.App` API like
this:

::

    app.option("action", "-q", "--quiet", action='store_true',
               help='Quiet mode, no print to stdout')
