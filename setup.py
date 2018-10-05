#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "python-tdlib",
    version = "1.0",
    author = "andrew-ld",
    license = "MIT",
    url = "https://github.com/andrew-ld/python-tdlib",
    packages = ["py_tdlib"],
    install_requires = ["werkzeug", "simplejson"]
)
