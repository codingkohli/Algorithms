"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
# expected output : a single space characters
def postOrder(root):
    if not root :
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data),
    return