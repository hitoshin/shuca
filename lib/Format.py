#!/usr/bin/python
# -*- coding: utf-8 -*-

class Format:

    def __init__(self, sentences, solution):
        self.sentences = sentences
        self.solution  = solution

    def FormatSummary(self, options):
        if options.verbose == True:
            print 'Maximum Length: %d' % (options.length)
        for i in range(0, len(self.solution)):
            if self.solution[i] == True:
                if options.verbose == True:
                    print '%d: %s' % (i, self.sentences[i].encode('utf-8'))
                else:
                    print self.sentences[i].encode('utf-8')
