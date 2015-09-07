#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from optparse import OptionParser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import Decode
import ExtractFeature
import Format
import Instantiate

class Shuca:

    def __init__(self):
    
        parser = OptionParser()
        parser.add_option('-d',
                          '--dict',
                          default=os.path.dirname(os.path.abspath(__file__)) + '/../dic/weight.dic',
                          dest='dict_path',
                          type='string')
        parser.add_option('-l',
                          '--length',
                          default=200,
                          dest='length',
                          type='int')
        parser.add_option('-s',
                          '--sent',
                          action='store_true',
                          default=False,
                          dest='length_by_sentence')
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
    sh = Shuca()
    sh.Summarize()
