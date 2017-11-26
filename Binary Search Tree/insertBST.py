"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if not r :
        r = None(val)
        return r
    # the pointer where the value is to be inserted
    ptr = r
    while(ptr):
        if ptr.data > val :
            if ptr.left :
                ptr = ptr.left
            else :
                break
        else :
            if ptr.right :
                ptr = ptr.right
            else :
                break
    if ptr.data > val :
        ptr.left = Node(val)
    else :
        ptr.right = Node(val)
    return r