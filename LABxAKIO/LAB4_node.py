class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data
    
    def setNext(self, next):
        self.next = next
    

a4 = Node('D')
a3 = Node('C',a4)
a2 = Node('B',a3)
a1 = Node('A',a2)

print(a1.getNext())

