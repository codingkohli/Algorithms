#This file deals with basic methods for creating,searching and traversals in a binary tree

#class declaration of a node of a Binary Tree
class TreeNode:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

# Pre-order Traversal in a Binary Tree : root,left,right {Iterative approach}
def preOrder(root):
    if not root:
        return
    # the output for the preorder traversal
    res = []
    stackList = []
    res.append(root.value)
    stackList.append(root.left)
    stackList.append(root.right)
    while(stackList):
        temp = stackList.pop(0)
        if temp :
            res.append(temp.value)
            stackList.append(temp.left)
            stackList.append(temp.right)

    return res

# Pre-order Traversal in a Binary Tree : {Recursive Approach}
def preOrderRec(root) :
    if not root:
        return
    print(root.value)
    print(preOrder(root.left))
    print(preOrder(root.right))
    return
# Post-order Traversal in a Binary Tree : left,right,root {Recursive approach}
def postOrder(root):
    if root :
        # the output for the traversal
        outRes = []
        outRes.append(postOrder(root.left))
        outRes.append(postOrder(root.right))
        outRes.append(root.value)
        return outRes

# Creating a basic Binary Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# printing the pre-order Traversal
print(preOrder(root))

#printing the post-order Traversal
print(postOrder(root))

#printing the recursive aoorach for pre-order
print("The pre-order traversal as follows")
preOrderRec(root)

