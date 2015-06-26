#!/usr/bin/env python

import sys

for line in sys.stdin:
    for word in line.split():
        print '%s\t%s' % (word, 1)
