"""
Solution to leetcode problem Word Search II : Problem 212
"""


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = ''


class Solution(object):
    def findWords(self, board, words):
        if not board:
            return
        root = self.populateTrie(words)
        res = []
        m = len(board)
        n = len(board[0])
        visitMat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(board, root, i, j, visitMat, res, m, n)

        return res

    # function for the dfs search on the board
    def dfs(self, board, node, i, j, visitMat, res, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] not in node.children:
            return
        if visitMat[i][j] == 1:
            return
        visitMat[i][j] = 1
        node = node.children[board[i][j]]
        if node.word:
            res.append(node.word)
            node.word = ''
        for row, col in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1):
            self.dfs(board, node, row, col, visitMat, res, m, n)
        visitMat[i][j] = 0
        return

    # function to poplulate the Trie
    def populateTrie(self, words):
        root = TrieNode()
        for word in words:
            tempPtr = root
            for c in word:
                if c not in tempPtr.children:
                    tempPtr.children[c] = TrieNode()
                tempPtr = tempPtr.children[c]
            tempPtr.word = word

        return root

