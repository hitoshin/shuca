#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys

indentation_pattern = re.compile(u'^　')
reporter_pattern = re.compile(u'(?:^【.+?】|【.+?】$)')

body = unicode(sys.stdin.read().rstrip(), 'utf-8')
buffer = ''
sentences = []
p_flag = False

for i in range(0, len(body)):
    c = body[i:i+1]
    if c != u'\n':
        buffer = buffer + c
    if c == u'。' and p_flag == False:
        sentences.append(buffer)
        buffer = ''
    if c == u'「':
        p_flag = True
    if c == u'」' and p_flag == True:
        p_flag = False
        if body[i+1:i+2] == u'\n':
            sentences.append(buffer)
            buffer = ''

for sentence in sentences:
    sentence = indentation_pattern.sub('', sentence)
    sentence = reporter_pattern.sub('', sentence)
    if sentence != '':
        print '%s' % (sentence.encode('utf-8'))
