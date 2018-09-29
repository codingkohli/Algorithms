class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
from collections import defaultdict
class Solution:

    def killProcess(pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        hashDict = defaultdict(list)
        queue = []
        result = []
        for i in range(len(ppid)):
            parent = ppid[i]
            if parent not  in hashDict:
                hashDict[parent] = []
            hashDict[parent].append(pid[i])
        queue.append(kill)
        print(hashDict)
        while queue:
           node = queue.pop(0)
           result.append(node)
           for child in hashDict[node]:
            queue.append(child)

        return result


pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
outRes = Solution.killProcess(pid, ppid, kill)
print(outRes)