====================
Defining SubCommands
====================

**subcmd** a python module for easily bulding multi-command scripts. So the
main pourpose of this tool is to be able to implement a subcommand pattern wraped
in a CLI interface.

Subcommand pattern follows this call format:

::

    [command] [subcommand] [options] [arguments]

And an example call could be one like this one:

::

	myapp action --verbose file.json

Where *mytool* is our CLI interface program, *do_action* is the subcommand and *--verbose*
and *file.json* both are arguments, one of them optional ( *--verbose* ).

Defining Subcommands in intherited mode
=======================================

Staring from the previous example of inherited class mode:

::

    from subcmd.app import App

    class Application(App):
        name = "myapp"
        description = "My cli application"
        version = "0.2"
        epilog = "CLI rocks!"

    if __name__ == "__main__":
        app = Application()
        app.cmdline()

A subcommand is defined by adding a method to this class which its name starts with *do_*.
By default all methods starting with this prefix will be converted to commands.

For example:

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

If you execute again your tool you will see how the new command is shown and is available.

::

	usage: example_inherited.py [-h] [-v] {action} ...

	My cli application

	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --version

	subcommands:
	  valid subcommands

	  {action}       additional help
	    action       Action subcommand

	CLI rocks!

And if you execute your action you will see its results:

::

	python example_inherited.py action
	execute action!

Defining Subcommands in builder mode
====================================

Taking as reference again the past example:

::

    from subcmd.app import App

    if __name__ == "__main__":
        app = App(name="myapp",
                  description="My cli application",
                  version="0.2",
                  epilog="CLI list!")
        app.cmdline()

:class:`subcmd.app.App` class provides methods to add, remove or list available
commands.

Adding a command
^^^^^^^^^^^^^^^^

.. method:: subcmd.app.App.add_command(self, name, command_func)

To add a new command call :meth:`subcmd.app.App.add_command` method and pass
a name and a callable to it.

Listing available commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. method:: subcmd.app.App.list_commands(self)

Listing all commands :meth:`subcmd.app.App.list_commands` will return all keys
( name of the commands ) available on the instancied class.

Removing an existing command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. method:: subcmd.app.App.remove_command(self, name)

To remove a command call :meth:`subcmd.app.App.remove_command` and pass a name
to it. If the command is available in the instancied class will be removed.

Example:

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

Not that we can add commands to our CLI tool, the next step is to add arguments
to them.

:ref:`Next: Defining Command Line Optional Arguments <manual_options>`
