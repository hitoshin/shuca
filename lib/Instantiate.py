#!/usr/bin/python
# -*- coding: utf-8 -*-

class Instantiate:

    def __init__(self, dict_path):
        self.dict = {}
        self.ReadDictionary(dict_path)
        self.sentence_weights = [0]

    def ReadDictionary(self, dict_path):
        f = open(dict_path, 'r')
        for line in f.readlines():
            line = unicode(line, 'UTF-8')
            line = line.rstrip()
            (feature, weight) = line.split('\t')
            self.dict[feature] = weight

    def CalculateSentenceWeights(self, features):
        for feature in features:
            for key, value in feature.items():
                print key, value

dict_path = '/Users/hitoshi/work/dev/shuka/dic/weight.dic'
inst = Instantiate(dict_path)
