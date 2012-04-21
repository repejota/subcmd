.. _manual_defaults:

==========================
Default optional arguments
==========================

At this moment just built a command line tool but it has no commands implemented so its quite 
useless.

But, perhaps you noticed on this simple example that there is always available two optional arguments, 
*help* and *version*. These, are the default optional arguments that every tool will have.

Each one can be called both in condensed way ( -h and -v ) or in full way ( --help and --version )
there will be no difference between them.

Help ( -h and --help )
----------------------

Help is a default optional argument used to show the basic usage message that are you seeing after executing the tool and to provide help and information of every command implemented.
We will cover it in depth later.

Calling help as an extended argument:

::

	$ python myapp.py --help
	usage: myapp.py [-h] [-v] {} ...

	My cli application

	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --version

	subcommands:
	  valid subcommands

	  {}             additional help

	CLI rocks!

Calling help as a condensed argument:

::

	$ python myapp.py --h
	usage: myapp.py [-h] [-v] {} ...

	My cli application

	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --version

	subcommands:
	  valid subcommands

	  {}             additional help

	CLI rocks!	

Version ( -v and --version )
----------------------------

Version is a default optional argument used to show the actual tool's version number.

Calling help as an extended argument:

::

	$ python myapp.py --version
	myapp 0.2

Calling help as an condensed argument:

::

	$ python myapp.py -v
	myapp 0.2	