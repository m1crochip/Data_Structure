from LAB4_node import Node

class list:

    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
            self.SIZE = 0
        else:
            self.head = head
            self.tail = self.head
            self.SIZE = 1
            while t.

    def __str__(self):
        return str(self.head)

    def append(self, data):
        
    
    def size(self):
        return self.SIZE

    def isEmpty(self):
        if self.SIZE > 0:
            return False
        else: return True
    
    def addHead(self, data):
        self.head = data

    def getHead(self):
        return self.head
I = list()
I.append('A')
I.append('B')
I.append('C')
print(I)
print(I.size())
print(I.isEmpty())
print(I.head)
