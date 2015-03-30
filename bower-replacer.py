#!/usr/bin/env python
import argparse
from replacer import ConfigReplacer

parser = argparse.ArgumentParser(description='Replace dependencies')
parser.add_argument('name', default='', help='Name of replaced package')
parser.add_argument('value', nargs='?', default='', help='Value to replace')
args = vars(parser.parse_args())

fname = 'bower.json'

replacer = ConfigReplacer(fname)
replacer.process(args['name'], args['value'])
