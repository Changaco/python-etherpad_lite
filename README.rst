Etherpad Lite is a web service that allows real-time document collaboration for groups of users. http://etherpad.org/

python-etherpad_lite provides an interface for Etherpad-Lite's HTTP API.

Installation
============

	pip install etherpad_lite

python-etherpad_lite doesn't have dependencies and is compatible with both python 2 and 3.

Usage
=====

From python::

	from etherpad_lite import EtherpadLiteClient
	c = EtherpadLiteClient(base_params={'apikey':'secret_from_APIKEY.txt'})
	c.createPad(padID='test', text="Lorem ipsum dolor sit amet.")

From the command line::

	$ python -m etherpad_lite -p apikey=secret_from_APIKEY.txt
	=> Welcome to the Etherpad Lite shell !
	=> Command example: createPad padID=test text="Lorem ipsum dolor sit amet."
	% createPad padID=test text="Lorem ipsum dolor sit amet."
	ok
	% getHTML padID=test
	{u'html': u'Lorem ipsum dolor sit amet.<br>'}
	% deletePad padID=test
	ok

See the documentation of Etherpad Lite (https://github.com/Pita/etherpad-lite) for the list of API functions and their arguments.

License
=======

LGPLv3+
