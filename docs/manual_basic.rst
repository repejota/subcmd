===========
Basic Usage
===========

**subcmd** can be used either subclassing :class:`subcmd.app.App` class or directly calling
its methods as a builder.

Inherited Class
===============
::

    from subcmd.app import App

    class Application(App):
        pass

    if __name__ == "__main__":
        app = Application()
        app.cmdline()

Builder API
===========
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