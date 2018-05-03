from heapq import heappush, heappop


class Solution(object):
    def topKFrequent(self, nums, k):
        if not nums:
            return []
        outRes = []
        hashDict = {}
        for num in nums:
            try:
                hashDict[num] += 1
            except:
                hashDict[num] = 1
        heapElem = []
        outRes = []
        # pushing the elements in the heap
        for var in hashDict.keys():
            heappush(heapElem, (-hashDict[var], var))

        for i in range(k):
            outRes.append(heappop(heapElem)[1])

        return outRes



