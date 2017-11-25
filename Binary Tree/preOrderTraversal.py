"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
# expeceted output is to print in a single line
def preOrder(root):
    if not root :
        return
    print(root.data),
    preOrder(root.left)
    preOrder(root.right)
    return
