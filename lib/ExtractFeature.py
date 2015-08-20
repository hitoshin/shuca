#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys

class ExtractFeature:

    def __init__(self):

        self.features  = [{}]
        self.lengths   = [0]
        self.sentences = ['']

        self.lines     = []
        self.n         = 0

        self.c_pattern = re.compile(u'^名詞|^動詞|^形容詞')
        self.s_pattern = re.compile(u'^\#')
        self.b_pattern = re.compile(u'^\*')
        self.p_pattern = re.compile(u'^\+')
        self.e_pattern = re.compile(u'^EOS')
        self.w_pattern = re.compile(u'^(\S+) (\S+) (\S+) (\S+) ')

    def ReadInput(self):

        for line in sys.stdin:
            line = unicode(line, 'UTF-8')
            line = line.rstrip()
    
            s_match = self.s_pattern.match(line)
            if s_match != None:
                self.n = self.n + 1
            self.lines.append(line)

    def ExtractFeatureVector(self):

        i = 0

        for line in self.lines:

            s_match = self.s_pattern.match(line)
            b_match = self.b_pattern.match(line)
            p_match = self.p_pattern.match(line)
            e_match = self.e_pattern.match(line)
   
            if s_match != None:
                i = i + 1
                self.features.append({})
                self.lengths.append('')
                self.sentences.append('')
                if i == 1:
                    self.features[i]['is_lead'] = 1
            elif b_match != None:
                pass
            elif p_match != None:
                pass
            elif e_match != None:
                self.lengths[i] = len(self.sentences[i])
            else:
                w_match = self.w_pattern.match(line)
                if w_match:
                    surface = w_match.group(1)
                    pos     = w_match.group(4)
                    self.sentences[i] = self.sentences[i] + surface

                    self.features[i]['abs_pos'] = i
                    self.features[i]['rel_pos'] = float(i) / self.n

                    c_match = self.c_pattern.match(pos)
                    if c_match:
                        self.features[i]['s:%s' % (surface)] = 1

    def GetFeatures(self):
        return self.features
    
    def GetLengths(self):
        return self.lengths
    
    def GetN(self):
        return self.n
    
    def GetSentences(self):
        return self.sentences

    def GetResults(self):
        return self.features, self.lengths, self.n, self.sentences

ef = ExtractFeature()
ef.ReadInput()
features, lengths, n, sentences = ef.ExtractFeatureVector()
for i in range(0, len(sentences)):
    print '%d %s %d' % (i, sentences[i], lengths[i])
    for key, value in features[i].items():
        print '%s %f' % (key, value)
