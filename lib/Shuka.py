#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from optparse import OptionParser

sys.path.append('/Users/hitoshi/work/dev/shuka/lib')

import Decode
import ExtractFeature
import Format
import Instantiate

class Shuka:

    def __init__(self):
        #self.dict_path = '/Users/hitoshi/work/dev/shuka/dic/weight.dic'
        #self.dict_path = '/Users/hitoshi/work/dev/shuka/dic/mod1000_shuka.dic'
        #self.K = 200
    
        parser = OptionParser()
        parser.add_option('-d', '--dict',   default='/Users/hitoshi/work/dev/shuka/dic/mod1000_shuka_b.dic', dest='dict_path', type='string')
        parser.add_option('-l', '--length', default=200, dest='length', type='int')
        parser.add_option('-s', '--sent',   action='store_true', default=False, dest='length_by_sentence')
        (options, args) = parser.parse_args()
        self.dict_path = options.dict_path
        self.K = options.length
        self.length_by_sentence = options.length_by_sentence

    def Summarize(self):
        ef = ExtractFeature.ExtractFeature(self.length_by_sentence)
        inst = Instantiate.Instantiate(self.dict_path)
        inst.CalculateSentenceWeights(ef.GetFeatures())
        dc = Decode.Decode(ef.GetLengths(),
                           self.K,
                           ef.GetN(),
                           inst.GetSentenceWeights())
        dc.Search()
        fm = Format.Format(ef.GetSentences(),
                           dc.GetSolution())
        fm.FormatSummary()

if __name__ == '__main__':
    sh = Shuka()
    sh.Summarize()
