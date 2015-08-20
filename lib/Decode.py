#!/usr/bin/python
# -*- coding: utf-8 -*-

def decode(length, K, n, weight):
    
    # Initialize
    insert   = [[False for k in range(0, K + 2)]for i in range(0, n + 2)]
    score    = [[0 for k in range(0, K + 2)]for i in range(0, n + 2)]
    solution = [False for i in range(0, n + 2)]
    
    # Loop
    for i in range(1, n + 1):
        for k in range(1, K + 1):
            if length[i] <= k and score[i-1][k] <= score[i-1][k-length[i]] + weight[i]:
                insert[i][k] = True
                score[i][k]  = score[i-1][k-length[i]] + weight[i]
            else:
                score[i][k]  = score[i-1][k]
            #print '%d %d ' % (i, k),
            #print insert[i][k],
            print score[i][k],
        print ''

    # Trace
    k = K
    for i in range(n, 0, -1):
        if insert[i][k] == True:
            k = k - length[i]
            solution[i] = True

    return solution


length = (None, 5, 3, 1, None)
weight = (None, 4, 3, 2, None)

K = 7
n = 3

print decode(length, K, n, weight)
