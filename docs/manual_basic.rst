.. _manual_basic:

===========
Basic Usage
===========

**subcmd** can be used either subclassing :class:`subcmd.app.App` class or directly calling
its methods as a builder.

Inherited Class
===============

In inherited class mode just create a class that inherits from :class:`subcmd.app.App`. To
customize this class just override its constructor and set the proprerties as you like.

We will see how to customize this inherited class on next chapter.

Here is the simples example tool that you can build using inherited class.

::

    from subcmd.app import App

    class Application(App):
        pass

    if __name__ == "__main__":
        app = Application()
        app.cmdline()

Builder API
===========

In builer mode instanciate main :class:`subcmd.app.App` class. This object provides an full API
to build appending commands to it, customizing them settings properties as you build your tool.

We will see how to build an complete tool using :class:`subcmd.app.App` API on next chapter.

Here is the simplest example tool that you can build using builder API.

::

	from subcmd.app import App

	if __name__ == "__main__":
		app = App()
		app.cmdline()

Executing both scripts will show the same output, a default usage help message like this:

::

    usage: example_inherited.py [-h] [-v] {} ...

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version

    subcommands:
      valid subcommands

      {}             additional help

Customizing Inherited Class
===========================

When defining inherited class you can customize it and provide some information for your
tool.

For now available options are:

name
  The program name.

description
  The program description ( one line should be fine ).

version
  The program version.

epilog
  An epilog to show at the end of usage help message.

::

    class Application(App):
        name = "myapp"
        description = "My cli application"
        version = "0.2"
        epilog = "CLI rocks!"


    if __name__ == "__main__":
        app = Application()
        app.cmdline()

Customizing Builder
===================

If you use the builder interface just pass the same options as an arguments to the :class:`subcmd.app.App` constructor:

::

  from subcmd.app import App

  if __name__ == "__main__":
    app = App(name="myapp",
              description="My cli application",
              version="0.2",
              epilog="CLI rocks!")
    app.cmdline()

Executing both scripts will show the same output, a default usage help message like this:

::

    usage: myapp.py [-h] [-v] {} ...

    My cli application

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version

    subcommands:
      valid subcommands

      {}             additional help

    CLI rocks!

Next we are going to see how to work with arguments, specifically the default arguments that
every tool will have.

This arguments are setted up automatically by :class:`subcmd.app.App` class and you don't
need to do anything to use them.

:ref:`Next: Default optional arguments <manual_defaults>`
