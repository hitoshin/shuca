#!/usr/bin/python
# -*- coding: utf-8 -*-

class Decode:
    
    def __init__(self, length, K, n, weight):
        self.K        = K
        self.length   = length
        self.n        = n
        self.weight   = weight
    
        self.solution = [False for i in range(0, n + 1)]
    
    def Search(self, ):
    
        # Initialize
        insert   = [[False for k in range(0, self.K + 2)]for i in range(0, self.n + 2)]
        score    = [[0 for k in range(0, self.K + 2)]for i in range(0, self.n + 2)]
    
        # Loop
        for i in range(1, self.n + 1):
            for k in range(1, self.K + 1):
                if self.length[i] <= k and score[i - 1][k] <= score[i - 1][k - self.length[i]] + self.weight[i]:
                    insert[i][k] = True
                    score[i][k]  = score[i - 1][k - self.length[i]] + self.weight[i]
                else:
                    score[i][k]  = score[i - 1][k]

        # Trace
        k = self.K
        for i in range(self.n, 0, -1):
            if insert[i][k] == True:
                k = k - self.length[i]
                self.solution[i] = True

    def GetSolution(self):
        return self.solution

if __name__ == '__main__':
    pass
