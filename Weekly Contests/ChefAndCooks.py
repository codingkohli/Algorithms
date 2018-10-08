"""
Code Chef : October Challenge
Chef and Serves : CHSERVE

"""

import sys

T = int(input())
for i in range(T):
    chef, cook, K = [int(val) for val in input().split()]
    totScore = chef+cook
    if totScore == 0:
        print("CHEF")
    elif int(totScore/K) % 2 == 0:
        print("CHEF")
    else:
        print("COOK")
