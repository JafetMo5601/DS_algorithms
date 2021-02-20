class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Trees:

    def newNode(self, value):
        return Node(value)

    def insert(self, value, node):
        if value < node.value:
            if node.left == None:
                node.left = self.newNode(value)
            else:
                self.insert(value, node.left)
        elif value > node.value:
            if node.right == None:
                node.right = self.newNode(value)
            else:
                self.insert(value, node.right)

    def search(self, value, node):
        if node is None or node == value:
            return node
        if node.value < value:
            return self.search(value, node.right)
        return self.search(value, node.left)

if __name__ == '__main__':
    t = Trees()
    root = t.newNode(50)
    root.left = t.newNode(25)
    root.right = t.newNode(75)
    t.insert(10, root)
    # print(root.left.left)
    t.search(25, root)
