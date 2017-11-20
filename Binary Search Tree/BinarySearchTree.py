# The file contains the basic implementation of Binary Search Tree and some helper functiosn
# defining the class for declaring the Tree Node
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    # method to search the element in the BST and return thr node containing it
    def searchNode(self, root, key):
        # res is the node with the key
        if not root:
            return
        if root.val == key:
            return root
        elif root.val < key:
            res = self.searchNode(root.right, key)
        else:
            res = self.searchNode(root.left, key)
        return res

    def maxElem(self, root):
        if not root:
            return
        if root.right:
            return self.maxElem(root.right)
        else:
            return root

    #def insert(self,root,x):