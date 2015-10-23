#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

class DecodeGreedyCoverage:

    def __init__(self, length, K, n, vectors, weight):
        self.K       = K
        self.length  = length
        self.n       = n
        self.vectors = vectors
        self.weight  = weight
        
        self.__MakeSentences(length, n, vectors, weight)

    def __MakeSentences(self, length, n, vectors, weight):
        self.sentences = []
        for i in range(1, n + 1):
            sentence = Sentence(i, length[i], vectors[i], weight)
            self.sentences.append(sentence)

    def __UpdateSentenceWeight(self, weight):
        for sentence in self.sentences:
            sentence.score = sentence.CalculateScore(sentence.term_vector,
                                                     weight)

    def __UpdateWeight(self, weight):
        for key, value in self.current_sentences.term_vector.items():
            weight[key] = 0
        return weight

    def GetScore(self):
        return self.current_sentences.GetScore()

    def GetSolution(self):
        solution = [False for i in range(0, self.n + 1)]
        for i in self.current_sentences.id:
            solution[i] = True
        solution[0] = False
        return solution

    def Search(self):
        self.current_sentences = Sentence(0, 0, {}, {})
        weight = copy.deepcopy(self.weight)
        while len(self.sentences) > 0:
            self.sentences.sort()
            sentence = self.sentences.pop()
            if sentence.length + self.current_sentences.length <= self.K:
                self.current_sentences.Update(sentence, self.weight)
            weight = self.__UpdateWeight(weight)
            self.__UpdateSentenceWeight(weight)

class Sentence:
    def __init__(self, id, length, term_vector, weight):
        self.id          = [id]
        self.length      = length
        self.term_vector = term_vector
        self.score       = self.CalculateScore(term_vector, weight)

    def __cmp__(self, other):
        if self.score > other.score:
            return 1
        elif self.score < other.score:
            return -1
        else:
            return 0

    def CalculateScore(self, term_vector, weight):
        score = 0
        for key, value in term_vector.items():
            score = score + weight[key]
        return score

    def GetScore(self):
        return self.score

    def Update(self, sentence, weight):
        self.id.extend(sentence.id)
        self.length = self.length + sentence.length
        self.term_vector.update(sentence.term_vector)
        self.score  = self.CalculateScore(self.term_vector, weight)

if __name__ == '__main__':
    length  = [0, 6, 5, 4]
    K       = 11
    n       = 3
    vectors = [{},
               {'a':1, 'b':1},
               {'b':1, 'c':1},
               {'a':1, 'c':1}]
    weight  = {'a':10, 'b':5, 'c':2, 'd':'7'}
    dgc = DecodeGreedyCoverage(length, K, n, vectors, weight)
    dgc.Search()
    #solution = dgc.GetSolution()
    print dgc.GetScore()
    print dgc.GetSolution()

