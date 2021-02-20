class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isUnival(root):
    if root == None:
        return True

    return root.left == root.right

def counterUnivals(root):
    if isUnival(root):
        return 1
def None_empty(root):
    counter = 0

    if root.left == root.right:
        counter += 1
        None_empty(root.left)
        None_empty(root.right)

    return counter


#  Our example tree looks like this:
#         1 (root)
#       /   \
#      1     0
#           / \
#          1   0
#         / \
#        1   1

root = Node(0)
node1 = Node(1)
node0 = Node(0)

root.left = node1
root.right = node0
root.right.left = node1
root.right.left.left = node1
root.right.left.right = node1
root.right.right = node0

print("Sum of all values of this tree is (should print 20):")
print(None_empty(root))
