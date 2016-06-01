# -*- coding: utf-8 -*-

import os
from os.path import join, dirname

from setuptools import setup, find_packages

from version import get_version

os.umask(18)  # octal 022

setup(
    name='etherpad_lite',
    version=get_version(),
    description='Python interface for Etherpad-Lite\'s HTTP API',
    author='Changaco',
    author_email='changaco ατ changaco δοτ net',
    url='http://changaco.net/gitweb/?p=python-etherpad_lite.git',
    license='CC0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
)
