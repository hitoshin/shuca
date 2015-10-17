#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    def GetSolution(self):
        solution = [False for i in range(0, self.n + 1)]
        for i in self.current_sentences.id:
            solution[i] = True
        solution[0] = False
        return solution

    def Search(self):
        self.current_sentences = Sentence(0, 0, {}, {})
        while len(self.sentences) > 0:
            self.sentences.sort()
            sentence = self.sentences.pop()
            if sentence.length + self.current_sentences.length <= self.K:
                self.current_sentences.Update(sentence, self.weight)

class Sentence:
    def __init__(self, id, length, term_vector, weight):
        self.id          = [id]
        self.length      = length
        self.term_vector = term_vector
        self.score       = self.__CalculateScore(term_vector, weight)

    def __cmp__(self, other):
        if self.score > other.score:
            return 1
        elif self.score < other.score:
            return -1
        else:
            return 0

    def __CalculateScore(self, term_vector, weight):
        score = 0
        for key, value in term_vector.items():
            score = score + weight[key]
        return score

    def Update(self, sentence, weight):
        self.id.extend(sentence.id)
        self.length = self.length + sentence.length
        self.term_vector.update(sentence.term_vector)
        self.score  = self.__CalculateScore(self.term_vector, weight)

if __name__ == '__main__':
    length  = [0, 6, 5, 4]
    K       = 10
    n       = 3
    vectors = [{},
               {'a':1, 'b':1},
               {'b':1, 'c':1},
               {'a':1, 'c':1}]
    weight  = {'a':10, 'b':5, 'c':2, 'd':'7'}
    dgc = DecodeGreedyCoverage(length, K, n, vectors, weight)
    dgc.Search()
    print dgc.GetSolution()
