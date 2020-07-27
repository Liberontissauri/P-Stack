
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
        temp = None
        while not self.isempty():
            if temp == None:
                temp = self.pop()
            if len(self.stack_copy)==0:
                self.stack_copy.append(temp)
                temp = None
            elif self.stack_copy[-1] >= temp:
                self.stack_copy.append(temp)
                temp = None
            else:
                self.push(self.stack_copy[-1])
                self.stack_copy.pop(-1)
        self.data = self.stack_copy

    def top_to_bottom(self):
        if len(self.stack_copy)!=0 and not self.isempty():
            self.stack_copy.insert(1,self.pop())
            self.top_to_bottom()
        elif not self.isempty():
            self.stack_copy.append(self.pop())
            self.top_to_bottom()
        
        self.data = self.stack_copy
        