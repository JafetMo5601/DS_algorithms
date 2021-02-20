class Stacks:
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        # self.stack[self.top] = None
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) > 0

    def top(self):
        return self.stack[-1]

    def printt(self):
        print(self.stack)

    def printStack(self):
        temp = self.top
        while(self.stack[temp]):
            if self.stack[temp] != None:
                print(self.stack[temp])
            temp -= 1

stack1 = Stacks()

stack1.printt()
stack1.push(1)
stack1.push(2)
stack1.printt()
stack1.pop()
stack1.push(3)
stack1.push(4)
stack1.printt()































#from queue import LifoQueue

# class Stack():

#     def __init__(self, size):
#         self.size = size
#         self.stack = LifoQueue(maxsize = self.size)

#     def getStackSize(self):
#         print(self.stack.qsize())

#     def push(self, data):

#         if self.stack.qsize() > self.size:
#             print('You cannot enter more data')
#         else:
#             self.stack.put(data)

#     def pop(self):
#         print(self.stack.get())

# stack1 = Stack(5)
# stack1.getStackSize()

# stack1.push(1)
# stack1.push(2)
# stack1.push(3)
# stack1.push(4)
# stack1.push(5)

# stack1.getStackSize()
