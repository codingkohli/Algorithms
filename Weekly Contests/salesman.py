#!/bin/python

import sys


def minimumTime(x):
    #sorting the times
    x = sorted(x)
    diffVal = []
    sum = 0
    for i in range(1,len(x)):
        temp = x[i] - x[i-1]
        sum += temp
    return sum

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        x = map(int, raw_input().strip().split(' '))
        result = minimumTime(x)
        print result

