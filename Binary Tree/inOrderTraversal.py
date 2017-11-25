"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
# Expected output : a single line spacedoutput
def inOrder(root):
    if not root :
        return
    inOrder(root.left)
    print(root.data),
    inOrder(root.right)
    return
