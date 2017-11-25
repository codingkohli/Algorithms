# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

# exepected output : integer denoting the max height
def height(root):
    if not root :
        return 0
    lheight,rheight = 0,0
    if root.left :
        lheight = 1 + height(root.left)
    if root.right :
        rheight = 1 + height(root.right)
    return max(lheight ,rheight)