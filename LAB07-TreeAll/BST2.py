class Node:
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.parent =  None if parent is None else parent

    def __str__(self):
        return str(self.data)

    def isLeaft(self):
        return self.left is None and self.right is None
    
    def isParent(self):
        return not(self.isLeaft())
    
    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def path(self, data, path):
        if self.data == data:
            path.append(self.data)
        elif data < self.data:
            path.append(self.data)
            



# l = [14,4,9,7,15,3,18,16,20,5,16]
# x = 
# for ele in l:
#     x.insert(ele)


