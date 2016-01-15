#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from optparse import OptionParser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import Decode
import DecodeGreedyCoverage
import ExtractFeature
import Format
import Instantiate

class Shuca:

    def __init__(self):
    
        parser = OptionParser()
        parser.set_defaults(dict_path=os.path.dirname(os.path.abspath(__file__)) + '/../dic/weight.dic',
                            input_type='knp',
                            length=200,
                            length_by_sentence=False,
                            summarization_type='single',
                            verbose=False)
        parser.add_option('-d',
                          '--dict',
                          action='store',
                          dest='dict_path',
                          type='string')
        parser.add_option('-e',
                          '--english',
                          action='store_const',
                          const='eng',
                          dest='input_type')
        parser.add_option('-l',
                          '--length',
                          action='store',
                          dest='length',
                          type='int')
        parser.add_option('-m',
                          '--multi',
                          action='store_const',
                          const='multi',
                          dest='summarization_type')
        parser.add_option('-s',
                          '--sent',
                          action='store_true',
                          dest='length_by_sentence')
        parser.add_option('-v',
                          '--verbose',
                          action='store_true',
                          dest='verbose')
        (self.options, self.args) = parser.parse_args()

    def Summarize(self):
        if self.options.summarization_type == 'single':
            ef = ExtractFeature.ExtractFeature(self.options)
            inst = Instantiate.Instantiate(self.options.dict_path)
            inst.CalculateSentenceWeights(ef.GetFeatures())
            dc = Decode.Decode(ef.GetLengths(),
                               self.options.length,
                               ef.GetN(),
                               inst.GetSentenceWeights())
            dc.Search()
            fm = Format.Format(ef.GetSentences(),
                               dc.GetSolution())
            fm.FormatSummary(self.options)
        elif self.options.summarization_type == 'multi':
            ef = ExtractFeature.ExtractFeature(self.options)
            #inst = Instantiate.Instantiate(self.options.dict_path)
            #inst.CalculateConceptWeights(ef.GetFeatures())
            dc = DecodeGreedyCoverage.DecodeGreedyCoverage(ef.GetLengths(),
                                                           self.options.length,
                                                           ef.GetN(),
                                                           ef.GetFeatures(),
                                                           ef.GetTermDic())
            dc.Search()
            fm = Format.Format(ef.GetSentences(),
                               dc.GetSolution())
            fm.FormatSummary(self.options)

if __name__ == '__main__':
    sh = Shuca()
    sh.Summarize()
