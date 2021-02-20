class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Python3 program to check
# if a given tree is BST.
import math

# A binary tree node has data,
# pointer to left child and
# a pointer to right child

def BST(root, prev):
    if (root != None):
        if BST(root.left, prev) == True:
            return False
        if prev != None and root.data <= prev.data:
            return False
        prev = root
        return BST(root.right, prev)
    return True

def isBST(root):
    prev = None
    return BST(root, prev)

# Driver Code
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)
    #root.right.left.left = Node(40)

    if (isBST(root) == None):
        print("Is BST")
    else:
        print("Not a BST")


# def isABnaryTree(node):
#     while node.value != None:
#         if node.left.value <= node.value and node.right.value >= node.value:
#             return True
#         elif node.left.value == None or node.right.value == None:
#             return False
#         else:
#             return False
#     #     print("Have children")
#     # print('no more children')

# if __name__ == '__main__':
#     root = Node(10)
#     root.left = Node(5)
#     root.right = Node(15)
#     root.left.left = Node(2)
#     root.left.right = Node(7)
#     root.right.left = Node(13)
#     root.right.right = Node(4)
#     print(isABnaryTree(root))

#           10
#         /    \
#        5     15
#       / \    / \
#      2   7  13  17
