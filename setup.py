#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "python-tdlib",
    version = "1.2.0",
    author = "andrew-ld",
    license = "MIT",
    url = "https://github.com/andrew-ld/python-tdlib",
    packages = ["py_tdlib", "py_tdlib.constructors", "py_tdlib.factory"],
    install_requires = ["werkzeug", "simplejson"],
)
