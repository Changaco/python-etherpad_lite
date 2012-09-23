Etherpad Lite is a web service that allows real-time document collaboration for groups of users. http://etherpad.org/

python-etherpad_lite provides an interface for Etherpad-Lite's HTTP API.

Installation
============

	pip install etherpad_lite

python-etherpad_lite doesn't have dependencies and is compatible with both python 2 and 3.

Usage
=====

Example::

	from etherpad_lite import EtherpadLiteClient
	c = EtherpadLiteClient(base_params={'apikey':'secret_from_APIKEY.txt'})
	c.createPad(padID='test', text="Lorem ipsum dolor sit amet.")

See the documentation of Etherpad Lite (https://github.com/Pita/etherpad-lite) for the list of API functions and their arguments.

License
=======

LGPLv3+
