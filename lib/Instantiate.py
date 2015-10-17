#!/usr/bin/python
# -*- coding: utf-8 -*-

class Instantiate:

    def __init__(self, dict_path):
        self.concept_weights = {}
        self.dict = {}
        self.ReadDictionary(dict_path)
        self.sentence_weights = []

    def ReadDictionary(self, dict_path):
        f = open(dict_path, 'r')
        for line in f.readlines():
            line = unicode(line, 'UTF-8')
            line = line.rstrip()
            (feature, weight) = line.split(u'\t')
            self.dict[feature] = weight

    def CalculateSentenceWeights(self, features):
        for feature in features:
            score = 0
            for key, value in feature.items():
                if key in self.dict:
                    score = score + float(value) * float(self.dict[key])
            self.sentence_weights.append(score)

    def CalculateConceptWeights(self, features):
        for feature in features:
            for key, value in feature.items():
                if key in self.dict:
                    score = score + float(value) * float(self.dict[key])
            self.concept_weights[feature] = score

    def GetConceptWeights(self):
        return self.concept_weights

    def GetSentenceWeights(self):
        return self.sentence_weights

if __name__ == '__main__':
    pass
