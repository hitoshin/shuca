#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys

indentation_pattern = re.compile(u'^　')
reporter_pattern = re.compile(u'^【.+?】')

for line in sys.stdin:
    line = unicode(line, 'utf-8')
    line = line.rstrip()
    array = line.split(u'。')
    for sentence in array:
        if sentence != '':
            sentence = indentation_pattern.sub('', sentence)
            sentence = reporter_pattern.sub('', sentence)
            print '%s%s' % (sentence.encode('utf-8'), '。')
