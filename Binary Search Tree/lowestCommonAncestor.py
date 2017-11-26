"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    if not root :
        return
    maxElem = max(v1,v2)
    minElem = min(v1,v2)
    prev = root
    curr = root
    while(curr) :
        if curr.data >= minElem and curr.data < maxElem :
            return curr
        elif curr.data < minElem :
            prev = curr
            curr = curr.right
        else :
            prev = curr
            curr = curr.left
    return prev