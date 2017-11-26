"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    if not root :
        return
    #using a queue to mantain the level order
    queue = []
    print(root.data),
    queue.append(root.left)
    queue.append(root.right)
    while queue :
        ptr =queue.pop(0)
        if ptr :
            print(ptr.data),
            queue.append(ptr.left)
            queue.append(ptr.right)
    return