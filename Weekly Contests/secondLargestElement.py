# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        if not root:
            return -1
        # case when both are present
        if root.left and root.right:
            lVal = root.left.val
            rVal = root.right.val
            if (lVal != root.val) and (rVal != root.val):
                return min(lVal, rVal)
            elif lVal != root.val:
                return lVal
            elif rVal != root.val:
                return rVal
            else:
                return -1
        # case of only left child :
        elif root.left:
            lVal = root.left.val
            if lVal != root.val:
                return lVal
            # call itself recursively for left child
            else:
                return self.findSecondMinimumValue(root.left)
        # case of only right child :
        elif root.right:
            rVal = root.right.val
            if rVal != root.val:
                return rVal
            # call itself recursively for left child
            else:
                return self.findSecondMinimumValue(root.right)
        # case of no child
        else:
            return -1
        """
        :type root: TreeNode
        :rtype: int
        """
