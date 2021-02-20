class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class LinkedList:

    def __init__(self):
        self.head = None

    def newNode(self, newData):
        newNode = Node(newData)
        return newNode

    def push(self, node):
        node.next = self.head
        self.head = node

    def append(self, node):
        if self.head == None:
            self.push(node)
        else:
            last = self.head
            while (last.next):
                last = last.next
            last.next = node

    def insertAfter(self, prevNode, node):
        node.next = prevNode.next
        prevNode.next = node

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            print(" => ")
            temp = temp.next


if __name__ == '__main__':
    list = LinkedList()

    list.push(list.newNode(1))
    list.append(list.newNode(3))
    list.append(list.newNode(4))
    list.append(list.newNode(5))
    list.append(list.newNode(5))
    list.insertAfter(list.head, list.newNode(2))

    list.printLL()
