
class Stack():
    def __init__(self, size = None):     # If the size is None, the stack has an undefined size
        self.data = []
        self.size = size
        self.stack_copy = []
    
    def isfull(self):
        if self.size == None:
            return False
        elif len(self.data) >= self.size:
            return True
        else:
            return False

    def isempty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def push(self,to_push):
        if not self.isfull():
            self.data.append(to_push)
        else:
            raise Exception("Stack Overflow")
    
    def pop(self):
        if not self.isempty():
            popped = self.data[-1]
            self.data.pop(-1)
            return popped
        else:
            raise Exception("Stack Underflow")
    
    def peek(self):
        if not self.isempty():
            return self.data[-1]
        else:
            return None

    def reverse(self):
        if not self.isempty():
            self.stack_copy.append(self.pop())
            self.reverse()
        self.data = self.stack_copy
        self.stack_copy = []

    def sort(self):
        self.data.sort()
