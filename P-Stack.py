
class Stack():
    def __init__(self, size = None):     # If the size is None, the stack has an undefined size
        self.data = []
        self.size = size
    
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
        if self.isfull() == False:
            self.data.append(to_push)
        else:
            raise Exception("Stack Overflow")
    
    def pop(self):
        if self.isempty()==False:
            self.data.pop(-1)
        else:
            raise Exception("Stack Underflow")
    
    def peek(self):
        if self.isempty()==False:
            return self.data[-1]
        else:
            return None
