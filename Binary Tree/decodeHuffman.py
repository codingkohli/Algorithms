"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    if not root :
        return
    if not s :
        return
    outRes = ""
    ptr = root
    for i in range(len(s)) :
        if s[i] == "1" :
            if ptr.right :
                ptr = ptr.right
            else :
                outRes += str(ptr.data)
                ptr = root.right
        else :
            if ptr.left :
                ptr = ptr.left
            else :
                outRes += str(ptr.data)
                ptr = root.left
    # printing for the  last iteration
    outRes += str(ptr.data)
    print(outRes)
    return
