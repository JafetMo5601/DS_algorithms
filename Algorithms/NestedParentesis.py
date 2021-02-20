class Stack:
    def __init__(self):
        self.stack = []
        self.top = None

    def Enqueue(self, value):
        self.stack.append(value)
        self.setTop()

    def Dequeue(self):
        self.stack.pop()
        self.setTop()

    def setTop(self):
        if len(self.stack) != 0:
            self.top = self.stack[-1]
        else:
            self.top = None

    def printStack(self):
        print(self.stack)

    def isOpenParentesis(self, string):
        return string == '('

    def isClosedParentesis(self, string):
        return string == ')'

    def checkNestedParentesis(self, string):
        for i in string:
            if len(self.stack) == 0 and self.isClosedParentesis(i):
                return 0
            elif self.isOpenParentesis(i):
                self.Enqueue(i)
            elif self.isClosedParentesis(i):
                if self.top != None and self.top == '(':
                    self.Dequeue()
                else:
                    self.Enqueue(i)

        if len(self.stack) == 0:
            return 1
        else:
            return 0

s = Stack()
print(s.checkNestedParentesis('(()((u))())'))



