class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    def __str__(self):
        return str(self.data)
    def getData(self): # accessor
        return self.data
    def getLeft(self): # accessor
        return self.left
    def getRight(self): # accessor
        return self.right
    def setData(self, data): # mutator
        self.data = data
    def setLeft(self, left): # mutator
        self.left = left
    def setRight(self, right): # mutator
        self.right = right

    def find(self, data):
        if self.data == data:
            return True
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        return False

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

