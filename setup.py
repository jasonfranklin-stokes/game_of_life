#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Some documentation"""

__author__ = "Jason"
__copyright__ = "Copyright 2018, Jason"
__credits__ = ["Jason's mates"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jason"
__email__ = "jason@jasonsemail.com"
__status__ = "experimental"

from setuptools import setup, find_packages

setup(
    name="Game of Life",
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
