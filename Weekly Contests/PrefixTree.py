class Node(object):
    def __init__(self):
        self.children = {}
        self.eow = False


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        if not word:
            return
        tempPtr = self.root
        for c in word:
            if c not in tempPtr.children:
                tempPtr.children[c] = Node()
            tempPtr = tempPtr.children[c]
        tempPtr.eow = True
        return

    def search(self, word):
        if not word:
            return False
        tempPtr = self.root
        for c in word:
            if c not in tempPtr.children:
                return False
            tempPtr = tempPtr.children[c]
        if tempPtr.eow:
            return True
        else:
            return False

    def startsWith(self, prefix):
        if not prefix:
            return False
        tempPtr = self.root
        for c in prefix:
            if c not in tempPtr.children:
                return False
            tempPtr = tempPtr.children[c]

        """if not tempPtr.children :
            return False
        else :
            return True
        """
        return True


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)