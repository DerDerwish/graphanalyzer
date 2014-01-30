#! /usr/bin/python3
# -- coding: utf-8 --

import sys
from sys import argv

filename = argv[1]

# print usage
if filename == "--help":
    print("usage: graphanalyzer FILENAME")
    sys.exit(2)
