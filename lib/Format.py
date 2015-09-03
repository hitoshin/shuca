#!/usr/bin/python
# -*- coding: utf-8 -*-

class Format:

    def __init__(self, sentences, solution):
        self.sentences = sentences
        self.solution  = solution

    def FormatSummary(self):
        for i in range(0, len(self.solution)):
            if self.solution[i] == True:
                print self.sentences[i].encode('utf-8')
