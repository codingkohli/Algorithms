"""
Codeforces round 519: warmup question
"""

num = int(input())
lst = input().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
sumVotes = sum(lst)
outRes = 2*sumVotes
outRes = int(outRes/num) + 1
lstMax = max(lst)
outRes = max(outRes,lstMax)
print(outRes)