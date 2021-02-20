class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def newNode(self, value):
        return Node(value)

    def printInorder(self, node):
        if node:
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)

    def printPreorder(self, node):
        if node:
            print(node.value)
            self.printInorder(node.left)
            self.printInorder(node.right)

    def printPostorder(self, node):
        if node:
            self.printInorder(node.left)
            self.printInorder(node.right)
            print(node.value)

t = Tree()
root = t.newNode(1)
root.left = t.newNode(2)
root.right = t.newNode(3)
root.left.left = t.newNode(4)
root.left.right = t.newNode(5)

print("Inorder")
t.printInorder(root)
print("Preorder")
t.printPreorder(root)
print("Postorder")
t.printPostorder(root)
