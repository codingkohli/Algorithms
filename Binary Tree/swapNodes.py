"""
Input Format
First line of input contains N, number of nodes in tree. Then N lines follow. Here each of ith line (1 <= i <= N) contains two integers, a b, where a is the index of left child, and b is the index of right child of ith node. -1 is used to represent null node.
Next line contain an integer, T. Then again T lines follows. Each of these line contains an integer K.

Output Format
For each K, perform swap operation as mentioned above and print the inorder traversal of the current state of tree.

"""
#defining the swap function
def swapNodes(indx):
    if indx < 1 :
        return
    temp = left[indx - 1]
    left[indx - 1] = right[indx - 1]
    right[indx - 1] = temp

#printing the inorder sequence
def inOrder(indx) :
    if left[indx -1 ] != -1:
        inOrder(left[indx -1 ])
    print(indx),
    if right[indx -1 ] != -1:
        inOrder(right[indx -1 ])


# reading input from the STDIN
N = int(raw_input())

#creating the left and right nodes
left = []
right = []

#constructing the tree
for i in range(N) :
    x = raw_input().split()
    left.append(int(x[0]))
    right.append(int(x[1]))

# swapping and printing the inorder
K = int(raw_input())
for i in range(K) :
    sIndx = int(raw_input())
    swapNodes(sIndx)
    inOrder(sIndx)
    print("")

