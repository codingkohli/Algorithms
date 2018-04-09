"""Leetcode problem : 127 Word Ladder"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if len(beginWord) != len(endWord):
            return 0
        hashMap = {}
        for word in wordList:
            hashMap[word] = 10000
        if endWord not in hashMap.keys():
            return 0
        queue = []
        hashMap[beginWord] = 1
        queue.append(beginWord)
        while queue:
            tempWord = queue[0]
            del queue[0]
            step = hashMap[tempWord]
            # wrdLst = [ch for ch in tempWord]
            for i in range(len(tempWord)):
                for j in range(ord('a'), ord('z') + 1):
                    # tempLst[i] = chr(j)
                    # newWord = ''.join(tempLst)
                    newWord = tempWord[:i] + chr(j) + tempWord[i + 1:]
                    try:
                        prevDist = hashMap[newWord]
                        if newWord == endWord:
                            return step + 1
                        if prevDist > step + 1:
                            hashMap[newWord] = step + 1
                            queue.append(newWord)
                    except:
                        pass

        if hashMap[endWord] == 10000:
            return 0
        else:
            return hashMap[endWord]