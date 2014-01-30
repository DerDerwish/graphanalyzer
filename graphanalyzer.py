#! /usr/bin/python3
# -- coding: utf-8 --

import sys
import json
from sys import argv

filename = argv[1]

# print usage
if filename == "--help":
    print("usage: graphanalyzer FILENAME")
    sys.exit(2)

# read file
data = json.load(open(filename, 'r'))
