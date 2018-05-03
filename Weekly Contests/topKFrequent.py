from heapq import heappush, heappop


class Solution(object):
    def topKFrequent(self, words, k):
        import heapq
        if not words:
            return []
        outRes = []
        hashDict = {}
        for word in words:
            try:
                hashDict[word] += 1
            except:
                hashDict[word] = 1

        heapWords = []
        # pushing the elements in the heap
        for var in hashDict.keys():
            heappush(heapWords, (-hashDict[var], var))

        # popping the elements from heap
        for i in range(k):
            outRes.append(heappop(heapWords)[1])

        return outRes
