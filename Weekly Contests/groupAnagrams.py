class Solution(object):
    def groupAnagrams(self, strs):
        if not str:
            return
        outRes = [[]]
        hashRes = {}

        # A helper function to get the hash
        def getHash(string):
            hashTemp = {}
            for s in string:
                try:
                    hashTemp[s] += 1
                except:
                    hashTemp[s] = 1
            return hashTemp

        # putting the first element in hashRes and outRes
        hashTemp = getHash(strs[0])
        outRes[0].append(strs[0])
        hashRes[strs[0]] = hashTemp

        # looping through the remaining elements and comparing it with others
        for ptr in range(1, len(strs)):
            string = strs[ptr]
            # getting the hash of the strings
            hashTemp = getHash(string)
            mFlag = False
            i = 0
            while (not mFlag) and (i < len(outRes)):
                if hashRes[outRes[i][0]] == hashTemp:
                    mFlag = True
                else:
                    i += 1
            if mFlag:
                outRes[i].append(string)
            else:
                # adding a new grouping in result and hash
                outRes.append([string])
                hashRes[string] = hashTemp

        return outRes
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
