#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from optparse import OptionParser

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
        parser.add_option('-d', '--dict'  , default='/Users/hitoshi/work/dev/shuka/dic/mod1000_shuka.dic', dest='dict_path', type='string')
        parser.add_option('-l', '--length', default=200, dest='length', type='int')
        (options, args) = parser.parse_args()
        self.dict_path = options.dict_path
        self.K = options.length

    def Summarize(self):
        ef = ExtractFeature.ExtractFeature()
        inst = Instantiate.Instantiate(self.dict_path)
        inst.CalculateSentenceWeights(ef.GetFeatures())
        #for weight in inst.GetSentenceWeights():
        #    print weight
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
