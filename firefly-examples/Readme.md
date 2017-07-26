# Firefly Examples

Example programs to demonstate the capabilities of [Firefly][1].

[1]: https://github.com/rorodata/firefly

## Classic Unix Utilities

The `unix.py` has classic unix utilities.

Run it as a service using:

	$ firefly unix.fortune unix.banner unix.cowsay unix.cowthink
	http://127.0.0.1:8000/

Use it using the client.

	>>> import firefly
	>>> unix = firefly.Client("http://127.0.0.1:8000/")	
	>>> print(unix.cowsay(message="Firefly!"))
	 __________
	< Firefly! >
	 ----------
	        \   ^__^
	         \  (oo)\_______
	            (__)\       )\/\
	                ||----w |
	                ||     ||


	>>> print(unix.banner(message="Firefly"))
	#######                                                   ###
	#           #    #####   ######  ######  #        #   #   ###
	#           #    #    #  #       #       #         # #    ###
	#####       #    #    #  #####   #####   #          #      #
	#           #    #####   #       #       #          #
	#           #    #   #   #       #       #          #     ###
	#           #    #    #  ######  #       ######     #     ###

	>>> print(unix.fortune())
	Q:	What's tiny and yellow and very, very, dangerous?
	A:	A canary with the super-user password.
