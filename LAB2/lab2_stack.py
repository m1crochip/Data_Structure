class Stack:

    def __init__(self, list = None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def __init__(self):
        self.item = []
    
    def push(self, i):
        self.item.append(i)

    def size(self):
        return len(self.item)

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False
    
    def pop(self):
        self.item.pop()
    
    def remove(self, x):
        self.item.remove(x)

    def peek(self):
        return self.item[len(self.item)-1]

    def isFull(self):
        if len(self.item) < 4:
            return False
        else: return True
    